# Overwatch Investigation: Architecture & Interactions

This document contains visual representations of the findings from the Overwatch network and system investigation.

## 1. Local Process Interaction Map
This diagram shows how various system components and third-party applications interact with the main Overwatch process, based on Sysmon telemetry.

```mermaid
graph TD
    %% Main Process
    OW["Overwatch.exe<br/>(Retail Binary)"]
    
    %% Blizzard Supporting Processes
    BNET["Battle.net.exe<br/>(Launcher/CEF)"]
    AGENT["Agent.exe<br/>(Update Agent)"]
    
    %% System Components
    EXP["explorer.exe"]
    DEF["MsMpEng.exe<br/>(Windows Defender)"]
    WMI["wmiprvse.exe<br/>(WMI Provider)"]
    LSASS["lsass.exe"]
    
    %% Third Party
    DISC["Discord.exe"]
    NV["NVIDIA Overlay"]
    XBOX["Xbox Game Bar"]

    %% Interactions (Sysmon correlated)
    DISC -- "Hook/Overlay (95 events)" --> OW
    DEF -- "Scan/Monitor" --> OW
    EXP -- "User Interface/Launch" --> OW
    WMI -- "Query Performance" --> OW
    LSASS -- "Identity/Auth" --> OW
    NV -- "Overlay/GPU Stats" --> OW
    XBOX -- "Gaming Services" --> OW
    
    BNET -- "Launch Child" --> OW
    AGENT -- "Patch/Session Management" --> BNET
```

## 2. Network Communication & Infrastructure
This diagram maps specific binaries to their identified Blizzard and third-party network endpoints, including protocols.

```mermaid
flowchart LR
    subgraph LocalHost [Local Machine]
        direction TB
        P1[Overwatch.exe]
        P2[Battle.net.exe]
        P3[Agent.exe]
        P4[NVIDIA App]
    end

    subgraph BlizzardCloud [Blizzard Infrastructure]
        direction TB
        G1[(Gameplay Servers)]
        S1[Match Ingestion Server]
        T1[Telemetry-in.battle.net]
        A1[Auth / Account Services]
        C1[CDN / Versioning]
    end

    subgraph ExternalServices [Third Party]
        AWS[AWS / Cloudfront]
        CF[Cloudflare]
        NV_CLOUD[NVIDIA Cloud]
    end

    %% Overwatch.exe Connections
    P1 -- "UDP (Direct)" --> G1
    P1 -- "QUIC / TLS 1.3" --> S1
    P1 -- "TCP 1119 / 3724" --> A1
    P1 -- "HTTPS" --> CF

    %% Battle.net Connections
    P2 -- "QUIC (Telemetry)" --> T1
    P2 -- "TLS 1.2 / 1.3" --> A1
    P2 -- "HTTPS" --> AWS

    %% Agent Connections
    P3 -- "HTTPS" --> C1
    
    %% Supporting Connections
    P4 -- "HTTPS (Sync)" --> NV_CLOUD

    %% Styling
    style G1 fill:#f96,stroke:#333,stroke-width:2px
    style LocalHost fill:#f5f5f5,stroke:#333
    style BlizzardCloud fill:#e1f5fe,stroke:#01579b
```

## 3. Data Analysis Pipeline
The technical workflow used to process the packet captures.

```mermaid
sequenceDiagram
    participant PCAP as ow-network-traffic.pcapng
    participant PDML as ow-test.pdml (XML)
    participant SCRIPT as pdml_to_parquet.py
    participant PARQ as enriched.parquet
    participant R as Analysis (Pandas)

    Note over PCAP: Raw Capture (~25MB)
    PCAP->>PDML: tshark conversion
    Note over PDML: Verbose XML (1.6GB!)
    PDML->>SCRIPT: Streaming LXML Parse
    SCRIPT->>PARQ: Columnar Storage
    Note over PARQ: Compressed Data (24KB - 550KB)
    PARQ->>R: Vectorized Querying
    R-->>R: IP-to-Hostname Correlation
```
