#!/usr/bin/env python3
"""
Comprehensive investigation timeline - full analysis of all agentsview sessions.
"""

import json
import sys
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional

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

def extract_user_text(msg: any) -> str:
    """Extract text from message object which can be string or list."""
    if isinstance(msg, str):
        return msg
    elif isinstance(msg, list):
        result = []
        for item in msg:
            if isinstance(item, dict) and 'text' in item:
                result.append(item['text'])
            elif isinstance(item, str):
                result.append(item)
        return ' '.join(result)
    elif isinstance(msg, dict) and 'content' in msg:
        return extract_user_text(msg['content'])
    return str(msg)

def analyze_content(content: str, event: Dict) -> Tuple[Set[str], Set[str], List[str]]:
    """Analyze content to extract subjects, approaches, and tools."""
    subjects = set()
    approaches = set()
    files = set()

    content_lower = content.lower()

    # Identify subjects
    if any(word in content_lower for word in ['sysmon', 'sysmonconfig', 'xml config']):
        subjects.add('Sysmon Configuration')
    if any(word in content_lower for word in ['vector', 'json event', 'windows_event', '.json']):
        subjects.add('Vector Event Logs')
    if any(word in content_lower for word in ['network', 'traffic', 'pcap', 'wireshark', 'pdml']):
        subjects.add('Network Traffic Analysis')
    if any(word in content_lower for word in ['overwatch', 'gaming', 'game', 'monitor', 'steam']):
        subjects.add('Overwatch/Gaming Monitoring')
    if any(word in content_lower for word in ['validation', 'verify', 'validate', 'check', 'compare', 'correlation']):
        subjects.add('Validation & Verification')
    if any(word in content_lower for word in ['parquet', 'pdml', 'convert', 'transform', 'export']):
        subjects.add('Data Processing & Export')
    if any(word in content_lower for word in ['osquery', 'query', 'database']):
        subjects.add('System Queries (osquery)')

    # Identify approaches
    if any(word in content_lower for word in ['review', 'read', 'examine', 'analyze', 'explain']):
        approaches.add('Analysis & Review')
    if any(word in content_lower for word in ['create', 'write', 'modify', 'implement', 'generate']):
        approaches.add('Implementation & Creation')
    if any(word in content_lower for word in ['test', 'validate', 'verify', 'check']):
        approaches.add('Testing & Validation')
    if any(word in content_lower for word in ['compare', 'correlation', 'trace', 'map']):
        approaches.add('Correlation & Mapping')
    if any(word in content_lower for word in ['scan', 'search', 'query', 'retrieve']):
        approaches.add('Scanning & Querying')

    # Extract file references
    file_refs = re.findall(r'@([\w\-\.]+(?:\.py|\.xml|\.md|\.json|\.csv|\.parquet|\.pcapng|\.toml)?)', content)
    files.update(file_refs)

    return subjects, approaches, sorted(list(files))

def analyze_all_sessions(session_dir: Path) -> Dict:
    """Analyze all sessions."""

    hourly_data = defaultdict(lambda: {
        'tools': defaultdict(int),
        'subjects': defaultdict(int),
        'approaches': defaultdict(int),
        'event_count': 0,
        'sessions': set(),
        'activities': [],
        'files': set()
    })

    session_files = list(session_dir.glob('*.jsonl'))
    print(f"Processing {len(session_files)} session files...", file=sys.stderr)

    for session_file in sorted(session_files):
        session_id = session_file.stem[:12]
        print(f"  {session_id}...", file=sys.stderr)
        events = parse_session_file(session_file)

        for event in events:
            timestamp = event.get('timestamp')
            if not timestamp:
                continue

            hour_key = get_hour_key(timestamp)
            hourly_data[hour_key]['event_count'] += 1
            hourly_data[hour_key]['sessions'].add(session_id)

            # Track tools
            if event.get('type') == 'tool-call':
                tool = event.get('toolName', '')
                if tool:
                    hourly_data[hour_key]['tools'][tool] += 1

            # Process user messages
            if event.get('type') == 'user':
                msg = event.get('message', {})
                if isinstance(msg, dict):
                    content_raw = msg.get('content') or ''
                    content = extract_user_text(content_raw)

                    if content and len(content) > 20:
                        subjects, approaches, files = analyze_content(content, event)

                        for subject in subjects:
                            hourly_data[hour_key]['subjects'][subject] += 1
                        for approach in approaches:
                            hourly_data[hour_key]['approaches'][approach] += 1
                        for f in files:
                            hourly_data[hour_key]['files'].add(f)

                        # Record activity
                        activity_summary = content[:120].replace('\n', ' ')
                        hourly_data[hour_key]['activities'].append(activity_summary)

    return dict(hourly_data)

