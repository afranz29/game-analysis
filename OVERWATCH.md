# Overwatch Network Investigation

Last Updated: 2026-05-31

This document summarizes the findings from the investigation of Overwatch and Blizzard-related network traffic using packet captures, live process monitoring, and system analysis.

## 1. Core Infrastructure

Through combined analysis of static captures and live execution, we mapped the following Blizzard endpoints:

| Service | Domain / Hostname | Identified IP(s) |
| :--- | :--- | :--- |
| **Gameplay** | (Direct UDP Traffic) | `24.105.60.145`, `24.105.60.232` |
| **Active Session** | (Blizzard/AWS) | **`34.182.236.194`** |
| **Match Ingestion** | `overwatch.ingest.gdp.blizzard.com` | `35.201.91.89` |
| **Telemetry** | `telemetry-in.battle.net` | `137.221.105.136`, `137.221.105.232` |
| **Authentication** | `oauth.battle.net`, `account.battle.net` | `100.20.157.63`, `52.38.105.79`, `34.210.233.116` |
| **Content/CDN** | `us.version.battle.net`, `us.cdn.blizzard.com` | `136.110.188.211`, `137.221.64.x` |

## 2. Traffic Signatures

### Gameplay & Control (UDP/TCP)
- **Gameplay Signature:** High frequency of small UDP packets (averaging ~100-200 bytes).
- **Game Service Port:** Live monitoring identified active communication on port **`3724`** (standard Blizzard Game Service port).
- **`wow` Protocol:** `tshark` dissectors identified a subset of control traffic as the **`wow` (World of Warcraft/Blizzard)** protocol, used for game-state management.

### Control & Telemetry (Encrypted)
- **Protocols:** Heavy usage of **TLSv1.3** and **QUIC**.
- **QUIC Streams:** Identified distinct sessions via Destination Connection IDs (DCIDs). 
- **TLS Ciphers:** Primarily uses `0x1302` (**TLS_AES_128_GCM_SHA256**), confirming modern encryption standards despite compatibility labels.

## 3. Live Execution Context

Monitoring the game in an active state revealed the following system metrics:
- **Process:** `Overwatch.exe` (started with `-uid prometheus`).
- **Memory Footprint:** Significant resource usage, stabilizing at **~8.9 GB**.
- **Supporting Ecosystem:** `Battle.net.exe` and `Agent.exe` maintain multiple established telemetry and update connections (port 443) while the game is running.

## 4. Binary Architecture & Purpose

Through web research and system analysis, we defined the roles of each key binary within the Overwatch/Battle.net ecosystem:

*   **`Overwatch.exe` (Game Client)**: Handles core gameplay, heavy asset loading (~8.9 GB RAM), real-time graphics rendering, audio processing, direct UDP gameplay traffic on Blizzard Game Service port `3724`, and session-level telemetry.
*   **`Battle.net.exe` (Desktop Application)**: Represents the user-facing launcher interface. Manages news display, library rendering, social presences, user authentication processes, and Chromium Embedded Framework (CEF) rendering.
*   **`Agent.exe` (Battle.net Update Agent)**: A lightweight background service exposing a local HTTP REST API for the launcher. Responsible for TACT/CASC file streaming, integrity checks, and checking versions/downloads via CDNs.
*   **`libcef.dll` / `chrome_elf.dll` (CEF Support)**: Support libraries imported by `Battle.net.exe` to run the underlying Chromium-based interface elements and crash reporting pipelines.

## 5. Correlated Process Activity

By correlating `osquery` process metadata with the enriched packet data, we mapped the following active conversations:

| Process | Remote IP | Hostname / Service | Role in Session |
| :--- | :--- | :--- | :--- |
| **`Overwatch.exe`** | `24.105.60.232` | **Blizzard Gameplay** | **Active match data (UDP)** |
| **`Overwatch.exe`** | `34.182.236.194` | Overwatch Session (AWS) | Session state management |
| **`Overwatch.exe`** | `35.201.91.89` | `overwatch.ingest...` | Match history upload |
| **`Battle.net.exe`**| `137.221.105.136`| `telemetry-in.battle.net` | Background analytics |
| **`Battle.net.exe`**| `34.125.180.26` | `account.battle.net` | Social & Presence |
| **`Agent.exe`**     | `136.110.188.211`| `us.version.battle.net` | Version checking |
| **`NVIDIA Overlay`**| `3.170.42.8` | `public.games.geforce.com` | Driver settings sync |
| **`Discord.exe`**   | `162.159.130.234`| `cdn.discordapp.com` | Media/Chat assets |

## 6. System Internals (Sysmon Telemetry)

Analysis of a Sysmon capture (`sysmon-overwatch-session.csv`) during active gameplay provided deeper visibility into host-level behavior:

### Process Interaction
The `Overwatch.exe` process is frequently accessed by other system components:
- **System Utilities:** Heavily accessed by `explorer.exe` (150 events), Windows Defender (`MsMpEng.exe`), `lsass.exe`, and WMI providers (`wmiprvse.exe`).
- **Third-Party Integration:** `Discord.exe` frequently accesses the game process (95 events), likely for its overlay and "Rich Presence" (game status) features.
- **Gaming Services:** Accessed by `GameBarFTServer.exe`, `GamingServices.exe`, and `NVDisplay.Container.exe` (NVIDIA drivers).

### DNS Query Attribution
Sysmon confirmed which specific binaries are making the DNS queries we saw in the packet capture:
- **`Overwatch.exe`:** Directly queries for ingestion (`overwatch.ingest.gdp.blizzard.com`), API services (`us.api.blizzard.com`), and CDNs (`us.cdn.blizzard.com`).
- **`Battle.net.exe`:** Handles launcher-specific queries like news (`breaking-news.support.blizzard.com`), telemetry (`telemetry-in.battle.net`), and Google Analytics.
- **`Agent.exe`:** Queries versioning (`us.version.battle.net`) and telemetry endpoints.

## 7. Analysis Methodology

We used a custom-built pipeline to handle large-scale packet data:
1.  **Extraction:** Used `tshark` to convert `.pcapng` to `.pdml` (XML).
2.  **Conversion:** Developed `pdml_to_parquet.py`, a streaming Python parser using `lxml` to convert verbose XML into compressed **Parquet** files.
    - *Result:* 1.6GB of XML was reduced to a manageable, queryable dataset.
3.  **Enrichment:** Extracted DNS queries, TLS SNI, TLS versions/ciphers, and QUIC metadata for correlation.
4.  **Live Validation:** Performed a live capture (`ow-live-sample.pcapng`) and correlated with `osquery` to map PIDs to network endpoints.

---
*Note: This data is derived from the `ow-network-traffic.pcapng` capture and live system state as of May 31, 2026.*
