import pandas as pd
import subprocess
import json

def get_osquery_connections():
    # Run osquery to get current process/socket mapping
    cmd = [
        "C:\\Program Files\\osquery\\osqueryi.exe",
        "--json",
        "SELECT p.name, p.pid, pos.remote_address, pos.remote_port FROM processes p JOIN process_open_sockets pos ON p.pid = pos.pid WHERE pos.remote_address NOT IN ('0', '0.0.0.0', '::', '127.0.0.1') AND pos.remote_address != '';"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return json.loads(result.stdout)
    return []

def correlate():
    print("Loading network mapping from Parquet...")
    df = pd.read_parquet('ow-network-traffic-enriched.parquet')
    
    # Build IP to Hostname mapping from SNI and DNS
    # We'll use both src and dst to build a comprehensive map of what IPs belong to what names
    mapping = {}
    
    # Process SNI
    sni_df = df[df['tls_sni'].notna()]
    for _, row in sni_df.iterrows():
        mapping[row['dst_ip']] = row['tls_sni']
        
    # Process DNS
    # Note: In our current parquet, we only have queries, not the IP responses.
    # But we can infer from SNI for most Blizzard traffic.
    
    # Hardcoded mappings from OVERWATCH.md and previous analysis
    overwatch_known_ips = {
        '24.105.60.145': 'Blizzard Gameplay (UDP)',
        '24.105.60.232': 'Blizzard Gameplay (UDP)',
        '34.182.236.194': 'Overwatch Active Session (AWS)',
        '35.201.91.89': 'overwatch.ingest.gdp.blizzard.com',
        '137.221.105.136': 'telemetry-in.battle.net',
        '137.221.105.232': 'telemetry-in.battle.net',
        '100.20.157.63': 'oauth.battle.net',
        '52.38.105.79': 'oauth.battle.net',
        '34.210.233.116': 'account.battle.net',
        '136.110.188.211': 'us.version.battle.net',
        '3.170.42.8': 'public.games.geforce.com (NVIDIA Overlay)'
    }
    
    mapping.update(overwatch_known_ips)
    
    print("Retrieving live process connections from osquery...")
    connections = get_osquery_connections()
    
    report = []
    for conn in connections:
        ip = conn['remote_address']
        hostname = mapping.get(ip, "Unknown (No SNI match)")
        
        # Heuristic for Blizzard IPs we identified earlier if SNI is missing
        if hostname == "Unknown (No SNI match)":
            if ip.startswith('24.105.') or ip.startswith('37.244.'):
                hostname = "Blizzard Infrastructure (Probable Gameplay/Control)"
            elif ip.startswith('137.221.'):
                hostname = "Blizzard/Battle.net (Probable Telemetry/CDN)"
            elif ip.startswith('104.18.'):
                hostname = "Cloudflare (Probable Blizzard CDN/Frontend)"
        
        report.append({
            'Process': conn['name'],
            'PID': conn['pid'],
            'Remote IP': ip,
            'Remote Port': conn['remote_port'],
            'Hostname/Service': hostname
        })
    
    report_df = pd.DataFrame(report)
    
    if not report_df.empty:
        # Group and count to see which processes are most active
        print("\n--- Correlated Network Activity Report ---")
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.width', 1000)
        
        # Sort by Process name
        summary = report_df.sort_values(by='Process')
        print(summary[['Process', 'Remote IP', 'Hostname/Service']].to_string(index=False))
    else:
        print("No active external connections found.")

if __name__ == "__main__":
    correlate()
