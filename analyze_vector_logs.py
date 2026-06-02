import json
from collections import Counter

event_types = Counter()
processes = Counter()
overwatch_events = []
dns_queries = []
network_connections = []

with open(r'D:\WindowsInvestigations\vector-json\windows_events-2026-06-02.json', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i > 10000:  # Sample first 10k events
            break
        try:
            event = json.loads(line)
            event_id = event.get('event_id', 'N/A')
            event_types[event_id] += 1

            event_data = event.get('event_data', {})
            image = event_data.get('Image', '')
            if image:
                processes[image.lower()] += 1

            # Track Overwatch-related events
            event_str = json.dumps(event).lower()
            if 'overwatch' in event_str or 'battle' in event_str or 'blizzard' in event_str:
                overwatch_events.append(event)

                # Categorize by event type
                if event_id == 22:  # DNS Query
                    dns_queries.append({
                        'Image': image,
                        'QueryName': event_data.get('QueryName', 'N/A')
                    })
                elif event_id == 3:  # Network Connection
                    network_connections.append({
                        'Image': image,
                        'DestinationHostname': event_data.get('DestinationHostname', 'N/A'),
                        'DestinationIp': event_data.get('DestinationIp', 'N/A'),
                        'DestinationPort': event_data.get('DestinationPort', 'N/A')
                    })

        except:
            continue

print('=' * 60)
print('EVENT TYPE DISTRIBUTION (First 10,000 events)')
print('=' * 60)
for event_id, count in event_types.most_common(15):
    print(f'{event_id}: {count}')

print('\n' + '=' * 60)
print('TOP PROCESSES')
print('=' * 60)
for proc, count in list(processes.most_common(25)):
    print(f'{proc}: {count}')

print('\n' + '=' * 60)
print(f'OVERWATCH/BLIZZARD EVENTS FOUND: {len(overwatch_events)}')
print('=' * 60)

print('\n--- DNS QUERIES (Event ID 22) ---')
for i, dns in enumerate(dns_queries[:15]):
    print(f"{dns['Image']} -> {dns['QueryName']}")

print('\n--- NETWORK CONNECTIONS (Event ID 3) ---')
for i, conn in enumerate(network_connections[:15]):
    print(f"{conn['Image']} -> {conn['DestinationHostname']} ({conn['DestinationIp']}:{conn['DestinationPort']})")

print('\n--- SAMPLE EVENT DETAILS ---')
if overwatch_events:
    print(json.dumps(overwatch_events[0], indent=2))