def generate_comprehensive_report(hourly_data: Dict) -> str:
    """Generate comprehensive markdown report."""
    lines = []

    lines.append("# Windows Investigation Timeline")
    lines.append("## Hour-by-Hour Breakdown of Investigation Activities\n")

    lines.append("### Investigation Summary")
    lines.append(f"- **Period**: {sorted(hourly_data.keys())[0]} to {sorted(hourly_data.keys())[-1]}")
    lines.append(f"- **Total hours**: {len(hourly_data)}")
    lines.append(f"- **Total events**: {sum(d['event_count'] for d in hourly_data.values())}")

    # Summary of subjects and approaches
    all_subjects = defaultdict(int)
    all_approaches = defaultdict(int)
    all_files = set()
    all_tools = defaultdict(int)

    for data in hourly_data.values():
        for subject, count in data['subjects'].items():
            all_subjects[subject] += count
        for approach, count in data['approaches'].items():
            all_approaches[approach] += count
        all_files.update(data['files'])
        for tool, count in data['tools'].items():
            all_tools[tool] += count

    lines.append("\n### Top Investigation Subjects")
    for subject, count in sorted(all_subjects.items(), key=lambda x: -x[1])[:10]:
        lines.append(f"- **{subject}**: {count} mentions")

    lines.append("\n### Primary Approaches Used")
    for approach, count in sorted(all_approaches.items(), key=lambda x: -x[1]):
        lines.append(f"- **{approach}**: {count} mentions")

    lines.append("\n### Most Frequently Used Tools")
    for tool, count in sorted(all_tools.items(), key=lambda x: -x[1])[:10]:
        lines.append(f"- `{tool}`: {count} calls")

    lines.append("\n### Key Files Referenced")
    for f in sorted(all_files)[:15]:
        lines.append(f"- `{f}`")

    # Hour-by-hour breakdown
    lines.append("\n\n## Hour-by-Hour Breakdown\n")

    for hour_key in sorted(hourly_data.keys()):
        data = hourly_data[hour_key]
        lines.append(f"### {hour_key}")
        lines.append(f"**Sessions**: {', '.join(sorted(list(data['sessions'])[:3]))}")
        lines.append(f"**Event Count**: {data['event_count']}")
        lines.append("")

        if data['subjects']:
            lines.append("**Investigation Focus**:")
            for subject, count in sorted(data['subjects'].items(), key=lambda x: -x[1]):
                lines.append(f"- {subject}")
        lines.append("")

        if data['approaches']:
            lines.append("**Approaches**:")
            for approach in sorted(data['approaches'].keys()):
                lines.append(f"- {approach}")
        lines.append("")

        if data['tools']:
            top_tools = sorted(data['tools'].items(), key=lambda x: -x[1])[:3]
            lines.append("**Tools Used**:")
            for tool, count in top_tools:
                lines.append(f"- `{tool}` ({count}x)")
        lines.append("")

        if data['files']:
            lines.append("**Files Worked With**:")
            for f in sorted(data['files'])[:5]:
                lines.append(f"- `{f}`")
        lines.append("")

        if data['activities']:
            lines.append("**Activities**:")
            for activity in data['activities'][:2]:
                clean = activity.replace('<', '').replace('>', '')
                if len(clean) > 10:
                    lines.append(f"- {clean}...")
        lines.append("")

    return "\n".join(lines)

def main():
    session_dir = Path("D:\\WindowsInvestigations\\agentsview")

    if not session_dir.exists():
        print(f"Error: {session_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    hourly_data = analyze_all_sessions(session_dir)
    report = generate_comprehensive_report(hourly_data)

    print(report)

    output_file = session_dir / "INVESTIGATION_TIMELINE.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {output_file}", file=sys.stderr)

if __name__ == "__main__":
    main()
