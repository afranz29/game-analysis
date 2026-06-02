import json
from collections import Counter

overwatch_processes = set()
battle_net_processes = set()
blizzard_dns = []
blizzard_network = []
process_events = []
file_events = []

print("Scanning entire file for Overwatch/Blizzard activity...")

with open(r'D:\WindowsInvestigations\vector-json\windows_events-2026-06-02.json', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i % 10000 == 0:
            print(f"  Processed {i} events...")

        try:
            event = json.loads(line)
            event_id = event.get('event_id')
            event_data = event.get('event_data', {})
            image = event_data.get('Image', '').lower()

            # Check for Overwatch/Battle.net processes
            if 'overwatch' in image or 'battle.net' in image or 'agent.exe' in image:
                overwatch_processes.add(image)

                if event_id == 1:  # Process Create
                    process_events.append({
                        'type': 'Process Create',
                        'time': event_data.get('UtcTime', 'N/A'),
                        'image': image,
                        'commandline': event_data.get('CommandLine', 'N/A')[:100]
                    })
                elif event_id == 5:  # Process Terminate
                    process_events.append({
                        'type': 'Process Terminate',
                        'time': event_data.get('UtcTime', 'N/A'),
                        'image': image
                    })
                elif event_id == 11:  # File Create
                    target = event_data.get('TargetFilename', '')
                    if 'overwatch' in target.lower() or 'battle' in target.lower():
                        file_events.append({
                            'image': image,
                            'target': target[:100]
                        })

            # Check for Blizzard DNS queries
            query_name = event_data.get('QueryName', '').lower()
            if 'blizzard' in query_name or 'battle.net' in query_name or 'overwatch' in query_name:
                blizzard_dns.append({
                    'image': image,
                    'query': query_name,
                    'time': event_data.get('UtcTime', 'N/A')
                })

            # Check for Blizzard network connections
            dest_hostname = event_data.get('DestinationHostname', '').lower()
            if 'blizzard' in dest_hostname or 'battle' in dest_hostname:
                blizzard_network.append({
                    'image': image,
                    'dest': dest_hostname,
                    'ip': event_data.get('DestinationIp', 'N/A'),
                    'port': event_data.get('DestinationPort', 'N/A'),
                    'time': event_data.get('UtcTime', 'N/A')
                })

        except Exception as e:
            continue

print("\n" + "=" * 70)
print("RESULTS")
print("=" * 70)

print(f"\nOverwatch/Battle.net Processes Found: {len(overwatch_processes)}")
for proc in sorted(overwatch_processes):
    print(f"  - {proc}")

print(f"\nProcess Events: {len(process_events)}")
for evt in process_events[:20]:
    print(f"  [{evt.get('type')}] {evt.get('time')} - {evt.get('image')}")
    if 'commandline' in evt:
        print(f"    CMD: {evt['commandline']}")

print(f"\nFile Events: {len(file_events)}")
for evt in file_events[:10]:
    print(f"  {evt['image']} -> {evt['target']}")

print(f"\nDNS Queries to Blizzard: {len(blizzard_dns)}")
for evt in blizzard_dns[:15]:
    print(f"  {evt['time']} - {evt['image']} -> {evt['query']}")

print(f"\nNetwork Connections to Blizzard: {len(blizzard_network)}")
for evt in blizzard_network[:15]:
    print(f"  {evt['time']} - {evt['image']} -> {evt['dest']} ({evt['ip']}:{evt['port']})")
