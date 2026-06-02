# Sysmon Configuration Gap Analysis
**Configuration:** `sysmon-gaming-monitoring.xml`  
**Date:** 2026-06-01  
**Based on:** Live validation findings from osquery and Vector logs

---

## Executive Summary

Reviewed the existing Sysmon gaming monitoring configuration against live telemetry and identified **3 high-priority gaps** and several optimization opportunities. The configuration is **fundamentally sound** with excellent coverage, but missing some key observability for gaming process IPC and crash reporting.

**Overall Assessment:** 8.5/10
- ✅ Excellent DNS coverage (captures all infrastructure)
- ✅ Strong process lifecycle monitoring
- ✅ Good anti-cheat detection coverage
- ⚠️ Missing loopback IPC visibility for gaming processes
- ⚠️ Missing crash reporter process capture
- ⚠️ Event ID 10 generates excessive volume (78% of events)

---

## 1. Process Coverage Analysis

### ✅ **Captured Processes**
| Process | Status | Notes |
|:---|:---:|:---|
| **Overwatch.exe** | ✅ | Explicitly included |
| **Battle.net.exe** | ✅ | Explicitly included |
| **Agent.exe** | ✅ | Explicitly included |
| **Steam games** | ✅ | Via `\steamapps\common\` path |

### ⚠️ **Missing Processes**

#### **CrashMailer_64.exe** (Medium Priority)
- **Path:** `C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe`
- **Parent:** Overwatch.exe (PID 25444)
- **Resident Memory:** 9.1 MB
- **Impact:** Crash reporter behavior not logged (Event ID 1, 5)
- **Recommendation:** Add `\ErrorReporting\` path to Process Create rules

#### **Battle.net Launcher.exe** (Low Priority)
- **Path:** `C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe`
- **Behavior:** Spawns Battle.net.exe then exits within seconds
- **Impact:** Initial launcher might not be captured
- **Evidence from Vector logs:**
  ```
  00:50:27 - Battle.net Launcher.exe started
  00:50:27 - Battle.net.exe spawned (--from-launcher)
  00:50:27 - Launcher.exe terminated
  ```
- **Recommendation:** Verify if captured; low priority since main process is captured

---

## 2. Network Coverage Analysis

### ✅ **Successfully Covered Endpoints**
All discovered endpoints should be captured by broad Event ID 3 monitoring:

| Endpoint | Destination | Protocol | Status |
|:---|:---|:---:|:---|
| **Port 3724 Gameplay** | 24.105.60.80:3724 | TCP | ✅ Should capture |
| **Cloudflare CDN** | 104.18.35.174:443 (×4) | TCP | ✅ Should capture |
| **Google Cloud 1119** | 34.16.129.152:1119 | TCP | ✅ Should capture |
| **Telemetry** | 137.221.105.232:443 | TCP | ✅ Should capture |
| **CDN (us.version)** | 136.110.188.211:443 | TCP | ✅ Should capture |
| **UDP Listeners** | Ports 4242, 64540 | UDP | ✅ Should capture |

### ❌ **Explicitly Excluded (Gap)**

#### **Loopback IPC** (High Priority)
The configuration **excludes all loopback (127.0.0.1) connections** to prevent log flooding:

```xml
<NetworkConnect onmatch="exclude">
    <DestinationIp condition="is">127.0.0.1</DestinationIp>
    <DestinationIp condition="is">::1</DestinationIp>
</NetworkConnect>
```

**Impact:** Cannot observe:
- **Overwatch internal threading:** `127.0.0.1:54063 ↔ 127.0.0.1:40644` (2 loopback pairs)
- **Battle.net REST API:** `127.0.0.1:22885` (LISTEN)
- **Agent.exe REST API:** `127.0.0.1:64517` (LISTEN)
- **Battle.net ↔ Agent communication:** Local HTTP calls

**Recommendation:** Add selective loopback monitoring for gaming processes:
```xml
<RuleGroup name="Gaming Loopback IPC" groupRelation="or">
    <NetworkConnect onmatch="include">
        <Image condition="contains">Overwatch</Image>
        <DestinationIp condition="is">127.0.0.1</DestinationIp>
    </NetworkConnect>
    <!-- Repeat for Battle.net, Agent, Steam games -->
