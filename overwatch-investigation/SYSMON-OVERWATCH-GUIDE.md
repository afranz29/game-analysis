# Sysmon Configuration Guide for Overwatch Monitoring

## Overview
This custom Sysmon configuration is designed to capture detailed telemetry from Overwatch game processes, Battle.net launcher, and related Blizzard services.

## What This Configuration Monitors

### 1. **Process Creation (Event ID 1)**
- All Overwatch.exe launches
- Battle.net launcher processes
- Blizzard Agent.exe
- Any child processes spawned by these applications
- Command-line arguments (useful for detecting launch parameters)

### 2. **Network Connections (Event ID 3)**
- **Most Important for your network analysis!**
- All network connections made by Overwatch
- Connections to Blizzard game servers
- Source/destination IPs and ports
- Protocols used
- Timestamps for connection analysis

### 3. **File Operations (Event ID 11)**
- Files created/modified by Overwatch
- Game asset downloads
- Configuration file changes
- Screenshot captures
- Replay file creation

### 4. **DNS Queries (Event ID 22)**
- **Critical for your traffic correlation!**
- Domain lookups by Overwatch
- Battle.net service queries
- Blizzard CDN requests
- Helps map IPs to hostnames

### 5. **Process Termination (Event ID 5)**
- When Overwatch closes
- Crash detection
- Session duration calculation

### 6. **Registry Modifications (Event ID 12/13/14)**
- Game settings changes
- Installation tracking
- Configuration updates

### 7. **Security-Relevant Events**
- **Remote Thread Creation (Event ID 8)**: Detects cheat injections
- **Process Access (Event ID 10)**: Monitors memory access (anti-cheat triggers)
- **Process Tampering (Event ID 25)**: Detects process modification attempts
- **Driver Loading (Event ID 6)**: Anti-cheat driver activity

## Installation Steps

### 1. Backup Current Configuration
```bash
# Export current Sysmon config
sysmon.exe -c > current-config-backup.xml
```

### 2. Apply Overwatch Monitoring Configuration
```bash
# Apply the new configuration
sysmon.exe -c sysmon-overwatch-monitoring.xml
```

### 3. Verify Configuration
```bash
# Check Sysmon is running
Get-Service Sysmon64

# View recent events
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 10
```

## Collecting Data for Your Network Analysis

### Method 1: Export Sysmon Logs During Gameplay
```powershell
# Start a gaming session
# Play Overwatch for your desired duration
# Export logs after session ends

Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 10000 | 
    Export-Csv -Path "D:\WindowsInvestigations\sysmon-overwatch-session.csv" -NoTypeInformation
```

### Method 2: Filter Network Events Only
```powershell
# Export only network connection events (Event ID 3)
Get-WinEvent -FilterHashtable @{
    LogName='Microsoft-Windows-Sysmon/Operational'
    ID=3
} | Where-Object {$_.Message -like "*Overwatch*"} | 
    Export-Csv -Path "D:\WindowsInvestigations\overwatch-network-events.csv" -NoTypeInformation
```

### Method 3: Real-time Monitoring
```powershell
# Watch network events in real-time
Get-WinEvent -FilterHashtable @{
    LogName='Microsoft-Windows-Sysmon/Operational'
    ID=3
} -MaxEvents 1 | Format-List *
```

## Correlating with Your PCAP Data

Your existing analysis files:
- `ow-network-traffic.pcapng` - Raw packet capture
- `ow-network-traffic.parquet` - Parsed packet data
- `correlate_traffic.py` - Correlation script

### Enhanced Correlation Workflow

1. **Capture simultaneously:**
   ```bash
   # Terminal 1: Start packet capture
   tshark -i <interface> -w ow-live-capture.pcapng
   
   # Terminal 2: Monitor Sysmon
   # (Sysmon runs automatically)
   
   # Terminal 3: Launch Overwatch
   ```

