#!/usr/bin/env python3
"""
Export investigation timeline to CSV for analysis.
"""

import json
import sys
import csv
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def parse_session_file(filepath: Path) -> list:
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

def extract_user_text(msg):
    """Extract text from message."""
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

def categorize_content(content: str):
    """Categorize content."""
    content_lower = content.lower()

    subjects = []
    if any(word in content_lower for word in ['sysmon', 'sysmonconfig']):
        subjects.append('Sysmon')
    if any(word in content_lower for word in ['vector', 'json event', 'windows_event']):
        subjects.append('Vector Logs')
    if any(word in content_lower for word in ['network', 'traffic', 'pcap']):
        subjects.append('Network')
    if any(word in content_lower for word in ['overwatch', 'gaming', 'steam']):
        subjects.append('Overwatch/Gaming')
    if any(word in content_lower for word in ['validation', 'verify', 'check']):
        subjects.append('Validation')
    if any(word in content_lower for word in ['parquet', 'pdml', 'convert']):
        subjects.append('Data Processing')

    approaches = []
    if any(word in content_lower for word in ['review', 'analyze', 'explain']):
        approaches.append('Analysis')
    if any(word in content_lower for word in ['create', 'write', 'modify']):
        approaches.append('Implementation')
    if any(word in content_lower for word in ['test', 'validate']):
        approaches.append('Testing')
    if any(word in content_lower for word in ['compare', 'correlation']):
        approaches.append('Correlation')

    return '|'.join(subjects) if subjects else '', '|'.join(approaches) if approaches else ''

def export_timeline():
    """Export timeline to CSV."""
    session_dir = Path("D:\\WindowsInvestigations\\agentsview")
    rows = []

    session_files = list(session_dir.glob('*.jsonl'))

    for session_file in sorted(session_files):
        session_id = session_file.stem[:12]
        events = parse_session_file(session_file)

        for event in events:
            if event.get('type') != 'user':
                continue

            timestamp = event.get('timestamp')
            if not timestamp:
                continue

            hour_key = get_hour_key(timestamp)
            msg = event.get('message', {})
            if isinstance(msg, dict):
                content = extract_user_text(msg.get('content') or '')

                if content and len(content) > 20:
                    subjects, approaches = categorize_content(content)
                    content_preview = content[:150].replace('\n', ' ')

                    rows.append({
                        'Timestamp': timestamp[:16],
                        'Hour': hour_key,
                        'Session': session_id,
                        'Subjects': subjects,
                        'Approaches': approaches,
                        'Activity Summary': content_preview
                    })

    # Write CSV
    output_file = session_dir / "investigation_timeline.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        if rows:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

    print(f"Exported {len(rows)} rows to {output_file}", file=sys.stderr)

if __name__ == "__main__":
    export_timeline()
