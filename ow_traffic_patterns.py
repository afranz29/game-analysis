import pandas as pd
import numpy as np

def identify_overwatch_traffic(file_path):
    print(f"Analyzing {file_path} for Overwatch patterns...")
    df = pd.read_parquet(file_path)
    
    # Known Blizzard IP ranges (partial list)
    # Blizzard often uses 24.105.0.0/18, 37.244.0.0/16, etc.
    blizzard_ips = ['24.105.', '37.244.', '137.221.', '117.52.']
    
    def is_blizzard(ip):
        if pd.isna(ip): return False
        return any(ip.startswith(prefix) for prefix in blizzard_ips)

    # Filter for potential OW traffic
    df['is_blizzard_src'] = df['src_ip'].apply(is_blizzard)
    df['is_blizzard_dst'] = df['dst_ip'].apply(is_blizzard)
    
    ow_df = df[df['is_blizzard_src'] | df['is_blizzard_dst']].copy()
    
    print(f"\nPotential Overwatch Packets Found: {len(ow_df)} ({len(ow_df)/len(df)*100:.2f}% of total)")
    
    # Analyze by Protocol
    print("\nProtocol Distribution:")
    print(ow_df['protocol'].value_counts())
    
    # Analyze Top Server IPs
    print("\nTop Blizzard Server IPs:")
    server_ips = ow_df.apply(lambda x: x['src_ip'] if x['is_blizzard_src'] else x['dst_ip'], axis=1)
    print(server_ips.value_counts().head(10))
    
    # Analyze Port Usage
    print("\nCommon Destination Ports (Blizzard Bound):")
    dest_ports = ow_df[ow_df['is_blizzard_dst']]['dst_port']
    print(dest_ports.value_counts().head(5))
    
    print("\nCommon Source Ports (From Blizzard):")
    src_ports = ow_df[ow_df['is_blizzard_src']]['src_port']
    print(src_ports.value_counts().head(5))

    # Summary of Game Signature
    gameplay_udp = ow_df[ow_df['protocol'] == 'UDP']
    if not gameplay_udp.empty:
        avg_size = gameplay_udp['length'].mean()
        print(f"\nAverage UDP Packet Size: {avg_size:.2f} bytes")
        print("Signature: Gameplay traffic typically consists of small, frequent UDP packets.")

if __name__ == "__main__":
    identify_overwatch_traffic('ow-network-traffic.parquet')
