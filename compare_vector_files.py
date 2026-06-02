"""
Compare vector-json vs vector-json-old files
Identifies filtering, time ranges, and content differences
"""

import json
import sys
from collections import Counter
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 80)
print("VECTOR-JSON vs VECTOR-JSON-OLD COMPARISON")
print("=" * 80)
print()

# File paths
file1 = r'D:\WindowsInvestigations\vector-json\windows_events-2026-06-02.json'
file2 = r'D:\WindowsInvestigations\vector-json-old\windows_events-2026-06-02.json'

def analyze_file(filepath, label):
    """Analyze a Vector JSON file and return statistics"""
    stats = {
        'label': label,
        'total_events': 0,
        'event_types': Counter(),
        'processes': Counter(),
        'timestamps': [],
        'overwatch_events': 0,
        'battle_net_events': 0,
        'steam_events': 0,
        'dns_queries': [],
        'network_connections': 0,
        'first_event': None,
        'last_event': None,
    }

    print(f"Analyzing {label}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i % 10000 == 0 and i > 0:
                print(f"  Processed {i:,} events...")

            try:
                event = json.loads(line)
                stats['total_events'] += 1

                event_id = event.get('event_id')
                stats['event_types'][event_id] += 1

                timestamp = event.get('timestamp')
                if timestamp:
                    stats['timestamps'].append(timestamp)
                    if stats['first_event'] is None:
                        stats['first_event'] = timestamp
                    stats['last_event'] = timestamp

                event_data = event.get('event_data', {})
                image = event_data.get('Image', '').lower()

                if image:
                    stats['processes'][image] += 1

                    if 'overwatch' in image:
                        stats['overwatch_events'] += 1
                    if 'battle' in image:
                        stats['battle_net_events'] += 1
                    if 'steam' in image:
                        stats['steam_events'] += 1

                # Track DNS queries
                if event_id == 22:
                    query_name = event_data.get('QueryName', '').lower()
                    if query_name:
                        stats['dns_queries'].append(query_name)

                # Track network connections
                if event_id == 3:
                    stats['network_connections'] += 1

            except:
                continue

    print(f"  ✅ Completed: {stats['total_events']:,} events")
    print()
    return stats

# Analyze both files
print("File 1: vector-json/")
stats1 = analyze_file(file1, "vector-json")

print("File 2: vector-json-old/")
stats2 = analyze_file(file2, "vector-json-old")

# Comparison
print("=" * 80)
print("COMPARISON RESULTS")
print("=" * 80)
print()

print("1. FILE SIZE COMPARISON")
print("-" * 80)
print(f"{'Metric':<30} {'vector-json':>20} {'vector-json-old':>20} {'Difference':>15}")
print("-" * 80)
print(f"{'Total Events':<30} {stats1['total_events']:>20,} {stats2['total_events']:>20,} {stats2['total_events'] - stats1['total_events']:>15,}")
print(f"{'Ratio':<30} {'':>20} {f'{stats2['total_events'] / stats1['total_events']:.2f}x':>20} {'':>15}")
print()

print("2. TIME RANGE COMPARISON")
print("-" * 80)
if stats1['first_event'] and stats2['first_event']:
    print(f"vector-json:")
    print(f"  First event: {stats1['first_event']}")
    print(f"  Last event:  {stats1['last_event']}")
    print()
    print(f"vector-json-old:")
    print(f"  First event: {stats2['first_event']}")
    print(f"  Last event:  {stats2['last_event']}")
    print()

    # Calculate duration
    try:
        time1_start = datetime.fromisoformat(stats1['first_event'].replace('Z', '+00:00'))
        time1_end = datetime.fromisoformat(stats1['last_event'].replace('Z', '+00:00'))
        duration1 = time1_end - time1_start

        time2_start = datetime.fromisoformat(stats2['first_event'].replace('Z', '+00:00'))
        time2_end = datetime.fromisoformat(stats2['last_event'].replace('Z', '+00:00'))
        duration2 = time2_end - time2_start

        print(f"Duration:")
        print(f"  vector-json:     {duration1}")
        print(f"  vector-json-old: {duration2}")
    except:
        pass
print()

print("3. EVENT TYPE DISTRIBUTION")
print("-" * 80)
print(f"{'Event ID':<15} {'vector-json':>20} {'vector-json-old':>20} {'Difference':>15}")
print("-" * 80)

all_event_ids = set(stats1['event_types'].keys()) | set(stats2['event_types'].keys())
for event_id in sorted(all_event_ids):
    count1 = stats1['event_types'].get(event_id, 0)
    count2 = stats2['event_types'].get(event_id, 0)
    diff = count2 - count1
    diff_str = f"{diff:+,}" if diff != 0 else "0"

    pct1 = (count1 / stats1['total_events'] * 100) if stats1['total_events'] > 0 else 0
    pct2 = (count2 / stats2['total_events'] * 100) if stats2['total_events'] > 0 else 0

    print(f"{str(event_id):<15} {f'{count1:,} ({pct1:.1f}%)':>20} {f'{count2:,} ({pct2:.1f}%)':>20} {diff_str:>15}")
print()

print("4. GAMING PROCESS ACTIVITY")
print("-" * 80)
print(f"{'Process Type':<30} {'vector-json':>20} {'vector-json-old':>20} {'Difference':>15}")
print("-" * 80)
print(f"{'Overwatch events':<30} {stats1['overwatch_events']:>20,} {stats2['overwatch_events']:>20,} {stats2['overwatch_events'] - stats1['overwatch_events']:>15,}")
print(f"{'Battle.net events':<30} {stats1['battle_net_events']:>20,} {stats2['battle_net_events']:>20,} {stats2['battle_net_events'] - stats1['battle_net_events']:>15,}")
print(f"{'Steam events':<30} {stats1['steam_events']:>20,} {stats2['steam_events']:>20,} {stats2['steam_events'] - stats1['steam_events']:>15,}")
print()

print("5. NETWORK ACTIVITY")
print("-" * 80)
print(f"{'Metric':<30} {'vector-json':>20} {'vector-json-old':>20} {'Difference':>15}")
print("-" * 80)
print(f"{'Event ID 3 (Network)':<30} {stats1['network_connections']:>20,} {stats2['network_connections']:>20,} {stats2['network_connections'] - stats1['network_connections']:>15,}")
print(f"{'Event ID 22 (DNS)':<30} {len(stats1['dns_queries']):>20,} {len(stats2['dns_queries']):>20,} {len(stats2['dns_queries']) - len(stats1['dns_queries']):>15,}")
print()

print("6. TOP PROCESSES COMPARISON")
print("-" * 80)
print("Top 10 processes in vector-json:")
for proc, count in stats1['processes'].most_common(10):
    proc_name = proc.split('\\')[-1] if '\\' in proc else proc
    print(f"  {count:6,} - {proc_name}")

print()
print("Top 10 processes in vector-json-old:")
for proc, count in stats2['processes'].most_common(10):
    proc_name = proc.split('\\')[-1] if '\\' in proc else proc
    print(f"  {count:6,} - {proc_name}")
print()

print("7. UNIQUE DNS QUERIES")
print("-" * 80)
unique_dns1 = set(stats1['dns_queries'])
unique_dns2 = set(stats2['dns_queries'])

only_in_1 = unique_dns1 - unique_dns2
only_in_2 = unique_dns2 - unique_dns1
in_both = unique_dns1 & unique_dns2

print(f"Unique DNS queries in vector-json:     {len(unique_dns1)}")
print(f"Unique DNS queries in vector-json-old: {len(unique_dns2)}")
print(f"In both:                               {len(in_both)}")
print(f"Only in vector-json:                   {len(only_in_1)}")
print(f"Only in vector-json-old:               {len(only_in_2)}")
print()

if only_in_1:
    print("DNS queries ONLY in vector-json:")
    for dns in sorted(only_in_1):
        if 'blizzard' in dns or 'battle' in dns or 'overwatch' in dns:
            print(f"  • {dns}")

if only_in_2:
    print("\nDNS queries ONLY in vector-json-old:")
    for dns in sorted(only_in_2)[:20]:
        if 'blizzard' in dns or 'battle' in dns or 'overwatch' in dns:
            print(f"  • {dns}")
print()

print("=" * 80)
print("ANALYSIS CONCLUSION")
print("=" * 80)
print()

# Determine the relationship
ratio = stats2['total_events'] / stats1['total_events'] if stats1['total_events'] > 0 else 0

if ratio > 5:
    print(f"📊 vector-json-old is {ratio:.1f}x LARGER than vector-json")
    print()
    print("Possible explanations:")
    print("  1. vector-json is a FILTERED/SAMPLED version")
    print("  2. vector-json-old is the COMPLETE capture")
    print("  3. Different time windows captured")
    print("  4. Different Vector configurations (filtering rules)")
elif ratio < 0.5:
    print(f"📊 vector-json is {1/ratio:.1f}x LARGER than vector-json-old")
    print()
    print("Possible explanations:")
    print("  1. vector-json-old is a FILTERED/SAMPLED version")
    print("  2. vector-json is the COMPLETE capture")
else:
    print(f"📊 Files are similar in size (ratio: {ratio:.2f}x)")
    print()
    print("Likely different time windows or slight variations in capture")

print()
if stats1['first_event'] and stats2['first_event']:
    if stats1['first_event'] != stats2['first_event']:
        print("⚠️ DIFFERENT TIME RANGES - these capture different periods!")
    else:
        print("✅ SAME START TIME - likely same capture with different filtering")
