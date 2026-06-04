# Watching Over Overwatch: Windows Security & Overwatch Gameplay Analysis Workspace

Welcome to the central intelligence hub for the **Windows Security Auditing & Overwatch Gameplay Monitoring** investigation. 

This repository serves as a structured laboratory environment containing configurations, raw/processed packet captures, host logs, analytical tools, and comprehensive reports validating host-level and network-level security telemetry for the Battle.net launcher, the Overwatch game client (`Overwatch.exe`), and their multi-cloud helper services.


![Overwatch Gameplay Analysis](overwatch.png)
---


## 🗺️ Repository Architecture & Directory Tree

The workspace has been organized into modular components. The diagram below illustrates the relationship and classification of these directories:

```text
D:\WindowsInvestigations (Workspace Root)
│
├── configs/ ───────────────────[ Defines Monitoring Policies ]
│   └── Sysmon Rules & Vector Pipelines
│
├── overwatch-investigation/ ───[ Primary Data & Analysis ]
│   └── PCAPNG Captures, PDML Tables, Validation Summaries
│
├── scripts/ ───────────────────[ Automates Audits & Parsing ]
│   └── Python Processing, Extraction, and Correlation Utilities
│
├── system-stuff/ ──────────────[ System Environment Baseline ]
│   └── Host patch history (KBs) and installed software
│
└── agentsview/ ────────────────[ AI Research Chronicles ]
    └── Multi-agent transcripts, prompt logs, token reports
```

---

## 🗂️ Component Directory Guide

### 1. ⚙️ [configs/](configs/)
Contains the security policy baselines defining what data is monitored on the host:
- [sysmon-gaming-monitoring.xml](configs/sysmon-gaming-monitoring.xml): Sysmon ruleset optimized for gaming environments, including path-generic filters.
- [sysmon-overwatch-monitoring.xml](configs/sysmon-overwatch-monitoring.xml): Sysmon configuration tuned specifically to capture Overwatch and Battle.net lifecycle elements.
- [sysmon-steam-monitoring.xml](configs/sysmon-steam-monitoring.xml): Custom rules targeting Steam launcher sub-processes.
- [vector1.toml](configs/vector1.toml): Configuration defining the Vector log-forwarding agent pipeline.

### 2. 🎮 [overwatch-investigation/](overwatch-investigation/)
The core data repository containing packet captures, Sysmon event logs, database structures, and analytical summaries:
- **Telemetry Reports & Summaries:**
  - [VALIDATION_SUMMARY.md](overwatch-investigation/VALIDATION_SUMMARY.md): Synthesis validating documented claims against active captures.
  - [VECTOR_ANALYSIS_CORRECTED.md](overwatch-investigation/VECTOR_ANALYSIS_CORRECTED.md): Critical analysis correcting the initial data sampling error.
  - [LIVE_VALIDATION.md](overwatch-investigation/LIVE_VALIDATION.md): Telemetry data captured in real-time during active, live gameplay.
  - [OW_VALIDATION_CHRONO.md](overwatch-investigation/OW_VALIDATION_CHRONO.md): Walkthrough charting the chronology of the system validation.
  - [DIAGRAMS.md](overwatch-investigation/DIAGRAMS.md): Mermaid architecture diagrams mapping process and network infrastructures.
- **Datasets & Raw Captures:**
  - `ow-network-traffic.pcapng` (25 MB) & `ow-live-sample.pcapng` (1.7 MB): Raw Wireshark packet captures.
  - `ow-network-traffic.pdml` (1.62 GB XML): Extended Wireshark packet detail markup export.
  - `ow-network-traffic-enriched.parquet` (566 KB) & `ow-network-traffic.parquet` (551 KB): Compact, high-speed database formats parsed from raw XML.
  - `sysmon-overwatch-session.csv` (2.2 MB): Historical Sysmon events representing the gameplay capture window.

### 3. 🐍 [scripts/](scripts/)
A library of 16 custom Python utilities designed to process high-volume XML logs, aggregate statistics, and correlate process activity.
> [!TIP]
> For a detailed, interactive map and catalog of all python utilities, please review the workspace script index: **[SCRIPTS.md](SCRIPTS.md)**.

### 4. 💻 [system-stuff/](system-stuff/)
Documents defining the environmental baseline of the test host:
- [PATCH_HISTORY.md](system-stuff/PATCH_HISTORY.md): Hotfix patches (KB packages) installed on the Windows system.
- [SOFTWARE.md](system-stuff/SOFTWARE.md): Installed applications, drivers, and runtime libraries forming the testing baseline.

### 5. 🧠 [agentsview/](agentsview/)
AI agent research logs, multi-agent session records, prompt histories, and resource consumption analysis:
- [FINAL_REPORT.md](agentsview/FINAL_REPORT.md) & [INVESTIGATION_SUMMARY.md](agentsview/INVESTIGATION_SUMMARY.md): Final investigative conclusions.
- [ALL_USER_PROMPTS.md](agentsview/ALL_USER_PROMPTS.md): Extracts of genuine instructions sent to AI models during the multi-day analysis.
- [TOKEN_AND_TOOL_USAGE.md](agentsview/TOKEN_AND_TOOL_USAGE.md): Aggregated token consumption and tool call statistics.

---

## 🔍 Core Findings & Telemetry Validation

The synthesis of historical logs and live `osquery` monitoring confirmed **100% of the core Overwatch infrastructure properties**:

### 1. Active Gameplay Telemetry
- **Memory Footprint:** The combined memory footprint under active gameplay measures **~8.88 GB** (including `Overwatch.exe` taking 8.18 GB and the supporting `Battle.net` launcher processes consuming ~0.7 GB).
- **Socket Connectivity:** Real-time gameplay runs over active TCP/UDP sockets mapped to direct Blizzard servers on `24.105.60.80:3724`.
- **Process Architecture:** Confirmed that `Battle.net.exe` launches `Overwatch.exe` (Parent PID link verified), which subsequently spawns the telemetry crash reporter `CrashMailer_64.exe`.

### 2. Multi-Cloud Infrastructure Discovered
- **Cloudflare CDN Integration:** Isolated `Overwatch.exe` establishing 4 simultaneous connections to `104.18.35.174` (port 443) to stream live assets and enforce DDoS protections.
- **Google Cloud Services (Port 1119):** Identified `Overwatch.exe` and `Battle.net.exe` communicating with GCP endpoints (e.g., `34.16.129.152` and `34.125.112.208` on port 1119) to coordinate session handshakes and matchmaking queues.

### 3. Log-Sampling Flaw & Correction
During historical log validation, a critical sampling flaw was discovered in the initial analytical script (`analyze_vector_logs.py`), which truncated parsing after the first **10,000 events**. Because the active gameplay took place later in the capture timeline, this caused the initial reports to conclude that "Vector logs contain zero Blizzard connections and show no active gameplay."

When the files were parsed in full, the logs successfully validated host-level monitoring:
- **`Overwatch.exe` activity:** **495 events** logged.
- **Sysmon Event ID 3 (Network Connections):** Fully operational, logging **301 Blizzard-related connections** (including immediate post-match telemetry uploads to the match ingestion endpoint `overwatch.ingest.gdp.blizzard.com` at `35.201.91.89:443`).
- **Additional Metadata:** Discovered game settings saving directly to cloud-synced folders (`OneDrive\Documents\Overwatch\Settings\Settings_v0.ini`) and extracted the user's Battle.net Account ID (`367827589`) from AppData paths.