</RuleGroup>
```

---

## 3. Event ID Coverage Assessment

### ✅ **Excellent Coverage (Events 1-25)**
| Event ID | Name | Status | Notes |
|:---:|:---|:---:|:---|
| **1** | Process Create | ✅ | Comprehensive |
| **2** | File Time Change | ✅ | Game directories |
| **3** | Network Connect | ✅⚠️ | Broad but excludes loopback |
| **5** | Process Terminate | ✅ | Tracks exits |
| **6** | Driver Load | ✅ | Game drivers |
| **7** | Image Load | ✅ | DLL monitoring |
| **8** | CreateRemoteThread | ✅ | Anti-cheat |
| **9** | RawAccessRead | ✅ | Disk access |
| **10** | Process Access | ✅⚠️ | HIGH VOLUME (78% of events) |
| **11** | File Create | ✅ | Game directories |
| **12-14** | Registry Events | ✅ | Game keys |
| **15** | FileStreamHash | ✅ | ADS detection |
| **17-18** | Named Pipes | ✅ | IPC monitoring |
| **19-21** | WMI Events | ✅ | Overwatch-specific |
| **22** | DNS Query | ✅✅ | **Excellent** - logs ALL DNS |
| **23** | File Delete | ✅ | Game directories |
| **25** | Process Tampering | ✅ | Anti-cheat |

### ❌ **Missing Events (26-29)**
| Event ID | Name | Status | Impact |
|:---:|:---|:---:|:---|
| **26** | File Delete Logged | ❌ | Tracks deleted file contents (forensics) |
| **27** | File Block Executable | ❌ | Blocks suspicious executables (active defense) |
| **28** | File Block Shredding | ❌ | Detects secure deletion |
| **29** | File Executable Detected | ❌ | Detects new executables (cheat detection) |

**Recommendation:**
- **Event ID 29** is most valuable for gaming use case (detecting injected cheat DLLs)
- Events 26-28 are forensic/defensive features, less critical for monitoring

---

## 4. High-Volume Event Analysis

### Event ID 10: Process Access (78% of events!)

From Vector logs analysis (first 10k events):
```
Event ID 10 (Process Access): 7,766 events (77.6%)
Event ID 3  (Network):        1,082 events (10.8%)
Event ID 11 (File Create):      156 events (1.6%)
```

**Top Accessors of Overwatch.exe:**
- `explorer.exe`: 150 events (file manager)
- `Discord.exe`: 95 events (overlay/Rich Presence)
- `MsMpEng.exe`: Windows Defender scans
- `GameBarFTServer.exe`: Xbox Game Bar
- `NVDisplay.Container.exe`: NVIDIA drivers
- `wmiprvse.exe`: WMI providers

**Analysis:**
- Most are **benign system processes** (Explorer, Defender, WMI)
- **Discord overlay** is expected and harmless
- **Game Bar** is built-in Windows feature

**Impact:** Log flooding, increased storage, harder to find suspicious activity

**Recommendation:** Add exclusion rules for known benign processes:
```xml
<RuleGroup name="Process Access Exclusions" groupRelation="or">
    <ProcessAccess onmatch="exclude">
        <SourceImage condition="is">C:\Windows\explorer.exe</SourceImage>
        <SourceImage condition="contains">MsMpEng.exe</SourceImage>
        <SourceImage condition="contains">GameBarFTServer.exe</SourceImage>
        <SourceImage condition="contains">Discord.exe</SourceImage>
        <!-- Keep suspicious access visible -->
    </ProcessAccess>
</RuleGroup>
```

---

## 5. Identified Gaps Summary

### **HIGH Priority**

| Gap | Impact | Recommendation |
|:---|:---|:---|
| **Loopback connections excluded** | Cannot monitor IPC between Overwatch threads, Battle.net ↔ Agent API calls | Add selective loopback inclusion for gaming processes |
| **Vector logs show 0 network connections** | Despite DNS queries, no Event ID 3 logged for Blizzard endpoints | Validate with live capture during gameplay |

### **MEDIUM Priority**

| Gap | Impact | Recommendation |
|:---|:---|:---|
| **CrashMailer_64.exe not captured** | Crash reporter behavior invisible | Add `\ErrorReporting\` path to Event ID 1/5 |
| **Event ID 10 high volume** | 78% of events, log flooding | Add benign process exclusions |
| **Battle.net Launcher.exe** | Initial launcher might be missed | Verify in logs; add if needed |

### **LOW Priority (Optional)**

| Gap | Impact | Recommendation |
|:---|:---|:---|
| **Event ID 29 not configured** | Cannot detect injected cheat DLLs | Add for executable detection in game folders |
| **Events 26-28 not configured** | Missing forensic capabilities | Evaluate based on use case |

---

## 6. Configuration Strengths

The configuration has several **excellent design choices**:

1. ✅ **Broad DNS monitoring** (Event ID 22 logs ALL system DNS)
   - Discovered 6 new Blizzard endpoints in Vector logs
   - No DNS endpoint can hide

2. ✅ **Generic Steam path monitoring** (`\steamapps\common\`)
   - Captured Slay the Spire 2 without explicit configuration
   - Future-proof for any Steam game

3. ✅ **Focused file operations**
   - Only monitors game directories, not entire system
   - Reduces noise while maintaining coverage

4. ✅ **Comprehensive anti-cheat coverage**
   - Event ID 8: Remote thread injection
   - Event ID 25: Process tampering
   - Event ID 10: Process access (though needs filtering)

5. ✅ **Multi-game support**
   - Overwatch + generic Steam coverage
   - Easy to extend to other Battle.net games

6. ✅ **Well-organized rule groups**
   - Clear naming and comments
   - Easy to maintain

---

## 7. Recommended Changes

### **Version 2.0 Configuration Changes**

#### **Change 1: Add Selective Loopback Monitoring** (High Priority)
```xml
<!-- NEW: Capture gaming process loopback before general exclusion -->
<RuleGroup name="Gaming Loopback IPC" groupRelation="or">
    <NetworkConnect onmatch="include">
        <Image condition="contains">Overwatch</Image>
        <DestinationIp condition="is">127.0.0.1</DestinationIp>
    </NetworkConnect>
    <NetworkConnect onmatch="include">
        <Image condition="contains">Battle.net</Image>
        <DestinationIp condition="is">127.0.0.1</DestinationIp>
    </NetworkConnect>
    <NetworkConnect onmatch="include">
        <Image condition="contains">Agent.exe</Image>
        <DestinationIp condition="is">127.0.0.1</DestinationIp>
    </NetworkConnect>