2. **Export Sysmon data:**
   ```powershell
   # After gaming session
   Get-WinEvent -FilterHashtable @{
       LogName='Microsoft-Windows-Sysmon/Operational'
       ID=3
       StartTime=(Get-Date).AddHours(-2)
   } | Export-Csv sysmon-session.csv
   ```

3. **Correlate data:**
   - Sysmon provides: Process names, PIDs, local ports
   - PCAP provides: Full packet data, protocols, sequences
   - Match on: Timestamp, local port, destination IP

## Key Benefits for Your Analysis

### 1. **Process Attribution**
- Know which exact process made each connection
- Distinguish Overwatch.exe from Battle.net launcher
- Track child processes (anti-cheat, crash reporter)

### 2. **Session Tracking**
- Process start/stop times
- Calculate session duration
- Correlate crashes with network events

### 3. **Security Analysis**
- Detect suspicious injections (cheats)
- Monitor anti-cheat behavior
- Track unusual file access patterns

### 4. **Network Pattern Analysis**
- Map high-level game events to network traffic
- Understand connection lifecycle
- Identify server pools and CDN usage

## Useful Sysmon Event IDs for Gaming Analysis

| Event ID | Event Type | Why It Matters |
|----------|------------|----------------|
| **3** | NetworkConnect | **Most important** - All network connections |
| **22** | DnsQuery | Resolve server hostnames, CDN mappings |
| 1 | ProcessCreate | Game launches, session starts |
| 5 | ProcessTerminate | Game exits, crashes |
| 11 | FileCreate | Screenshots, replays, downloads |
| 8 | CreateRemoteThread | Cheat detection, DLL injection |
| 10 | ProcessAccess | Memory access (anti-cheat triggers) |

## Reducing Noise (Optional)

If you get too many events, add these exclusions:

```xml
<!-- Exclude cache file operations -->
<FileCreate onmatch="exclude">
    <TargetFilename condition="contains">\Overwatch\Cache\</TargetFilename>
    <TargetFilename condition="contains">\Overwatch\Logs\</TargetFilename>
</FileCreate>

<!-- Exclude localhost connections -->
<NetworkConnect onmatch="exclude">
    <DestinationIp condition="is">127.0.0.1</DestinationIp>
</NetworkConnect>
```

## Integration with Your Python Analysis

Update your `correlate_traffic.py` to include Sysmon data:

```python
import pandas as pd
from datetime import datetime

# Load Sysmon network events
sysmon_df = pd.read_csv('sysmon-session.csv')

# Load PCAP data (your existing code)
pcap_df = pd.read_parquet('ow-network-traffic.parquet')

# Correlate on timestamp + local port
merged_df = pd.merge_asof(
    pcap_df.sort_values('timestamp'),
    sysmon_df[['timestamp', 'source_port', 'process_name', 'pid']],
    left_on='timestamp',
    right_on='timestamp',
    by='source_port',
    direction='nearest',
    tolerance=pd.Timedelta('5s')
)

# Now you have process attribution for each packet!
```

## Monitoring Performance Impact

Sysmon is lightweight but monitor system impact:

```powershell
# Check Sysmon CPU/Memory usage
Get-Process Sysmon64 | Select-Object CPU, WorkingSet
```

## Troubleshooting

### Configuration Not Loading
```bash
# Check for XML syntax errors
sysmon.exe -c sysmon-overwatch-monitoring.xml
# Look for error messages
```

### No Events Being Generated
```powershell
# Verify Sysmon service is running
Get-Service Sysmon64

# Check event log for errors
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 5
```

### Too Many Events
- Add more specific exclusions
- Focus only on Event ID 3 (Network) and 22 (DNS)
- Increase log size in Event Viewer

## Next Steps

1. **Apply this configuration** before your next Overwatch session
2. **Capture simultaneously**: Sysmon + packet capture
3. **Export and correlate** the data using timestamps and ports
4. **Analyze patterns** with full process attribution

This will give you much richer data than packet capture alone!
