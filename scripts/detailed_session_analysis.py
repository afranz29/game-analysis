#!/usr/bin/env python3
"""
Detailed analysis of agentsview sessions with full tool and approach extraction.
"""

import json
import sys
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Set, Tuple

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

def get_hour_key(timestamp_str: str) -> str:
    """Convert timestamp to hour key."""
    try:
        dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:00')
    except:
        return "UNKNOWN"

def extract_tools_and_subjects(event: Dict) -> Tuple[Set[str], Set[str], str]:
    """Extract tools, subjects, and approaches from an event."""
    tools = set()
    subjects = set()
    approaches = []

    # Extract from message content
    if event.get('type') == 'user':
        msg = event.get('message', {})
        if isinstance(msg, dict):
            content_raw = msg.get('content') or ''
            if isinstance(content_raw, list):
                content = ' '.join(str(c.get('text', '')) if isinstance(c, dict) else str(c) for c in content_raw).lower()
            else:
                content = str(content_raw).lower()

            # Identify subjects
            if any(word in content for word in ['sysmon', 'sysmonconfig', 'xml config']):
                subjects.add('Sysmon Configuration')
            if any(word in content for word in ['vector', 'json events', 'windows_events']):
                subjects.add('Vector Event Logs')
            if any(word in content for word in ['network', 'traffic', 'pcap', 'wireshark']):
                subjects.add('Network Traffic Analysis')
            if any(word in content for word in ['overwatch', 'gaming', 'game', 'monitor']):
                subjects.add('Overwatch Application Monitoring')
            if any(word in content for word in ['validation', 'verify', 'validate', 'check', 'compare']):
                subjects.add('Validation & Verification')
            if any(word in content for word in ['parquet', 'pdml', 'convert', 'transform']):
                subjects.add('Data Conversion & Processing')

            # Identify approaches
            if 'read' in content or 'review' in content:
                approaches.append('Code Review')
            if 'analyze' in content or 'analysis' in content:
                approaches.append('Analysis')
            if 'create' in content or 'write' in content or 'implement' in content:
                approaches.append('Implementation')
            if 'test' in content or 'validate' in content:
                approaches.append('Testing')
            if 'compare' in content or 'correlation' in content:
                approaches.append('Correlation Analysis')

    # Extract from tool calls
    if event.get('type') == 'tool-call':
        tool_name = event.get('toolName', '')
        if tool_name:
            tools.add(tool_name)

    # Extract from content
    if event.get('type') == 'system':
        content = event.get('content', '')
        if '<tool-name>' in content:
            try:
                start = content.index('<tool-name>') + len('<tool-name>')
                end = content.index('</tool-name>')
                tools.add(content[start:end])
            except:
                pass

    return tools, subjects, ','.join(approaches) if approaches else ''

def analyze_all_sessions(session_dir: Path) -> Dict:
    """Analyze all sessions with detailed breakdown."""

    hourly_data = defaultdict(lambda: {
        'tools': defaultdict(int),
        'approaches': defaultdict(int),
        'subjects': defaultdict(int),
        'event_count': 0,
        'sessions': set(),
        'user_prompts': [],
        'key_files': set()
    })

    session_files = list(session_dir.glob('*.jsonl'))

    for session_file in sorted(session_files):
        session_id = session_file.stem[:12]
        events = parse_session_file(session_file)

        for event in events:
            timestamp = event.get('timestamp')
            if not timestamp:
                continue

            hour_key = get_hour_key(timestamp)
            hourly_data[hour_key]['event_count'] += 1
            hourly_data[hour_key]['sessions'].add(session_id)

            tools, subjects, approaches = extract_tools_and_subjects(event)

            # Track tools and subjects
            for tool in tools:
                if tool:
                    hourly_data[hour_key]['tools'][tool] += 1
            for subject in subjects:
                hourly_data[hour_key]['subjects'][subject] += 1
            if approaches:
                for approach in approaches.split(','):
                    hourly_data[hour_key]['approaches'][approach.strip()] += 1

            # Extract user prompts and file references
            if event.get('type') == 'user':
                msg = event.get('message', {})
                if isinstance(msg, dict):
                    content = msg.get('content') or ''
                    if content and len(content) > 20:
                        # Find file references
                        import re
                        files = re.findall(r'@([\w\.\-]+(?:\.py|\.xml|\.md|\.json|\.csv|\.parquet|\.pcapng)?)', content)
                        for f in files:
                            hourly_data[hour_key]['key_files'].add(f)

                        # Store prompt summary
                        prompt_summary = content[:100].replace('\n', ' ')
                        hourly_data[hour_key]['user_prompts'].append(prompt_summary)

    return dict(hourly_data)

def generate_detailed_report(hourly_data: Dict) -> str:
    """Generate a detailed markdown report."""
    lines = []
    lines.append("# Investigation Timeline - Hour-by-Hour Breakdown")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- **Total hours analyzed**: {len(hourly_data)}")
    lines.append(f"- **Date range**: {sorted(hourly_data.keys())[0]} to {sorted(hourly_data.keys())[-1]}")
    lines.append("")

    for hour_key in sorted(hourly_data.keys()):
        data = hourly_data[hour_key]
        lines.append(f"## {hour_key}")
        lines.append("")
        lines.append(f"**Sessions**: {', '.join(sorted(list(data['sessions'])[:3]))}")
        lines.append(f"**Event Count**: {data['event_count']}")
        lines.append("")

        if data['subjects']:
            lines.append("### Investigation Subjects")
            for subject, count in sorted(data['subjects'].items(), key=lambda x: -x[1]):
                lines.append(f"- **{subject}**: {count} mentions")
            lines.append("")

        if data['approaches']:
            lines.append("### Approaches Used")
            for approach, count in sorted(data['approaches'].items(), key=lambda x: -x[1]):
                lines.append(f"- **{approach}**: {count} times")
            lines.append("")

        if data['tools']:
            top_tools = sorted(data['tools'].items(), key=lambda x: -x[1])[:5]
            lines.append("### Tools Used (Top 5)")
            for tool, count in top_tools:
                lines.append(f"- `{tool}`: {count} calls")
            lines.append("")

        if data['key_files']:
            lines.append("### Key Files Referenced")
            for f in sorted(data['key_files'])[:5]:
                lines.append(f"- `{f}`")
            lines.append("")

        if data['user_prompts']:
            lines.append("### User Prompts")
            for prompt in data['user_prompts'][:2]:
                clean = prompt.replace('<', '').replace('>', '')
                if len(clean) > 10:
                    lines.append(f"- {clean}...")
            lines.append("")

    return "\n".join(lines)

def main():
    session_dir = Path("D:\\WindowsInvestigations\\agentsview")

    if not session_dir.exists():
        print(f"Error: {session_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    print("Analyzing sessions in detail...", file=sys.stderr)
    hourly_data = analyze_all_sessions(session_dir)

    report = generate_detailed_report(hourly_data)
    print(report)

    # Save report
    output_file = session_dir / "DETAILED_TIMELINE.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {output_file}", file=sys.stderr)

if __name__ == "__main__":
    main()
