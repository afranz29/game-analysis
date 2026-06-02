#!/usr/bin/env python3
"""
Analyze agentsview sessions to trace tools, approaches, and subjects
by hour-by-hour timeline.
"""

import json
import sys
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

# Fix stdout encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def parse_session_file(filepath: Path) -> List[Dict]:
    """Parse a JSONL session file."""
    events = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if line.strip():
                    try:
                        events.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
    return events

def extract_tool_name(event: Dict) -> Optional[str]:
    """Extract tool name from event."""
    if event.get('type') == 'tool-call':
        return event.get('toolName')
    if event.get('type') == 'system' and event.get('subtype') == 'tool':
        content = event.get('content', '')
        if '<tool-name>' in content:
            start = content.index('<tool-name>') + len('<tool-name>')
            end = content.index('</tool-name>')
            return content[start:end]
    return None

def extract_message_content(event: Dict) -> str:
    """Extract message content from event."""
    if event.get('type') == 'user':
        msg = event.get('message', {})
        if isinstance(msg, dict):
            content = msg.get('content', '')
            if isinstance(content, str):
                return content[:200]  # First 200 chars
    elif event.get('type') == 'assistant':
        msg = event.get('message', {})
        if isinstance(msg, dict):
            content = msg.get('content', '')
            if isinstance(content, str):
                return content[:200]
    return ""

def get_hour_key(timestamp_str: str) -> Optional[str]:
    """Convert timestamp to hour key YYYY-MM-DD HH:00."""
    try:
        dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:00')
    except:
        return None

def analyze_sessions(session_dir: Path) -> Dict:
    """Analyze all sessions and organize by hour."""

    hourly_data = defaultdict(lambda: {
        'tools': defaultdict(int),
        'subjects': [],
        'messages': [],
        'events_count': 0,
        'sessions': set()
    })

    session_files = list(session_dir.glob('*.jsonl'))
    print(f"Found {len(session_files)} session files", file=sys.stderr)

    for session_file in sorted(session_files):
        session_id = session_file.stem
        print(f"Processing: {session_id}", file=sys.stderr)

        events = parse_session_file(session_file)

        for event in events:
            timestamp = event.get('timestamp')
            if not timestamp:
                continue

            hour_key = get_hour_key(timestamp)
            if not hour_key:
                continue

            hourly_data[hour_key]['events_count'] += 1
            hourly_data[hour_key]['sessions'].add(session_id[:16])  # Shortened ID

            # Extract tool usage
            tool = extract_tool_name(event)
            if tool:
                hourly_data[hour_key]['tools'][tool] += 1

            # Extract user prompts and assistant responses
            if event.get('type') == 'user':
                content = extract_message_content(event)
                if content:
                    hourly_data[hour_key]['messages'].append(('USER', content))
                    # Try to identify subject
                    content_lower = content.lower()
                    if any(word in content_lower for word in ['sysmon', 'config']):
                        hourly_data[hour_key]['subjects'].append('Sysmon Configuration')
                    if any(word in content_lower for word in ['vector', 'events', 'json']):
                        hourly_data[hour_key]['subjects'].append('Vector Events')
                    if any(word in content_lower for word in ['network', 'traffic', 'pcap']):
                        hourly_data[hour_key]['subjects'].append('Network Traffic')
                    if any(word in content_lower for word in ['overwatch', 'monitoring']):
                        hourly_data[hour_key]['subjects'].append('Overwatch Monitoring')
                    if any(word in content_lower for word in ['validate', 'verify', 'check']):
                        hourly_data[hour_key]['subjects'].append('Validation/Verification')

    return dict(hourly_data)

def format_report(hourly_data: Dict) -> str:
    """Format analysis as a readable report."""
    report = []
    report.append("=" * 80)
    report.append("AGENTSVIEW SESSION ANALYSIS - HOUR-BY-HOUR TIMELINE")
    report.append("=" * 80)
    report.append("")

    for hour_key in sorted(hourly_data.keys()):
        data = hourly_data[hour_key]

        report.append(f"\n{'─' * 80}")
        report.append(f"TIME: {hour_key}")
        report.append(f"{'─' * 80}")
        report.append(f"Sessions Active: {', '.join(sorted(data['sessions']))}")
        report.append(f"Total Events: {data['events_count']}")

        if data['tools']:
            report.append("\nTools Used:")
            for tool, count in sorted(data['tools'].items(), key=lambda x: -x[1]):
                report.append(f"  • {tool}: {count} times")

        if data['subjects']:
            unique_subjects = list(set(data['subjects']))
            report.append("\nInvestigation Subjects:")
            for subject in sorted(unique_subjects):
                report.append(f"  • {subject}")

        if data['messages']:
            report.append("\nKey Prompts/Activities:")
            # Show first few messages
            for msg_type, content in data['messages'][:3]:
                clean_content = content.replace('\n', ' ')[:100]
                report.append(f"  [{msg_type}] {clean_content}...")

    report.append("\n" + "=" * 80)
    return "\n".join(report)

def main():
    session_dir = Path("D:\\WindowsInvestigations\\agentsview")

    if not session_dir.exists():
        print(f"Error: {session_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    print(f"Analyzing sessions from: {session_dir}", file=sys.stderr)
    hourly_data = analyze_sessions(session_dir)

    report = format_report(hourly_data)
    print(report, file=sys.stdout)

    # Save to markdown
    output_file = Path("D:\\WindowsInvestigations\\agentsview\\SESSION_ANALYSIS.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"\nReport saved to: {output_file}", file=sys.stderr)

if __name__ == "__main__":
    main()
