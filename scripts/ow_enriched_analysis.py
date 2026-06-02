import pandas as pd

def analyze_enriched_traffic(file_path):
    print(f"Analyzing enriched traffic in {file_path}...")
    df = pd.read_parquet(file_path)
    
    # 1. DNS Queries
    if 'dns_query' in df.columns:
        print("\nTop DNS Queries:")
        dns_counts = df['dns_query'].value_counts()
        print(dns_counts.head(20))
        
        # Look specifically for Blizzard/Overwatch related DNS
        ow_dns = dns_counts[dns_counts.index.str.contains('blizzard|battle.net|overwatch', case=False, na=False)]
        if not ow_dns.empty:
            print("\nBlizzard/Overwatch DNS matches:")
            print(ow_dns)
    
    # 2. TLS SNI Hostnames
    if 'tls_sni' in df.columns:
        print("\nTop TLS SNI Hostnames:")
        sni_counts = df['tls_sni'].value_counts()
        print(sni_counts.head(10))
        
        # Look specifically for Blizzard/Overwatch related SNI
        ow_sni = sni_counts[sni_counts.index.str.contains('blizzard|battle.net|overwatch', case=False, na=False)]
        if not ow_sni.empty:
            print("\nBlizzard/Overwatch SNI matches:")
            print(ow_sni)

    # 3. TLS Versions and Ciphers
    if 'tls_version' in df.columns:
        print("\nTLS Versions Distribution:")
        print(df['tls_version'].value_counts())
    
    if 'tls_cipher' in df.columns:
        print("\nTop TLS Ciphers Used:")
        print(df['tls_cipher'].value_counts().head(5))

    # 4. QUIC Metadata
    if 'quic_dcid' in df.columns:
        print("\nTop QUIC Destination Connection IDs (DCIDs):")
        print(df['quic_dcid'].value_counts().head(10))
    
    if 'quic_version' in df.columns:
        print("\nQUIC Versions Distribution:")
        print(df['quic_version'].value_counts())

    # 5. Correlation: Find IPs associated with Blizzard domains
    if 'dns_query' in df.columns and 'tls_sni' in df.columns:
        blizz_domains = df[
            (df['dns_query'].str.contains('blizzard|battle.net', case=False, na=False)) |
            (df['tls_sni'].str.contains('blizzard|battle.net', case=False, na=False))
        ]
        
        if not blizz_domains.empty:
            print("\nIPs associated with Blizzard/Battle.net domains:")
            # For DNS, the response would have the IP, but we only extracted the query name.
            # However, TLS SNI tells us exactly which IP we are talking to for that domain.
            sni_ips = blizz_domains[blizz_domains['tls_sni'].notna()][['dst_ip', 'tls_sni']].drop_duplicates()
            print(sni_ips)

if __name__ == "__main__":
    analyze_enriched_traffic('ow-network-traffic-enriched.parquet')