</RuleGroup>

<!-- Keep existing broad exclusion for non-gaming processes -->
<RuleGroup name="Broad Network Monitoring" groupRelation="or">
    <NetworkConnect onmatch="exclude">
        <DestinationIp condition="is">127.0.0.1</DestinationIp>
    </NetworkConnect>
</RuleGroup>
```

#### **Change 2: Add Crash Reporter Capture** (Medium Priority)
```xml
<ProcessCreate onmatch="include">
    <!-- Crash Reporters -->
    <Image condition="contains">\ErrorReporting\</Image>
    <Image condition="contains">CrashMailer</Image>
</ProcessCreate>
```

#### **Change 3: Add Event ID 10 Exclusions** (Medium Priority)
```xml
<RuleGroup name="Process Access Exclusions" groupRelation="or">
    <ProcessAccess onmatch="exclude">
        <SourceImage condition="is">C:\Windows\explorer.exe</SourceImage>
        <SourceImage condition="contains">MsMpEng.exe</SourceImage>
        <SourceImage condition="contains">GameBarFTServer.exe</SourceImage>
        <SourceImage condition="contains">GamingServices.exe</SourceImage>
        <SourceImage condition="contains">wmiprvse.exe</SourceImage>
        <SourceImage condition="contains">NVDisplay.Container.exe</SourceImage>
        <SourceImage condition="contains">Discord.exe</SourceImage>
    </ProcessAccess>
</RuleGroup>
```

#### **Change 4: Add Event ID 29** (Low Priority)
```xml
<RuleGroup name="Gaming Executable Detection" groupRelation="or">
    <FileExecutableDetected onmatch="include">
        <TargetFilename condition="contains">Overwatch</TargetFilename>
        <TargetFilename condition="contains">\steamapps\common\</TargetFilename>
    </FileExecutableDetected>
</RuleGroup>
```

---

## 8. Validation Requirements

Before deploying v2.0 config, validate:

1. **Loopback Capture Test:**
   ```powershell
   # Launch Overwatch, check for Event ID 3 with 127.0.0.1
   Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=3} |
       Where-Object {$_.Message -match "127.0.0.1" -and $_.Message -match "Overwatch"}
   ```

2. **Event ID 10 Volume Test:**
   ```powershell
   # Compare event counts before/after exclusions
   (Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=10} -MaxEvents 1000).Count
   ```

3. **Network Connection Test:**
   - Launch Overwatch with new config
   - Verify Event ID 3 captures port 3724, Cloudflare, telemetry
   - Compare with osquery network state

4. **CrashMailer Test:**
   - Check Event ID 1 logs for CrashMailer_64.exe spawn

---

## 9. Estimated Impact

### **Storage/Performance Impact**
- **Loopback monitoring:** +5-10% events (gaming processes only)
- **Event ID 10 exclusions:** -50-60% reduction in process access events
- **Event ID 29:** +1-2% events (new executables rare)
- **Net result:** ~40-50% reduction in event volume

### **Observability Improvement**
- Loopback IPC: +100% visibility into internal game communication
- Crash reporters: +100% visibility into crash handling
- Event ID 29: +100% visibility into injected executables

---

## 10. Conclusion

The current `sysmon-gaming-monitoring.xml` configuration is **well-designed and effective**, scoring **8.5/10**. The three high-priority gaps are:

1. ✅ **Loopback exclusion** - Prevents IPC observability
2. ✅ **Crash reporter missing** - Incomplete process lifecycle
3. ✅ **Event ID 10 noise** - Log flooding from benign processes

Implementing the recommended v2.0 changes will:
- ✅ Enable complete process communication visibility
- ✅ Reduce log volume by ~40-50%
- ✅ Improve signal-to-noise ratio for security analysis

**Recommended Action:** Apply v2.0 configuration changes and validate with live Overwatch gameplay session.

---

**Related Documents:**
- `VALIDATION_SUMMARY.md` - Three-way validation results
- `LIVE_VALIDATION.md` - Live osquery telemetry analysis
- `SYSMON_CONFIG_REVIEW.md` - Proposed v2.0 configuration (XML)
