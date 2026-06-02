"""
Sysmon Configuration Gap Analysis
Compares sysmon-gaming-monitoring.xml against live validation findings
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("SYSMON CONFIGURATION GAP ANALYSIS")
print("=" * 70)

# Processes discovered in live validation
discovered_processes = {
    "Overwatch.exe": {
        "path": r"C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe",
        "in_config": True,
        "notes": "Explicitly included"
    },
    "CrashMailer_64.exe": {
        "path": r"C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe",
        "in_config": False,
        "notes": "Child of Overwatch, NOT explicitly captured"
    },
    "Battle.net.exe": {
        "path": r"C:\Program Files (x86)\Battle.net\Battle.net.exe",
        "in_config": True,
        "notes": "Explicitly included"
    },
    "Battle.net Launcher.exe": {
        "path": r"C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe",
        "in_config": False,
        "notes": "Spawns Battle.net.exe, then exits - might not be captured"
    },
    "Agent.exe": {
        "path": r"C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe",
        "in_config": True,
        "notes": "Explicitly included"
    }
}

print("\n1. PROCESS COVERAGE ANALYSIS")
print("-" * 70)
for proc, info in discovered_processes.items():
    status = "✅" if info["in_config"] else "⚠️"
    print(f"{status} {proc}")
    print(f"   Path: {info['path']}")
    print(f"   Notes: {info['notes']}\n")

# Network endpoints discovered
network_findings = {
    "Port 3724 (Gameplay)": {
        "destination": "24.105.60.80:3724",
        "captured": "Should be captured (broad Event ID 3)",
        "protocol": "TCP"
    },
    "Cloudflare CDN": {
        "destination": "104.18.35.174:443 (×4)",
        "captured": "Should be captured (broad Event ID 3)",
        "protocol": "TCP/HTTPS"
    },
    "Google Cloud Port 1119": {
        "destination": "34.16.129.152:1119, 34.125.112.208:1119",
        "captured": "Should be captured (broad Event ID 3)",
        "protocol": "TCP"
    },
    "Telemetry (Blizzard)": {
        "destination": "137.221.105.232:443",
        "captured": "Should be captured (broad Event ID 3)",
        "protocol": "TCP/HTTPS"
    },
    "CDN (us.version)": {
        "destination": "136.110.188.211:443",
        "captured": "Should be captured (broad Event ID 3)",
        "protocol": "TCP/HTTPS"
    },
    "UDP Listeners": {
        "destination": "Local ports 4242, 64540",
        "captured": "Should be captured (broad Event ID 3)",
        "protocol": "UDP"
    },
    "Loopback IPC": {
        "destination": "127.0.0.1:* (multiple)",
        "captured": "❌ EXPLICITLY EXCLUDED by config",
        "protocol": "TCP"
    },
    "Local REST APIs": {
        "destination": "127.0.0.1:22885 (Battle.net), :64517 (Agent)",
        "captured": "❌ EXPLICITLY EXCLUDED by config",
        "protocol": "TCP (LISTEN)"
    }
}

print("\n2. NETWORK COVERAGE ANALYSIS")
print("-" * 70)
for name, info in network_findings.items():
    if "EXCLUDED" in info["captured"]:
        status = "❌"
    else:
        status = "✅"
    print(f"{status} {name}")
    print(f"   Destination: {info['destination']}")
    print(f"   Protocol: {info['protocol']}")
    print(f"   Status: {info['captured']}\n")

# Event ID coverage check
event_coverage = {
    "1": {
        "name": "Process Create",
        "status": "✅",
        "notes": "Captures Overwatch, Battle.net, Agent, Steam games"
    },
    "2": {
        "name": "File Creation Time",
        "status": "✅",
        "notes": "Monitors Overwatch and Steam directories"
    },
    "3": {
        "name": "Network Connection",
        "status": "✅⚠️",
        "notes": "Broad monitoring BUT excludes loopback (see gap analysis)"
    },
    "5": {
        "name": "Process Terminate",
        "status": "✅",
        "notes": "Tracks game exits"
    },
    "6": {
        "name": "Driver Load",
        "status": "✅",
        "notes": "Monitors game drivers"
    },
    "7": {
        "name": "Image Load (DLL)",
        "status": "✅",
        "notes": "Tracks DLL loading"
    },
    "8": {
        "name": "CreateRemoteThread",
        "status": "✅",
        "notes": "Anti-cheat detection"
    },
    "9": {
        "name": "Raw Disk Access",
        "status": "✅",
        "notes": "Monitors suspicious disk access"
    },
    "10": {
        "name": "Process Access",
        "status": "✅⚠️",
        "notes": "HIGH VOLUME - 78% of events. Includes generic Steam path."
    },
    "11": {
        "name": "File Create",
        "status": "✅",
        "notes": "Focused on game directories"
    },
    "12-14": {
        "name": "Registry Events",
        "status": "✅",
        "notes": "Monitors game registry keys"
    },
    "15": {
        "name": "Alternate Data Stream",
        "status": "✅",
        "notes": "Monitors ADS in game folders"
    },
    "17-18": {
        "name": "Named Pipes",
        "status": "✅",
        "notes": "IPC monitoring"
    },
    "19-21": {
        "name": "WMI Events",
        "status": "✅",
        "notes": "Overwatch-specific only"
    },
    "22": {
        "name": "DNS Query",
        "status": "✅✅",
        "notes": "BROAD - logs ALL system DNS (excellent coverage)"
    },
    "23": {
        "name": "File Delete",
        "status": "✅",
        "notes": "Monitors deletions in game folders"
    },
    "25": {
        "name": "Process Tampering",
        "status": "✅",
        "notes": "Anti-cheat detection"
    },
    "26": {
        "name": "File Delete Logged",
        "status": "❌",
        "notes": "NOT CONFIGURED - tracks deleted file contents"
    },
    "27": {
        "name": "File Block Executable",
        "status": "❌",
        "notes": "NOT CONFIGURED - blocks suspicious executables"
    },
    "28": {
        "name": "File Block Shredding",
        "status": "❌",
        "notes": "NOT CONFIGURED - detects secure deletion"
    },
    "29": {
        "name": "File Executable Detected",
        "status": "❌",
        "notes": "NOT CONFIGURED - detects new executables"
    }
}

print("\n3. SYSMON EVENT ID COVERAGE")
print("-" * 70)
for event_id, info in event_coverage.items():
    print(f"Event ID {event_id}: {info['name']}")
    print(f"  {info['status']} {info['notes']}\n")

print("\n4. IDENTIFIED GAPS")
print("-" * 70)

gaps = [
    {
        "severity": "HIGH",
        "issue": "Loopback connections excluded",
        "impact": "Cannot monitor local IPC between game processes (Overwatch internal threads, Battle.net ↔ Agent REST API)",
        "recommendation": "Consider selective inclusion of loopback for gaming processes only"
    },
    {
        "severity": "MEDIUM",
        "issue": "CrashMailer_64.exe not explicitly captured",
        "impact": "Crash reporter might not be logged in Event ID 1/5",
        "recommendation": "Add ErrorReporting path or crash handler processes"
    },
    {
        "severity": "MEDIUM",
        "issue": "Battle.net Launcher.exe might be missed",
        "impact": "Initial launcher process might not be captured (exits quickly)",
        "recommendation": "Verify if launcher spawning is logged"
    },
    {
        "severity": "LOW",
        "issue": "Event ID 10 (Process Access) high volume",
        "impact": "78% of sampled events - potential log flooding",
        "recommendation": "Consider filtering to reduce noise while maintaining security coverage"
    },
    {
        "severity": "INFO",
        "issue": "Events 26-29 not configured",
        "impact": "Missing advanced file monitoring (executable detection, secure deletion)",
        "recommendation": "Evaluate if needed for cheat detection use case"
    },
    {
        "severity": "INFO",
        "issue": "No capture of parent-to-child handoff details",
        "impact": "Battle.net Launcher → Battle.net.exe handoff details might be incomplete",
        "recommendation": "Document expected process lifecycle for validation"
    }
]

for gap in gaps:
    print(f"[{gap['severity']}] {gap['issue']}")
    print(f"  Impact: {gap['impact']}")
    print(f"  Recommendation: {gap['recommendation']}\n")

print("\n5. CONFIGURATION STRENGTHS")
print("-" * 70)

strengths = [
    "✅ Broad DNS monitoring (Event ID 22) captures all infrastructure",
    "✅ Generic Steam path (\\steamapps\\common\\) captures any Steam game",
    "✅ Focused file operations reduce noise (game directories only)",
    "✅ Comprehensive process lifecycle (create, access, terminate)",
    "✅ Anti-cheat coverage (remote threads, process tampering, process access)",
    "✅ Multi-game support (Overwatch + generic Steam)",
    "✅ Well-organized rule groups with clear naming"
]

for strength in strengths:
    print(strength)

print("\n" + "=" * 70)
print("RECOMMENDATION SUMMARY")
print("=" * 70)
print("""
PRIORITY 1 (High Impact):
  - Decide on loopback monitoring strategy (include for gaming processes?)
  - Add CrashMailer and error reporting processes

PRIORITY 2 (Medium Impact):
  - Verify Battle.net Launcher.exe capture in logs
  - Consider Event ID 10 filtering to reduce volume

PRIORITY 3 (Low Impact):
  - Evaluate Events 26-29 for advanced file monitoring
  - Document expected process lifecycles for validation
""")
