import pandas as pd
import numpy as np
from datetime import datetime

def analyze_packet_frequency(file_path):
    print(f"Analyzing packet frequency in {file_path}...")
    df = pd.read_parquet(file_path)
    
    # Simple heuristic for gameplay traffic:
    # High frequency UDP packets to/from the same IP
    
    # Filter for UDP
    udp_df = df[df['protocol'] == 'UDP'].copy()
    
    # Convert timestamp string to datetime if possible, otherwise use numeric if it was epoch
    # In our conversion script, it was the 'show' value which is a string
    # Let's try to parse the relative time if available, or just use indices as a proxy for frequency
    
    # The timestamp in PDML looks like "May 31, 2026 15:32:16..."
    # A better way is to use the relative time from the beginning of the capture
    # But since we have the data, let's just group by second if possible
    
    try:
        # Example: "May 31, 2026 15:32:16.181423800"
        # We'll extract the core time and convert to datetime
        df['dt'] = pd.to_datetime(df['timestamp'].str.slice(0, 24), format='%b %d, %Y %H:%M:%S')
        
        # Group by second and count packets
        pps = df.groupby(df['dt'].dt.second).size()
        print("\nPackets Per Second (Distribution):")
        print(pps.describe())
        
        # Focus on the most active second
        most_active_sec = pps.idxmax()
        print(f"\nPeak activity at second {most_active_sec}: {pps.max()} packets")
        
    except Exception as e:
        print(f"\nCould not parse timestamps for frequency analysis: {e}")
        print("Falling back to packet-to-packet delta analysis.")

    # Calculate packet size distribution for gameplay candidates
    # We'll look at the IP we identified earlier (24.105.60.145)
    target_ip = '24.105.60.145'
    game_traffic = udp_df[(udp_df['src_ip'] == target_ip) | (udp_df['dst_ip'] == target_ip)]
    
    if not game_traffic.empty:
        print(f"\nAnalyzing signature for IP: {target_ip}")
        print(f"Total packets: {len(game_traffic)}")
        print("\nPacket Size Summary:")
        print(game_traffic['length'].describe())
        
        # In gaming, we expect a tight distribution of small packets
        print("\nPacket Size Distribution (Value Counts):")
        print(game_traffic['length'].value_counts().head(10))
    else:
        print(f"\nNo traffic found for target IP {target_ip}")

if __name__ == "__main__":
    analyze_packet_frequency('ow-network-traffic.parquet')
