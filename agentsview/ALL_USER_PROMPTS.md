# All User Prompts by Session
This document contains all genuine user-typed prompts extracted from the raw AgentsView session JSONL logs in full, with no truncation. Auto-generated CLI metadata, tool outputs, and environment setup contexts have been filtered out for readability.

## 👤 Claude TUI Session (5ab83b0f)
- **Source File:** `5ab83b0f-0838-4d1d-adae-74b256b920ae.jsonl`
- **Total Prompts:** `2`

> **Prompt 1** (*2026-05-30 02:11:25*)
>
> are you there

> **Prompt 2** (*2026-05-30 02:11:35*)
>
> explain this codebase to me

---

## 👤 Claude API Session (cd0c62dd)
- **Source File:** `cd0c62dd-12ae-4ea2-9623-71d7e94f8d01.jsonl`
- **Total Prompts:** `2`

> **Prompt 1** (*2026-05-31 19:52:26*)
>
> use the instructions in @PDML.md to convert the large pcapng file

> **Prompt 2** (*2026-05-31 19:55:11*)
>
> I want you to use the script @pdml_to_parquet.py to convert the file. If you modify the script, ensure you save it in a new file.

---

## 👤 Claude Investigation Session (f8ced8fd)
- **Source File:** `f8ced8fd-e122-4ff8-aa98-9aaac01564f3.jsonl`
- **Total Prompts:** `6`

> **Prompt 1** (*2026-06-02 00:58:46*)
>
> Review @sysmon-gaming-monitoring.xml and the @vector-json/windows_events-2026-06-02.json to validate @OVERWATCH.md. I want to see if there is new information or additional perspectives.

> **Prompt 2** (*2026-06-02 00:59:59*)
>
> Check @CLAUDE.md

> **Prompt 3** (*2026-06-02 01:06:40*)
>
> Check osquery for all running processes

> **Prompt 4** (*2026-06-02 01:11:30*)
>
> Can you review @sysmon-gaming-monitoring.xml and see if we missed anything?

> **Prompt 5** (*2026-06-02 01:21:06*)
>
> Review @vector-json/windows_events-2026-06-02.json and see how it compares to @VALIDATION_SUMMARY.md

> **Prompt 6** (*2026-06-02 01:26:29*)
>
> What is different between @vector-json/windows_events-2026-06-02.json and @vector-json-old/windows_events-2026-06-02.json

---

## 👤 Claude Analysis Session (f8f583d3)
- **Source File:** `f8f583d3-8f41-4cfb-957d-8f71ae431a2c.jsonl`
- **Total Prompts:** `2`

> **Prompt 1** (*2026-05-31 20:27:03*)
>
> Explain @sysmonconfig-export.xml

> **Prompt 2** (*2026-05-31 20:28:28*)
>
> I want to use this file to monitor Overwatch applications. How should I modify it

---

## 👤 Gemini AI Session (444800ed)
- **Source File:** `gemini444800ed-2cc3-46f3-a186-beb9da353a23.jsonl`
- **Total Prompts:** `103`

> **Prompt 1** (*2026-05-31 19:06:28*)
>
> Is osqueryi.exe installed?

> **Prompt 2** (*2026-05-31 19:11:40*)
>
> find when my windows was last patched

> **Prompt 3** (*2026-05-31 19:12:00*)
>
> use osquery

> **Prompt 4** (*2026-05-31 19:13:08*)
>
> can you tell me all my installed software (using os query)

> **Prompt 5** (*2026-05-31 19:15:33*)
>
> Update @SOFTWARE.md and @PATH-HISTORY.md based on this information

> **Prompt 6** (*2026-05-31 19:16:40*)
>
> Let's explore running processes

> **Prompt 7** (*2026-05-31 19:17:41*)
>
> Can you give me more details about the network connections for each of these processes?

> **Prompt 8** (*2026-05-31 19:18:55*)
>
> What is the NVDIA Overlay and why does it need network communication

> **Prompt 9** (*2026-05-31 19:30:41*)
>
> have I installed any new software?

> **Prompt 10** (*2026-05-31 19:33:27*)
>
> Review the NVIDIA Connections

> **Prompt 11** (*2026-05-31 19:34:54*)
>
> Can you tell what files the overlay is accessing?

> **Prompt 12** (*2026-05-31 19:38:05*)
>
> Can you analyze @ow-network-traffic.pcapng

> **Prompt 13** (*2026-05-31 19:39:28*)
>
> Convert @ow-network-traffic.pcapng to a pdml using tshark

> **Prompt 14** (*2026-05-31 19:43:38*)
>
> Extract a thouesand packets into a new pdml file that we can use for testing

> **Prompt 15** (*2026-05-31 19:45:20*)
>
> Can you convert @ow-test.pdml to parquet using Python. Remember to use uv to install any new packages and create a venv.

> **Prompt 16** (*2026-05-31 19:51:13*)
>
> Capture what you did in @PDML.md, explaining what you did to convert it and why you did what you did

> **Prompt 17** (*2026-05-31 19:57:23*)
>
> Create python scripts to identify overwatch traffic patterns in @ow-network-traffic.parquet . Save the scripts to .py files

> **Prompt 18** (*2026-05-31 19:57:23*)
>
> Cannot display content of binary file: ow-network-traffic.parquet

> **Prompt 19** (*2026-05-31 19:59:13*)
>
> Can you look for DNS queries or TLS SNI to also identify more traffic

> **Prompt 20** (*2026-05-31 19:59:42*)
>
> Use the parquet

> **Prompt 21** (*2026-05-31 20:02:31*)
>
> That's great that you added those enrichments. Can we review the original file to see what additional protocol schemas that we should add to our parquet

> **Prompt 22** (*2026-05-31 20:03:51*)
>
> what have you found so far

> **Prompt 23** (*2026-05-31 20:04:24*)
>
> what do you remember about your current task

> **Prompt 24** (*2026-05-31 20:05:19*)
>
> Let's add QUIC and TLSv1.3 to our @pdml_to_parquet.py

> **Prompt 25** (*2026-05-31 20:05:19*)
>
> from lxml import etree
> import pandas as pd
> import sys
> 
> def parse_pdml(file_path):
>     print(f"Parsing {file_path}...")
>     context = etree.iterparse(file_path, events=('end',), tag='packet')
>     packets = []
>     
>     count = 0
>     for event, elem in context:
>         packet_data = {}
>         
>         # Basic info from geninfo and other protos
>         for proto in elem.findall('proto'):
>             proto_name = proto.get('name')
>             
>             # Frame number and length
>             if proto_name == 'geninfo':
>                 num = proto.find(".//field[@name='num']")
>                 if num is not None: packet_data['frame_number'] = num.get('show')
>                 
>                 ts = proto.find(".//field[@name='timestamp']")
>                 if ts is not None: packet_data['timestamp'] = ts.get('show')
>                 
>                 len_field = proto.find(".//field[@name='len']")
>                 if len_field is not None: packet_data['length'] = int(len_field.get('show'))
> 
>             # IP Addresses
>             elif proto_name == 'ip':
>                 src = proto.find(".//field[@name='ip.src']")
>                 if src is not None: packet_data['src_ip'] = src.get('show')
>                 
>                 dst = proto.find(".//field[@name='ip.dst']")
>                 if dst is not None: packet_data['dst_ip'] = dst.get('show')
>             
>             # IPv6 Addresses
>             elif proto_name == 'ipv6':
>                 src = proto.find(".//field[@name='ipv6.src']")
>                 if src is not None: packet_data['src_ip'] = src.get('show')
>                 
>                 dst = proto.find(".//field[@name='ipv6.dst']")
>                 if dst is not None: packet_data['dst_ip'] = dst.get('show')
> 
>             # DNS Queries
>             elif proto_name == 'dns':
>                 qry = proto.xpath(".//field[@name='dns.qry.name']")
>                 if qry:
>                     packet_data['dns_query'] = qry[0].get('show')
> 
>             # TLS SNI
>             elif proto_name == 'tls':
>                 sni = proto.xpath(".//field[@name='tls.handshake.extensions_server_name']")
>                 if sni:
>                     packet_data['tls_sni'] = sni[0].get('show')
> 
>             # Ports (TCP/UDP)
>             elif proto_name in ['tcp', 'udp']:
>                 packet_data['protocol'] = proto_name.upper()
>                 
>                 # Use xpath for robust field finding
>                 src_port_elem = proto.xpath(".//field[@name='tcp.srcport' or @name='udp.srcport']")
>                 if src_port_elem:
>                     packet_data['src_port'] = int(src_port_elem[0].get('show'))
>                 
>                 dst_port_elem = proto.xpath(".//field[@name='tcp.dstport' or @name='udp.dstport']")
>                 if dst_port_elem:
>                     packet_data['dst_port'] = int(dst_port_elem[0].get('show'))
> 
>         # If protocol not set by TCP/UDP, get the highest layer protocol name
>         if 'protocol' not in packet_data:
>             # Get the last proto that isn't geninfo, frame, or eth
>             protos = [p.get('name') for p in elem.findall('proto') if p.get('name') not in ['geninfo', 'frame', 'eth', 'ip', 'ipv6']]
>             if protos:
>                 packet_data['protocol'] = protos[-1].upper()
>             else:
>                 packet_data['protocol'] = 'OTHER'
> 
>         packets.append(packet_data)
>         count += 1
>         if count % 100 == 0:
>             print(f"Processed {count} packets...")
>         
>         # Clean up element to save memory
>         elem.clear()
>         while elem.getprevious() is not None:
>             del elem.getparent()[0]
>             
>     return pd.DataFrame(packets)
> 
> if __name__ == "__main__":
>     input_file = "D:/WindowsInvestigations/ow-network-traffic.pdml"
>     output_file = "D:/WindowsInvestigations/ow-network-traffic-enriched.parquet"
>     
>     df = parse_pdml(input_file)
>     print(f"Saving {len(df)} packets to {output_file}...")
>     df.to_parquet(output_file, engine='pyarrow')
>     print("Done!")

> **Prompt 26** (*2026-05-31 20:07:17*)
>
> Is osqueryi.exe installed?

> **Prompt 27** (*2026-05-31 20:07:17*)
>
> find when my windows was last patched

> **Prompt 28** (*2026-05-31 20:07:17*)
>
> use osquery

> **Prompt 29** (*2026-05-31 20:07:17*)
>
> can you tell me all my installed software (using os query)

> **Prompt 30** (*2026-05-31 20:07:17*)
>
> Update @SOFTWARE.md and @PATH-HISTORY.md based on this information

> **Prompt 31** (*2026-05-31 20:07:17*)
>
> Let's explore running processes

> **Prompt 32** (*2026-05-31 20:07:17*)
>
> Can you give me more details about the network connections for each of these processes?

> **Prompt 33** (*2026-05-31 20:07:17*)
>
> What is the NVDIA Overlay and why does it need network communication

> **Prompt 34** (*2026-05-31 20:07:17*)
>
> have I installed any new software?

> **Prompt 35** (*2026-05-31 20:07:17*)
>
> Review the NVIDIA Connections

> **Prompt 36** (*2026-05-31 20:07:17*)
>
> Can you tell what files the overlay is accessing?

> **Prompt 37** (*2026-05-31 20:07:17*)
>
> Can you analyze @ow-network-traffic.pcapng

> **Prompt 38** (*2026-05-31 20:07:17*)
>
> Convert @ow-network-traffic.pcapng to a pdml using tshark

> **Prompt 39** (*2026-05-31 20:07:17*)
>
> Extract a thouesand packets into a new pdml file that we can use for testing

> **Prompt 40** (*2026-05-31 20:07:17*)
>
> Can you convert @ow-test.pdml to parquet using Python. Remember to use uv to install any new packages and create a venv.

> **Prompt 41** (*2026-05-31 20:07:17*)
>
> Capture what you did in @PDML.md, explaining what you did to convert it and why you did what you did

> **Prompt 42** (*2026-05-31 20:07:17*)
>
> Create python scripts to identify overwatch traffic patterns in @ow-network-traffic.parquet . Save the scripts to .py files

> **Prompt 43** (*2026-05-31 20:07:17*)
>
> Cannot display content of binary file: ow-network-traffic.parquet

> **Prompt 44** (*2026-05-31 20:07:17*)
>
> Can you look for DNS queries or TLS SNI to also identify more traffic

> **Prompt 45** (*2026-05-31 20:07:17*)
>
> Use the parquet

> **Prompt 46** (*2026-05-31 20:07:17*)
>
> That's great that you added those enrichments. Can we review the original file to see what additional protocol schemas that we should add to our parquet

> **Prompt 47** (*2026-05-31 20:07:17*)
>
> what have you found so far

> **Prompt 48** (*2026-05-31 20:07:17*)
>
> what do you remember about your current task

> **Prompt 49** (*2026-05-31 20:07:17*)
>
> Let's add QUIC and TLSv1.3 to our @pdml_to_parquet.py

> **Prompt 50** (*2026-05-31 20:07:17*)
>
> from lxml import etree
> import pandas as pd
> import sys
> 
> def parse_pdml(file_path):
>     print(f"Parsing {file_path}...")
>     context = etree.iterparse(file_path, events=('end',), tag='packet')
>     packets = []
>     
>     count = 0
>     for event, elem in context:
>         packet_data = {}
>         
>         # Basic info from geninfo and other protos
>         for proto in elem.findall('proto'):
>             proto_name = proto.get('name')
>             
>             # Frame number and length
>             if proto_name == 'geninfo':
>                 num = proto.find(".//field[@name='num']")
>                 if num is not None: packet_data['frame_number'] = num.get('show')
>                 
>                 ts = proto.find(".//field[@name='timestamp']")
>                 if ts is not None: packet_data['timestamp'] = ts.get('show')
>                 
>                 len_field = proto.find(".//field[@name='len']")
>                 if len_field is not None: packet_data['length'] = int(len_field.get('show'))
> 
>             # IP Addresses
>             elif proto_name == 'ip':
>                 src = proto.find(".//field[@name='ip.src']")
>                 if src is not None: packet_data['src_ip'] = src.get('show')
>                 
>                 dst = proto.find(".//field[@name='ip.dst']")
>                 if dst is not None: packet_data['dst_ip'] = dst.get('show')
>             
>             # IPv6 Addresses
>             elif proto_name == 'ipv6':
>                 src = proto.find(".//field[@name='ipv6.src']")
>                 if src is not None: packet_data['src_ip'] = src.get('show')
>                 
>                 dst = proto.find(".//field[@name='ipv6.dst']")
>                 if dst is not None: packet_data['dst_ip'] = dst.get('show')
> 
>             # DNS Queries
>             elif proto_name == 'dns':
>                 qry = proto.xpath(".//field[@name='dns.qry.name']")
>                 if qry:
>                     packet_data['dns_query'] = qry[0].get('show')
> 
>             # TLS SNI
>             elif proto_name == 'tls':
>                 sni = proto.xpath(".//field[@name='tls.handshake.extensions_server_name']")
>                 if sni:
>                     packet_data['tls_sni'] = sni[0].get('show')
> 
>             # Ports (TCP/UDP)
>             elif proto_name in ['tcp', 'udp']:
>                 packet_data['protocol'] = proto_name.upper()
>                 
>                 # Use xpath for robust field finding
>                 src_port_elem = proto.xpath(".//field[@name='tcp.srcport' or @name='udp.srcport']")
>                 if src_port_elem:
>                     packet_data['src_port'] = int(src_port_elem[0].get('show'))
>                 
>                 dst_port_elem = proto.xpath(".//field[@name='tcp.dstport' or @name='udp.dstport']")
>                 if dst_port_elem:
>                     packet_data['dst_port'] = int(dst_port_elem[0].get('show'))
> 
>         # If protocol not set by TCP/UDP, get the highest layer protocol name
>         if 'protocol' not in packet_data:
>             # Get the last proto that isn't geninfo, frame, or eth
>             protos = [p.get('name') for p in elem.findall('proto') if p.get('name') not in ['geninfo', 'frame', 'eth', 'ip', 'ipv6']]
>             if protos:
>                 packet_data['protocol'] = protos[-1].upper()
>             else:
>                 packet_data['protocol'] = 'OTHER'
> 
>         packets.append(packet_data)
>         count += 1
>         if count % 100 == 0:
>             print(f"Processed {count} packets...")
>         
>         # Clean up element to save memory
>         elem.clear()
>         while elem.getprevious() is not None:
>             del elem.getparent()[0]
>             
>     return pd.DataFrame(packets)
> 
> if __name__ == "__main__":
>     input_file = "D:/WindowsInvestigations/ow-network-traffic.pdml"
>     output_file = "D:/WindowsInvestigations/ow-network-traffic-enriched.parquet"
>     
>     df = parse_pdml(input_file)
>     print(f"Saving {len(df)} packets to {output_file}...")
>     df.to_parquet(output_file, engine='pyarrow')
>     print("Done!")

> **Prompt 51** (*2026-05-31 20:12:48*)
>
> Update @OVERWATCH.md with your findings

> **Prompt 52** (*2026-05-31 20:13:49*)
>
> Using osquery, what can you find out about overwatch

> **Prompt 53** (*2026-05-31 20:16:31*)
>
> I am now running the game. Look for process and network activity

> **Prompt 54** (*2026-05-31 20:17:20*)
>
> sure

> **Prompt 55** (*2026-05-31 20:20:22*)
>
> Add these findings to @OVERWATCH.md

> **Prompt 56** (*2026-05-31 20:20:22*)
>
> # Overwatch Network Investigation
> 
> Last Updated: 2026-05-31
> 
> This document summarizes the findings from the investigation of Overwatch and Blizzard-related network traffic using packet captures and system analysis.
> 
> ## 1. Core Infrastructure
> 
> Through DNS and TLS SNI analysis, we mapped the following key Blizzard endpoints:
> 
> | Service | Domain / Hostname | Identified IP(s) |
> | :--- | :--- | :--- |
> | **Gameplay** | (Direct UDP Traffic) | `24.105.60.145` |
> | **Match Ingestion** | `overwatch.ingest.gdp.blizzard.com` | `35.201.91.89` |
> | **Telemetry** | `telemetry-in.battle.net` | `137.221.105.136`, `137.221.105.232` |
> | **Authentication** | `oauth.battle.net`, `account.battle.net` | `100.20.157.63`, `52.38.105.79`, `34.210.233.116` |
> | **Content/CDN** | `us.version.battle.net`, `us.cdn.blizzard.com` | `136.110.188.211`, `137.221.64.x` |
> 
> ## 2. Traffic Signatures
> 
> ### Gameplay (UDP)
> - **Pattern:** High frequency of small packets (averaging ~100-200 bytes).
> - **Behavior:** Symmetrical flow between the local machine and Blizzard gameplay servers.
> 
> ### Control & Telemetry (Encrypted)
> - **Protocols:** Heavy usage of **TLSv1.3** and **QUIC**.
> - **QUIC Streams:** Identified distinct sessions via Destination Connection IDs (DCIDs). 
>     - *Example DCID:* `12:38:62:3c:38:80:80:2e` (500+ packets).
> - **TLS Ciphers:** Primarily uses `0x1302` (**TLS_AES_128_GCM_SHA256**), confirming modern encryption standards despite compatibility labels.
> 
> ## 3. Analysis Methodology
> 
> We used a custom-built pipeline to handle large-scale packet data:
> 1.  **Extraction:** Used `tshark` to convert `.pcapng` to `.pdml` (XML).
> 2.  **Conversion:** Developed `pdml_to_parquet.py`, a streaming Python parser using `lxml` to convert verbose XML into compressed **Parquet** files.
>     - *Result:* 1.6GB of XML was reduced to a manageable, queryable dataset.
> 3.  **Enrichment:** Extracted DNS queries, TLS SNI, TLS versions/ciphers, and QUIC metadata for correlation.
> 
> ## 4. System Context
> - **Last Patch:** May 26, 2026 (KB5078674).
> - **Environment:** Recent setup of Node.js and osquery indicates an active development/investigation session.
> - **Supporting Processes:** NVIDIA Overlay was found communicating locally with GPU drivers while maintaining its own encrypted cloud connections for settings and telemetry.
> 
> ---
> *Note: This data is derived from the `ow-network-traffic.pcapng` capture.*

> **Prompt 57** (*2026-05-31 20:21:37*)
>
> Correlate the osquery information with the wireshark data so we can see the full picture of which processes are communicating with which network destinations

> **Prompt 58** (*2026-05-31 20:28:05*)
>
> Add this to @OVERWATCH.md

> **Prompt 59** (*2026-05-31 20:28:05*)
>
> # Overwatch Network Investigation
> 
> Last Updated: 2026-05-31
> 
> This document summarizes the findings from the investigation of Overwatch and Blizzard-related network traffic using packet captures, live process monitoring, and system analysis.
> 
> ## 1. Core Infrastructure
> 
> Through combined analysis of static captures and live execution, we mapped the following Blizzard endpoints:
> 
> | Service | Domain / Hostname | Identified IP(s) |
> | :--- | :--- | :--- |
> | **Gameplay** | (Direct UDP Traffic) | `24.105.60.145`, `24.105.60.232` |
> | **Active Session** | (Blizzard/AWS) | **`34.182.236.194`** |
> | **Match Ingestion** | `overwatch.ingest.gdp.blizzard.com` | `35.201.91.89` |
> | **Telemetry** | `telemetry-in.battle.net` | `137.221.105.136`, `137.221.105.232` |
> | **Authentication** | `oauth.battle.net`, `account.battle.net` | `100.20.157.63`, `52.38.105.79`, `34.210.233.116` |
> | **Content/CDN** | `us.version.battle.net`, `us.cdn.blizzard.com` | `136.110.188.211`, `137.221.64.x` |
> 
> ## 2. Traffic Signatures
> 
> ### Gameplay & Control (UDP/TCP)
> - **Gameplay Signature:** High frequency of small UDP packets (averaging ~100-200 bytes).
> - **Game Service Port:** Live monitoring identified active communication on port **`3724`** (standard Blizzard Game Service port).
> - **`wow` Protocol:** `tshark` dissectors identified a subset of control traffic as the **`wow` (World of Warcraft/Blizzard)** protocol, used for game-state management.
> 
> ### Control & Telemetry (Encrypted)
> - **Protocols:** Heavy usage of **TLSv1.3** and **QUIC**.
> - **QUIC Streams:** Identified distinct sessions via Destination Connection IDs (DCIDs). 
> - **TLS Ciphers:** Primarily uses `0x1302` (**TLS_AES_128_GCM_SHA256**), confirming modern encryption standards despite compatibility labels.
> 
> ## 3. Live Execution Context
> 
> Monitoring the game in an active state revealed the following system metrics:
> - **Process:** `Overwatch.exe` (started with `-uid prometheus`).
> - **Memory Footprint:** Significant resource usage, stabilizing at **~8.9 GB**.
> - **Supporting Ecosystem:** `Battle.net.exe` and `Agent.exe` maintain multiple established telemetry and update connections (port 443) while the game is running.
> 
> ## 4. Analysis Methodology
> 
> We used a custom-built pipeline to handle large-scale packet data:
> 1.  **Extraction:** Used `tshark` to convert `.pcapng` to `.pdml` (XML).
> 2.  **Conversion:** Developed `pdml_to_parquet.py`, a streaming Python parser using `lxml` to convert verbose XML into compressed **Parquet** files.
>     - *Result:* 1.6GB of XML was reduced to a manageable, queryable dataset.
> 3.  **Enrichment:** Extracted DNS queries, TLS SNI, TLS versions/ciphers, and QUIC metadata for correlation.
> 4.  **Live Validation:** Performed a live capture (`ow-live-sample.pcapng`) to verify infrastructure and identify active session IPs.
> 
> ---
> *Note: This data is derived from the `ow-network-traffic.pcapng` capture and live system state as of May 31, 2026.*

> **Prompt 60** (*2026-05-31 20:41:23*)
>
> I have run sysmon and extracted during a short session of Overwatch in @sysmon-overwatch-session.csv. Correlate with existing data.

> **Prompt 61** (*2026-05-31 20:41:23*)
>
> [WARNING: This file was truncated. To view the full content, use the 'read_file' tool on this specific file.]
> 
> "Message","Id","Version","Qualifiers","Level","Task","Opcode","Keywords","RecordId","ProviderName","ProviderId","LogName","ProcessId","ThreadId","MachineName","UserId","TimeCreated","ActivityId","RelatedActivityId","ContainerLog","MatchedQueryIds","Bookmark","LevelDisplayName","OpcodeDisplayName","TaskDisplayName","KeywordsDisplayNames","Properties"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:21.383
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1657","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:21 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:21.351
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\Agent.9464\Logs\Telemetry-MessageStats-20260531T203409.log
> CreationUtcTime: 2026-05-31 20:36:21.351
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1656","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:21 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:18.121
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\product.db.new
> CreationUtcTime: 2026-05-31 20:36:00.986
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1655","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:18 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:17.807
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\aggregate.json
> CreationUtcTime: 2026-05-26 05:21:27.424
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1654","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:17 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:14.959
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1653","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.959
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 6380
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea60b|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a30fe|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a5678|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+694380|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6ed19a|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6cbe88|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a7ba5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a48ae|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a4e87|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d4b68|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87478|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87363|C:\WINDOWS\SYSTEM32\ntdll.dll+23080|C:\WINDOWS\SYSTEM32\ntdll.dll+240d1|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1652","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.959
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1651","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.923
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 6380
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea60b|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a30fe|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a5678|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+694380|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6ed19a|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6cbe88|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a7ba5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a48ae|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a4e87|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d4b68|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87478|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87363|C:\WINDOWS\SYSTEM32\ntdll.dll+23080|C:\WINDOWS\SYSTEM32\ntdll.dll+240d1|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1650","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.923
> ProcessGuid: {f162fe7e-9b56-6a1c-0251-000000000900}
> ProcessId: 27488
> Image: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1649","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.921
> ProcessGuid: {f162fe7e-9b56-6a1c-0251-000000000900}
> ProcessId: 27488
> Image: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> ImageLoaded: C:\Windows\System32\kernel.appcore.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: AppModel API Host
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: kernel.appcore.dll
> Hashes: MD5=65800310E00B24D50F743F7C771E53BF,SHA256=E47C8F31C70A91AAF199CAAB2338896D6DF86B2EE4E64D6F274B698223DFDC98,IMPHASH=066FFFA45EF798520DE9BAA65A2B842C
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1648","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:13.776
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1647","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:13 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:13.776
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1646","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:13 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.733
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\mfcore.dll
> FileVersion: 10.0.26100.8457 (WinBuild.160101.0800)
> Description: Media Foundation Core DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: mfcore.dll
> Hashes: MD5=CEC4D20C64C01C79599534DC707E2757,SHA256=7013064E8E28AF30C112421745309966FD9223C7F8B9009C9E5F730EF1069F20,IMPHASH=3A94DB83E3B4FB80067B95BD968A8FDA
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1645","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.703
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\mfreadwrite.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: Media Foundation ReadWrite DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: mfreadwrite.dll
> Hashes: MD5=0541E513C50E55899FBB8A68FB90B9B8,SHA256=650A295DB62D5063BAAF81BD1E79278B39B4820DD48C80720B885C4302D5F79B,IMPHASH=36FA6935F2A7B5813A2A9B94E71F0303
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1644","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.707
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1643","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.707
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1642","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.695
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\RTWorkQ.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: Realtime WorkQueue DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: RTWorkQ.dll
> Hashes: MD5=DC5051E80CF552032ADAA0740FA59C3D,SHA256=63FDDAD8759720F0AA43FC15C466BB74B52593F7CE5980829CA4BA92D3B10A71,IMPHASH=163F592AB493FBB3AC3448DC8A20F69A
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1641","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.706
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 15944
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea60b|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a30fe|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a5678|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6933cf|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6ed19a|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6cbe88|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a7ba5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a48ae|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a4e87|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d4b68|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87478|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87363|C:\WINDOWS\SYSTEM32\ntdll.dll+23080|C:\WINDOWS\SYSTEM32\ntdll.dll+240d1|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1640","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.690
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\mfplat.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: Media Foundation Platform DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: mfplat.dll
> Hashes: MD5=6390028C7C457B7F914C98AA3B937B53,SHA256=43C897A3C4190644EEAD791EA82B1503CC26F597D36B5A2CE6AF1C029584C046,IMPHASH=8E87A39D335960D7F555429CE77476BA
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1639","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.696
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1638","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.674
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\mf.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: Media Foundation DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: mf.dll
> Hashes: MD5=CEE73D01E8BEACAC4D198A5685C5708C,SHA256=4462ADC94833D295193A704850D697D8D51066BC127686232E2A51F33BE358F5,IMPHASH=C2DAA55E55F79F6858A11E283694053A
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1637","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.671
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 15944
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea60b|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a30fe|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a5678|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6933cf|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6ed19a|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6cbe88|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a7ba5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a48ae|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a4e87|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d4b68|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87478|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87363|C:\WINDOWS\SYSTEM32\ntdll.dll+23080|C:\WINDOWS\SYSTEM32\ntdll.dll+240d1|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1636","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.564
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d5cdc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9b8b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1635","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.429
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1634","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.429
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1633","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.418
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1632","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.074
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\product.db.new
> CreationUtcTime: 2026-05-31 20:36:00.986
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1631","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:09.767
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1630","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:09 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:09.767
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1629","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:09 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:07.696
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1628","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:07 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:07.696
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1627","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:07 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:07.685
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1626","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:07 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:05.769
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1625","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:05 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:05.769
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1624","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:05 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:05.565
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d5cdc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9b8b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1623","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:05 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:02.689
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1622","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:02.689
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1621","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:02.676
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1620","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.694
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: false
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50528
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1619","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.694
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50528
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1618","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.754
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1617","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.754
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1616","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:01.108
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1615","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.107
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1614","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.070
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Roaming\Battle.net\Battle.net.config
> CreationUtcTime: 2026-05-26 05:23:00.710
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1613","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.069
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Roaming\Battle.net\15ec9a85.config
> CreationUtcTime: 2026-05-26 05:24:15.911
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1612","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.986
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\product.db.new
> CreationUtcTime: 2026-05-31 20:36:00.986
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1611","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.671
> ProcessGuid: {f162fe7e-9b42-6a1c-db50-000000000900}
> ProcessId: 16276
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1610","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.671
> ProcessGuid: {f162fe7e-9b42-6a1c-db50-000000000900}
> ProcessId: 16276
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1609","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.639
> ProcessGuid: {f162fe7e-9b42-6a1c-dc50-000000000900}
> ProcessId: 11524
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1608","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.639
> ProcessGuid: {f162fe7e-9b42-6a1c-dc50-000000000900}
> ProcessId: 11524
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1607","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.629
> ProcessGuid: {f162fe7e-9b42-6a1c-dd50-000000000900}
> ProcessId: 18772
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1606","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.629
> ProcessGuid: {f162fe7e-9b42-6a1c-dd50-000000000900}
> ProcessId: 18772
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1605","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.556
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d5cdc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9b8b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1604","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.435
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1603","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.435
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1602","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.423
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1601","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.094
> ProcessGuid: {f162fe7e-9b42-6a1c-dd50-000000000900}
> ProcessId: 18772
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\BrowserCaches\367827589\Network\Network Persistent State~RFf89bc1c.TMP
> CreationUtcTime: 2026-05-31 20:36:00.094
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1600","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.082
> ProcessGuid: {f162fe7e-9b4d-6a1c-f150-000000000900}
> ProcessId: 20388
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1599","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.082
> ProcessGuid: {f162fe7e-9b4d-6a1c-f150-000000000900}
> ProcessId: 20388
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1598","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.072
> ProcessGuid: {f162fe7e-9b42-6a1c-dd50-000000000900}
> ProcessId: 18772
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\BrowserCaches\367827589\Network\db1b5eea-716d-424a-8214-6bb1ebbb8809.tmp
> CreationUtcTime: 2026-05-31 20:36:00.072
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1597","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.022
> ProcessGuid: {f162fe7e-9b46-6a1c-ef50-000000000900}
> ProcessId: 13400
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1596","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.014
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\CachedData.db-journal
> CreationUtcTime: 2026-05-31 20:35:59.985
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1595","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.012
> ProcessGuid: {f162fe7e-9b46-6a1c-ef50-000000000900}
> ProcessId: 13400
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1594","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.004
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\CachedData.db-journal
> CreationUtcTime: 2026-05-31 20:35:59.985
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1593","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.000
> ProcessGuid: {f162fe7e-9b4e-6a1c-f350-000000000900}
> ProcessId: 30404
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1592","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:35:59.999
> ProcessGuid: {f162fe7e-9b4e-6a1c-f350-000000000900}
> ProcessId: 30404
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1591","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:35:59.999
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\CachedData.db-journal
> CreationUtcTime: 2026-05-31 20:35:59.985
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1590","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:35:59.999
> ProcessGuid: {f162fe7e-9b45-6a1c-e150-000000000900}
> ProcessId: 28220
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1589","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:35:59.996
> ProcessGuid: {f162fe7e-9b45-6a1c-e150-000000000900}
> ProcessId: 28220
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1588","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:58.438
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: false
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50527
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1587","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:58.438
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50527
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1586","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.954
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50521
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1585","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50516
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1584","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50525
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1583","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50523
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1582","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50517
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1581","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50524
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1580","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50519
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1579","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50522
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1578","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50520
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1577","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50518
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1576","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50526
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1575","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.950
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50515
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1574","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.950
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50513
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1573","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.950
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50514
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1572","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.949
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50512
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1571","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:35:59.985
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\CachedData.db-journal
> CreationUtcTime: 2026-05-31 20:35:59.985
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1570","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Dns query:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.870
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> QueryName: overwatch.ingest.gdp.blizzard.com
> QueryStatus: 0
> QueryResults: ::ffff:35.201.91.89;
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac","22","5",,"4","22","0","-9223372036854775808","1569","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","28092","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.971
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1568","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.970
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1567","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.969
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1566","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.969
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1565","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.968
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1564","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.963
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1563","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.963
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1562","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.961
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1561","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.960
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1560","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.959
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1559","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.956
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1558","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.955
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1557","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.955
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1556","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.951
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1555","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.950
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1554","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File Delete archived:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.773
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> User: Panda-PC\annac
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetFilename: C:\Users\annac\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini_LOCK
> Hashes: MD5=0D542CD521BEA05A4C3D12EE43FD332C,SHA256=B653C87B7FCA89E0005891743B9F60F83254830C940C8FF0A3A9DC24BB419D24,IMPHASH=00000000000000000000000000000000
> IsExecutable: false
> Archived: true","23","5",,"4","23","0","-9223372036854775808","1553","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Error report:
> UtcTime: 2026-05-31 20:35:57.773
> ID: FILE_DELETE
> Description: The ""C:\Sysmon\"" owner is not System. Archiving is disabled.","255","3",,"2","255","0","-9223372036854775808","1552","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Error","Info",,"System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.772
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetFilename: C:\Users\annac\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini
> CreationUtcTime: 2026-05-26 03:17:19.616
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1551","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File Delete archived:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.772
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> User: Panda-PC\annac
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetFilename: C:\Users\annac\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini
> Hashes: MD5=F5816CE03EDED4C63D23E7D4DEAB84C8,SHA256=AE457B305A292DFAB7F454F7062FEC9CA59985AF6DF1D40803744E2A1F0C109A,IMPHASH=00000000000000000000000000000000
> IsExecutable: false
> Archived: true","23","5",,"4","23","0","-9223372036854775808","1550","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Error report:
> UtcTime: 2026-05-31 20:35:57.772
> ID: FILE_DELETE
> Description: The ""C:\Sysmon\"" owner is not System. Archiving is disabled.","255","3",,"2","255","0","-9223372036854775808","1549","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Error","Info",,"System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.770
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetFilename: C:\Users\annac\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini_LOCK
> CreationUtcTime: 2026-05-31 20:35:57.770
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1548","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.750
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1547","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.750
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1546","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.677
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1545","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.676
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1544","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.664
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1543","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.724
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: udp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 4242
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 224.0.0.5
> DestinationHostname: ospf-all.mcast.net
> DestinationPort: 4242
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1542","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:56 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.437
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: false
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50511
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1541","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:56 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.437
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50511
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1540","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:56 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.539
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d5cdc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9b8b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1539","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.536
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130608|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+1304d5|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9761|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1538","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.528
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+da773|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d95cc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1537","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.526
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d95a7|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1536","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.498
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 12116
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d97dc|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa096|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f2498|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa934|C:\WINDOWS\SYSTEM32\sechost.dll+4208|C:\WINDOWS\SYSTEM32\sechost.dll+29af|C:\WINDOWS\SYSTEM32\sechost.dll+23207|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f43e5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+17d27f|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1535","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:54.478
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 12116
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d97dc|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa096|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f2498|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa934|C:\WINDOWS\SYSTEM32\sechost.dll+4208|C:\WINDOWS\SYSTEM32\sechost.dll+29af|C:\WINDOWS\SYSTEM32\sechost.dll+23207|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f43e5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+17d27f|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1534","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:54 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:53.751
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1533","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:53 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:53.751
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1532","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:53 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.426
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: false
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50510
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1531","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:53 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.426
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50510
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1530","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:53 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.647
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1529","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:52 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.446
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 12116
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d97dc|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa096|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f2498|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa934|C:\WINDOWS\SYSTEM32\sechost.dll+4208|C:\WINDOWS\SYSTEM32\sechost.dll+29af|C:\WINDOWS\SYSTEM32\sechost.dll+23207|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f43e5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+17d27f|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1528","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:52 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.446
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 12116
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d97dc|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa096|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f2498|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa934|C:\WINDOWS\SYSTEM32\sechost.dll+4208|C:\WINDOWS\SYSTEM32\sechost.dll+29af|C:\WINDOWS\SYSTEM32\sechost.dll+23207|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f43e5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+17d27f|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1527","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:52 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.984
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 8632
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\Windows\System32\TWINAPI.dll+7587|C:\WINDOWS\SYSTEM32\twinui.dll+156d6|C:\WINDOWS\SYSTEM32\twinui.dll+2cb173|C:\WINDOWS\SYSTEM32\twinui.dll+2ca4e2|C:\WINDOWS\System32\user32.dll+3d2d6|C:\WINDOWS\SYSTEM32\twinui.dll+2ca451|C:\WINDOWS\SYSTEM32\twinui.dll+37af6|C:\WINDOWS\SYSTEM32\twinui.dll+35fec|C:\WINDOWS\SYSTEM32\twinui.dll+3781d|C:\WINDOWS\SYSTEM32\twinui.dll+51e03|C:\WINDOWS\SYSTEM32\twinui.dll+acfb|C:\WINDOWS\SYSTEM32\twinui.dll+a92b|C:\WINDOWS\SYSTEM32\twinui.dll+51047|C:\WINDOWS\SYSTEM32\twinui.dll+1ecca|C:\WINDOWS\SYSTEM32\twinui.dll+1ec4c|C:\WINDOWS\System32\user32.dll+c396|C:\WINDOWS\System32\user32.dll+a7ed|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+3d4f|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+1727f|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+52ea1|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+52de9|C:\WINDOWS\System32\KERNEL32.DLL+2e957
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1526","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.524
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1525","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.517
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1524","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.517
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1523","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.516
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1522","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.515
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1521","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.515
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1520","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.514
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1519","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.514
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1518","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.508
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1517","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.507
> SourceProcessGUID: {f162fe7e-a179-6a18-0d00-000000000900}
> SourceProcessId: 1288
> SourceThreadId: 13344
> SourceImage: C:\WINDOWS\system32\svchost.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+983e|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+9a15|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+a0f0|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+8c35|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+6e8c|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+d570e|C:\WINDOWS\System32\RPCRT4.dll+8a77c|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4ea88|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc|C:\WINDOWS\System32\RPCRT4.dll+51fdc|C:\WINDOWS\System32\RPCRT4.dll+51163|C:\WINDOWS\System32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1516","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.505
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5ec48|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a5dd0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7326|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1515","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.505
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5ec48|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a5dd0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7326|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1514","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.485
> SourceProcessGUID: {f162fe7e-83df-6a1c-6442-000000000900}
> SourceProcessId: 6844
> SourceThreadId: 28972
> SourceImage: C:\WINDOWS\system32\svchost.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\System32\NPSMDesktopProvider.dll+1dc9f|C:\WINDOWS\System32\NPSMDesktopProvider.dll+18488|C:\WINDOWS\System32\NPSMDesktopProvider.dll+161e3|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1513","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.485
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 8632
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.dll+1869e|C:\WINDOWS\SYSTEM32\twinui.dll+3b1ac|C:\WINDOWS\SYSTEM32\twinui.dll+842d8|C:\WINDOWS\System32\shcore.dll+517bf|C:\WINDOWS\System32\shcore.dll+51734|C:\WINDOWS\System32\shcore.dll+d0ea|C:\WINDOWS\System32\combase.dll+ac22d|C:\WINDOWS\System32\combase.dll+ac1be|C:\WINDOWS\System32\combase.dll+ab256|C:\WINDOWS\System32\combase.dll+1726c7|C:\WINDOWS\System32\combase.dll+172141|C:\WINDOWS\System32\combase.dll+25d63|C:\WINDOWS\System32\combase.dll+1a18aa|C:\WINDOWS\System32\combase.dll+15cb76|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+d570e|C:\WINDOWS\System32\RPCRT4.dll+16c50|C:\WINDOWS\System32\combase.dll+8dc9d|C:\WINDOWS\System32\combase.dll+8dbdb|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1512","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.470
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 8632
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\Windows\System32\TWINAPI.dll+7587|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+32c50|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+31b38|C:\WINDOWS\SYSTEM32\twinui.dll+51e03|C:\WINDOWS\SYSTEM32\twinui.dll+acfb|C:\WINDOWS\SYSTEM32\twinui.dll+a92b|C:\WINDOWS\SYSTEM32\twinui.dll+51047|C:\WINDOWS\SYSTEM32\twinui.dll+1ecca|C:\WINDOWS\SYSTEM32\twinui.dll+1ec4c|C:\WINDOWS\System32\user32.dll+c396|C:\WINDOWS\System32\user32.dll+a7ed|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+3d4f|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+1727f|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+52ea1|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+52de9|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1511","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.468
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 19932
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\AppResolver.dll+31999|C:\WINDOWS\SYSTEM32\AppResolver.dll+2c30b|C:\WINDOWS\SYSTEM32\AppResolver.dll+2c639|C:\Windows\System32\Taskbar.dll+b7c39|C:\Windows\System32\Taskbar.dll+b7ab4|C:\Windows\System32\Taskbar.dll+6bcc9|C:\WINDOWS\System32\windows.storage.dll+b7892|C:\WINDOWS\System32\windows.storage.dll+32719e|C:\WINDOWS\System32\shcore.dll+4b385|C:\WINDOWS\SYSTEM32\ntdll.dll+6f9c2|C:\WINDOWS\SYSTEM32\ntdll.dll+240f0|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1510","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.468
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 8632
> SourceImage: C:\WINDOWS\explorer.exe

> **Prompt 62** (*2026-05-31 20:45:27*)
>
> Has everything been updated, in particular all the files from OS query and sysmon?

> **Prompt 63** (*2026-05-31 20:48:01*)
>
> Create one or more Mermaid diagrams to reflect component interactions, network communications, etc

> **Prompt 64** (*2026-05-31 20:51:30*)
>
> Convert the Mermaid diagrams to PNG files

> **Prompt 65** (*2026-05-31 20:53:39*)
>
> Is osqueryi.exe installed?

> **Prompt 66** (*2026-05-31 20:53:39*)
>
> find when my windows was last patched

> **Prompt 67** (*2026-05-31 20:53:39*)
>
> use osquery

> **Prompt 68** (*2026-05-31 20:53:39*)
>
> can you tell me all my installed software (using os query)

> **Prompt 69** (*2026-05-31 20:53:39*)
>
> Update @SOFTWARE.md and @PATH-HISTORY.md based on this information

> **Prompt 70** (*2026-05-31 20:53:39*)
>
> Let's explore running processes

> **Prompt 71** (*2026-05-31 20:53:39*)
>
> Can you give me more details about the network connections for each of these processes?

> **Prompt 72** (*2026-05-31 20:53:39*)
>
> What is the NVDIA Overlay and why does it need network communication

> **Prompt 73** (*2026-05-31 20:53:39*)
>
> have I installed any new software?

> **Prompt 74** (*2026-05-31 20:53:39*)
>
> Review the NVIDIA Connections

> **Prompt 75** (*2026-05-31 20:53:39*)
>
> Can you tell what files the overlay is accessing?

> **Prompt 76** (*2026-05-31 20:53:39*)
>
> Can you analyze @ow-network-traffic.pcapng

> **Prompt 77** (*2026-05-31 20:53:39*)
>
> Convert @ow-network-traffic.pcapng to a pdml using tshark

> **Prompt 78** (*2026-05-31 20:53:39*)
>
> Extract a thouesand packets into a new pdml file that we can use for testing

> **Prompt 79** (*2026-05-31 20:53:39*)
>
> Can you convert @ow-test.pdml to parquet using Python. Remember to use uv to install any new packages and create a venv.

> **Prompt 80** (*2026-05-31 20:53:39*)
>
> Capture what you did in @PDML.md, explaining what you did to convert it and why you did what you did

> **Prompt 81** (*2026-05-31 20:53:39*)
>
> Create python scripts to identify overwatch traffic patterns in @ow-network-traffic.parquet . Save the scripts to .py files

> **Prompt 82** (*2026-05-31 20:53:39*)
>
> Cannot display content of binary file: ow-network-traffic.parquet

> **Prompt 83** (*2026-05-31 20:53:39*)
>
> Can you look for DNS queries or TLS SNI to also identify more traffic

> **Prompt 84** (*2026-05-31 20:53:39*)
>
> Use the parquet

> **Prompt 85** (*2026-05-31 20:53:39*)
>
> That's great that you added those enrichments. Can we review the original file to see what additional protocol schemas that we should add to our parquet

> **Prompt 86** (*2026-05-31 20:53:39*)
>
> what have you found so far

> **Prompt 87** (*2026-05-31 20:53:39*)
>
> what do you remember about your current task

> **Prompt 88** (*2026-05-31 20:53:39*)
>
> Let's add QUIC and TLSv1.3 to our @pdml_to_parquet.py

> **Prompt 89** (*2026-05-31 20:53:39*)
>
> from lxml import etree
> import pandas as pd
> import sys
> 
> def parse_pdml(file_path):
>     print(f"Parsing {file_path}...")
>     context = etree.iterparse(file_path, events=('end',), tag='packet')
>     packets = []
>     
>     count = 0
>     for event, elem in context:
>         packet_data = {}
>         
>         # Basic info from geninfo and other protos
>         for proto in elem.findall('proto'):
>             proto_name = proto.get('name')
>             
>             # Frame number and length
>             if proto_name == 'geninfo':
>                 num = proto.find(".//field[@name='num']")
>                 if num is not None: packet_data['frame_number'] = num.get('show')
>                 
>                 ts = proto.find(".//field[@name='timestamp']")
>                 if ts is not None: packet_data['timestamp'] = ts.get('show')
>                 
>                 len_field = proto.find(".//field[@name='len']")
>                 if len_field is not None: packet_data['length'] = int(len_field.get('show'))
> 
>             # IP Addresses
>             elif proto_name == 'ip':
>                 src = proto.find(".//field[@name='ip.src']")
>                 if src is not None: packet_data['src_ip'] = src.get('show')
>                 
>                 dst = proto.find(".//field[@name='ip.dst']")
>                 if dst is not None: packet_data['dst_ip'] = dst.get('show')
>             
>             # IPv6 Addresses
>             elif proto_name == 'ipv6':
>                 src = proto.find(".//field[@name='ipv6.src']")
>                 if src is not None: packet_data['src_ip'] = src.get('show')
>                 
>                 dst = proto.find(".//field[@name='ipv6.dst']")
>                 if dst is not None: packet_data['dst_ip'] = dst.get('show')
> 
>             # DNS Queries
>             elif proto_name == 'dns':
>                 qry = proto.xpath(".//field[@name='dns.qry.name']")
>                 if qry:
>                     packet_data['dns_query'] = qry[0].get('show')
> 
>             # TLS SNI
>             elif proto_name == 'tls':
>                 sni = proto.xpath(".//field[@name='tls.handshake.extensions_server_name']")
>                 if sni:
>                     packet_data['tls_sni'] = sni[0].get('show')
> 
>             # Ports (TCP/UDP)
>             elif proto_name in ['tcp', 'udp']:
>                 packet_data['protocol'] = proto_name.upper()
>                 
>                 # Use xpath for robust field finding
>                 src_port_elem = proto.xpath(".//field[@name='tcp.srcport' or @name='udp.srcport']")
>                 if src_port_elem:
>                     packet_data['src_port'] = int(src_port_elem[0].get('show'))
>                 
>                 dst_port_elem = proto.xpath(".//field[@name='tcp.dstport' or @name='udp.dstport']")
>                 if dst_port_elem:
>                     packet_data['dst_port'] = int(dst_port_elem[0].get('show'))
> 
>         # If protocol not set by TCP/UDP, get the highest layer protocol name
>         if 'protocol' not in packet_data:
>             # Get the last proto that isn't geninfo, frame, or eth
>             protos = [p.get('name') for p in elem.findall('proto') if p.get('name') not in ['geninfo', 'frame', 'eth', 'ip', 'ipv6']]
>             if protos:
>                 packet_data['protocol'] = protos[-1].upper()
>             else:
>                 packet_data['protocol'] = 'OTHER'
> 
>         packets.append(packet_data)
>         count += 1
>         if count % 100 == 0:
>             print(f"Processed {count} packets...")
>         
>         # Clean up element to save memory
>         elem.clear()
>         while elem.getprevious() is not None:
>             del elem.getparent()[0]
>             
>     return pd.DataFrame(packets)
> 
> if __name__ == "__main__":
>     input_file = "D:/WindowsInvestigations/ow-network-traffic.pdml"
>     output_file = "D:/WindowsInvestigations/ow-network-traffic-enriched.parquet"
>     
>     df = parse_pdml(input_file)
>     print(f"Saving {len(df)} packets to {output_file}...")
>     df.to_parquet(output_file, engine='pyarrow')
>     print("Done!")

> **Prompt 90** (*2026-05-31 20:53:39*)
>
> Update @OVERWATCH.md with your findings

> **Prompt 91** (*2026-05-31 20:53:39*)
>
> Using osquery, what can you find out about overwatch

> **Prompt 92** (*2026-05-31 20:53:39*)
>
> I am now running the game. Look for process and network activity

> **Prompt 93** (*2026-05-31 20:53:39*)
>
> sure

> **Prompt 94** (*2026-05-31 20:53:39*)
>
> Add these findings to @OVERWATCH.md

> **Prompt 95** (*2026-05-31 20:53:39*)
>
> # Overwatch Network Investigation
> 
> Last Updated: 2026-05-31
> 
> This document summarizes the findings from the investigation of Overwatch and Blizzard-related network traffic using packet captures and system analysis.
> 
> ## 1. Core Infrastructure
> 
> Through DNS and TLS SNI analysis, we mapped the following key Blizzard endpoints:
> 
> | Service | Domain / Hostname | Identified IP(s) |
> | :--- | :--- | :--- |
> | **Gameplay** | (Direct UDP Traffic) | `24.105.60.145` |
> | **Match Ingestion** | `overwatch.ingest.gdp.blizzard.com` | `35.201.91.89` |
> | **Telemetry** | `telemetry-in.battle.net` | `137.221.105.136`, `137.221.105.232` |
> | **Authentication** | `oauth.battle.net`, `account.battle.net` | `100.20.157.63`, `52.38.105.79`, `34.210.233.116` |
> | **Content/CDN** | `us.version.battle.net`, `us.cdn.blizzard.com` | `136.110.188.211`, `137.221.64.x` |
> 
> ## 2. Traffic Signatures
> 
> ### Gameplay (UDP)
> - **Pattern:** High frequency of small packets (averaging ~100-200 bytes).
> - **Behavior:** Symmetrical flow between the local machine and Blizzard gameplay servers.
> 
> ### Control & Telemetry (Encrypted)
> - **Protocols:** Heavy usage of **TLSv1.3** and **QUIC**.
> - **QUIC Streams:** Identified distinct sessions via Destination Connection IDs (DCIDs). 
>     - *Example DCID:* `12:38:62:3c:38:80:80:2e` (500+ packets).
> - **TLS Ciphers:** Primarily uses `0x1302` (**TLS_AES_128_GCM_SHA256**), confirming modern encryption standards despite compatibility labels.
> 
> ## 3. Analysis Methodology
> 
> We used a custom-built pipeline to handle large-scale packet data:
> 1.  **Extraction:** Used `tshark` to convert `.pcapng` to `.pdml` (XML).
> 2.  **Conversion:** Developed `pdml_to_parquet.py`, a streaming Python parser using `lxml` to convert verbose XML into compressed **Parquet** files.
>     - *Result:* 1.6GB of XML was reduced to a manageable, queryable dataset.
> 3.  **Enrichment:** Extracted DNS queries, TLS SNI, TLS versions/ciphers, and QUIC metadata for correlation.
> 
> ## 4. System Context
> - **Last Patch:** May 26, 2026 (KB5078674).
> - **Environment:** Recent setup of Node.js and osquery indicates an active development/investigation session.
> - **Supporting Processes:** NVIDIA Overlay was found communicating locally with GPU drivers while maintaining its own encrypted cloud connections for settings and telemetry.
> 
> ---
> *Note: This data is derived from the `ow-network-traffic.pcapng` capture.*

> **Prompt 96** (*2026-05-31 20:53:39*)
>
> Correlate the osquery information with the wireshark data so we can see the full picture of which processes are communicating with which network destinations

> **Prompt 97** (*2026-05-31 20:53:39*)
>
> Add this to @OVERWATCH.md

> **Prompt 98** (*2026-05-31 20:53:39*)
>
> # Overwatch Network Investigation
> 
> Last Updated: 2026-05-31
> 
> This document summarizes the findings from the investigation of Overwatch and Blizzard-related network traffic using packet captures, live process monitoring, and system analysis.
> 
> ## 1. Core Infrastructure
> 
> Through combined analysis of static captures and live execution, we mapped the following Blizzard endpoints:
> 
> | Service | Domain / Hostname | Identified IP(s) |
> | :--- | :--- | :--- |
> | **Gameplay** | (Direct UDP Traffic) | `24.105.60.145`, `24.105.60.232` |
> | **Active Session** | (Blizzard/AWS) | **`34.182.236.194`** |
> | **Match Ingestion** | `overwatch.ingest.gdp.blizzard.com` | `35.201.91.89` |
> | **Telemetry** | `telemetry-in.battle.net` | `137.221.105.136`, `137.221.105.232` |
> | **Authentication** | `oauth.battle.net`, `account.battle.net` | `100.20.157.63`, `52.38.105.79`, `34.210.233.116` |
> | **Content/CDN** | `us.version.battle.net`, `us.cdn.blizzard.com` | `136.110.188.211`, `137.221.64.x` |
> 
> ## 2. Traffic Signatures
> 
> ### Gameplay & Control (UDP/TCP)
> - **Gameplay Signature:** High frequency of small UDP packets (averaging ~100-200 bytes).
> - **Game Service Port:** Live monitoring identified active communication on port **`3724`** (standard Blizzard Game Service port).
> - **`wow` Protocol:** `tshark` dissectors identified a subset of control traffic as the **`wow` (World of Warcraft/Blizzard)** protocol, used for game-state management.
> 
> ### Control & Telemetry (Encrypted)
> - **Protocols:** Heavy usage of **TLSv1.3** and **QUIC**.
> - **QUIC Streams:** Identified distinct sessions via Destination Connection IDs (DCIDs). 
> - **TLS Ciphers:** Primarily uses `0x1302` (**TLS_AES_128_GCM_SHA256**), confirming modern encryption standards despite compatibility labels.
> 
> ## 3. Live Execution Context
> 
> Monitoring the game in an active state revealed the following system metrics:
> - **Process:** `Overwatch.exe` (started with `-uid prometheus`).
> - **Memory Footprint:** Significant resource usage, stabilizing at **~8.9 GB**.
> - **Supporting Ecosystem:** `Battle.net.exe` and `Agent.exe` maintain multiple established telemetry and update connections (port 443) while the game is running.
> 
> ## 4. Analysis Methodology
> 
> We used a custom-built pipeline to handle large-scale packet data:
> 1.  **Extraction:** Used `tshark` to convert `.pcapng` to `.pdml` (XML).
> 2.  **Conversion:** Developed `pdml_to_parquet.py`, a streaming Python parser using `lxml` to convert verbose XML into compressed **Parquet** files.
>     - *Result:* 1.6GB of XML was reduced to a manageable, queryable dataset.
> 3.  **Enrichment:** Extracted DNS queries, TLS SNI, TLS versions/ciphers, and QUIC metadata for correlation.
> 4.  **Live Validation:** Performed a live capture (`ow-live-sample.pcapng`) to verify infrastructure and identify active session IPs.
> 
> ---
> *Note: This data is derived from the `ow-network-traffic.pcapng` capture and live system state as of May 31, 2026.*

> **Prompt 99** (*2026-05-31 20:53:39*)
>
> I have run sysmon and extracted during a short session of Overwatch in @sysmon-overwatch-session.csv. Correlate with existing data.

> **Prompt 100** (*2026-05-31 20:53:39*)
>
> [WARNING: This file was truncated. To view the full content, use the 'read_file' tool on this specific file.]
> 
> "Message","Id","Version","Qualifiers","Level","Task","Opcode","Keywords","RecordId","ProviderName","ProviderId","LogName","ProcessId","ThreadId","MachineName","UserId","TimeCreated","ActivityId","RelatedActivityId","ContainerLog","MatchedQueryIds","Bookmark","LevelDisplayName","OpcodeDisplayName","TaskDisplayName","KeywordsDisplayNames","Properties"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:21.383
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1657","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:21 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:21.351
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\Agent.9464\Logs\Telemetry-MessageStats-20260531T203409.log
> CreationUtcTime: 2026-05-31 20:36:21.351
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1656","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:21 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:18.121
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\product.db.new
> CreationUtcTime: 2026-05-31 20:36:00.986
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1655","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:18 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:17.807
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\aggregate.json
> CreationUtcTime: 2026-05-26 05:21:27.424
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1654","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:17 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:14.959
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1653","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.959
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 6380
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea60b|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a30fe|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a5678|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+694380|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6ed19a|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6cbe88|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a7ba5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a48ae|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a4e87|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d4b68|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87478|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87363|C:\WINDOWS\SYSTEM32\ntdll.dll+23080|C:\WINDOWS\SYSTEM32\ntdll.dll+240d1|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1652","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.959
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1651","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.923
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 6380
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea60b|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a30fe|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a5678|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+694380|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6ed19a|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6cbe88|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a7ba5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a48ae|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a4e87|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d4b68|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87478|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87363|C:\WINDOWS\SYSTEM32\ntdll.dll+23080|C:\WINDOWS\SYSTEM32\ntdll.dll+240d1|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1650","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.923
> ProcessGuid: {f162fe7e-9b56-6a1c-0251-000000000900}
> ProcessId: 27488
> Image: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1649","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:14.921
> ProcessGuid: {f162fe7e-9b56-6a1c-0251-000000000900}
> ProcessId: 27488
> Image: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> ImageLoaded: C:\Windows\System32\kernel.appcore.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: AppModel API Host
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: kernel.appcore.dll
> Hashes: MD5=65800310E00B24D50F743F7C771E53BF,SHA256=E47C8F31C70A91AAF199CAAB2338896D6DF86B2EE4E64D6F274B698223DFDC98,IMPHASH=066FFFA45EF798520DE9BAA65A2B842C
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1648","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:14 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:13.776
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1647","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:13 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:13.776
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1646","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:13 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.733
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\mfcore.dll
> FileVersion: 10.0.26100.8457 (WinBuild.160101.0800)
> Description: Media Foundation Core DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: mfcore.dll
> Hashes: MD5=CEC4D20C64C01C79599534DC707E2757,SHA256=7013064E8E28AF30C112421745309966FD9223C7F8B9009C9E5F730EF1069F20,IMPHASH=3A94DB83E3B4FB80067B95BD968A8FDA
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1645","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.703
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\mfreadwrite.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: Media Foundation ReadWrite DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: mfreadwrite.dll
> Hashes: MD5=0541E513C50E55899FBB8A68FB90B9B8,SHA256=650A295DB62D5063BAAF81BD1E79278B39B4820DD48C80720B885C4302D5F79B,IMPHASH=36FA6935F2A7B5813A2A9B94E71F0303
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1644","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.707
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1643","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.707
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1642","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.695
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\RTWorkQ.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: Realtime WorkQueue DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: RTWorkQ.dll
> Hashes: MD5=DC5051E80CF552032ADAA0740FA59C3D,SHA256=63FDDAD8759720F0AA43FC15C466BB74B52593F7CE5980829CA4BA92D3B10A71,IMPHASH=163F592AB493FBB3AC3448DC8A20F69A
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1641","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.706
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 15944
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea60b|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a30fe|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a5678|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6933cf|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6ed19a|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6cbe88|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a7ba5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a48ae|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a4e87|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d4b68|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87478|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87363|C:\WINDOWS\SYSTEM32\ntdll.dll+23080|C:\WINDOWS\SYSTEM32\ntdll.dll+240d1|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1640","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.690
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\mfplat.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: Media Foundation Platform DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: mfplat.dll
> Hashes: MD5=6390028C7C457B7F914C98AA3B937B53,SHA256=43C897A3C4190644EEAD791EA82B1503CC26F597D36B5A2CE6AF1C029584C046,IMPHASH=8E87A39D335960D7F555429CE77476BA
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1639","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.696
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1638","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Image loaded:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.674
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> ImageLoaded: C:\Windows\System32\mf.dll
> FileVersion: 10.0.26100.8328 (WinBuild.160101.0800)
> Description: Media Foundation DLL
> Product: Microsoft? Windows? Operating System
> Company: Microsoft Corporation
> OriginalFileName: mf.dll
> Hashes: MD5=CEE73D01E8BEACAC4D198A5685C5708C,SHA256=4462ADC94833D295193A704850D697D8D51066BC127686232E2A51F33BE358F5,IMPHASH=C2DAA55E55F79F6858A11E283694053A
> Signed: true
> Signature: Microsoft Windows
> SignatureStatus: Valid
> User: Panda-PC\annac","7","3",,"4","7","0","-9223372036854775808","1637","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","15132","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:12.671
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 15944
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea60b|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a30fe|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a5678|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6933cf|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6ed19a|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6cbe88|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a7ba5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a48ae|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6a4e87|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d4b68|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87478|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+87363|C:\WINDOWS\SYSTEM32\ntdll.dll+23080|C:\WINDOWS\SYSTEM32\ntdll.dll+240d1|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1636","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:12 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.564
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d5cdc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9b8b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1635","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.429
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1634","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.429
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1633","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.418
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1632","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:10.074
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\product.db.new
> CreationUtcTime: 2026-05-31 20:36:00.986
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1631","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:10 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:09.767
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1630","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:09 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:09.767
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1629","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:09 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:07.696
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1628","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:07 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:07.696
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1627","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:07 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:07.685
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1626","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:07 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:05.769
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1625","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:05 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:05.769
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1624","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:05 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:05.565
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d5cdc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9b8b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1623","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:05 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:02.689
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1622","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:02.689
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1621","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:02.676
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1620","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.694
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: false
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50528
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1619","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.694
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50528
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1618","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:36:02 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.754
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1617","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.754
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1616","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:01.108
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1615","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.107
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1614","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.070
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Roaming\Battle.net\Battle.net.config
> CreationUtcTime: 2026-05-26 05:23:00.710
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1613","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:01.069
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Roaming\Battle.net\15ec9a85.config
> CreationUtcTime: 2026-05-26 05:24:15.911
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1612","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:01 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.986
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> TargetFilename: C:\ProgramData\Battle.net\Agent\product.db.new
> CreationUtcTime: 2026-05-31 20:36:00.986
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1611","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.671
> ProcessGuid: {f162fe7e-9b42-6a1c-db50-000000000900}
> ProcessId: 16276
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1610","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.671
> ProcessGuid: {f162fe7e-9b42-6a1c-db50-000000000900}
> ProcessId: 16276
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1609","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.639
> ProcessGuid: {f162fe7e-9b42-6a1c-dc50-000000000900}
> ProcessId: 11524
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1608","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.639
> ProcessGuid: {f162fe7e-9b42-6a1c-dc50-000000000900}
> ProcessId: 11524
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1607","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.629
> ProcessGuid: {f162fe7e-9b42-6a1c-dd50-000000000900}
> ProcessId: 18772
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1606","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.629
> ProcessGuid: {f162fe7e-9b42-6a1c-dd50-000000000900}
> ProcessId: 18772
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1605","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.556
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d5cdc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9b8b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1604","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.435
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1603","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.435
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1602","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.423
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0FE7CEA)|UNKNOWN(00007FF7E0A537CF)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1601","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.094
> ProcessGuid: {f162fe7e-9b42-6a1c-dd50-000000000900}
> ProcessId: 18772
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\BrowserCaches\367827589\Network\Network Persistent State~RFf89bc1c.TMP
> CreationUtcTime: 2026-05-31 20:36:00.094
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1600","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.082
> ProcessGuid: {f162fe7e-9b4d-6a1c-f150-000000000900}
> ProcessId: 20388
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1599","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.082
> ProcessGuid: {f162fe7e-9b4d-6a1c-f150-000000000900}
> ProcessId: 20388
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1598","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.072
> ProcessGuid: {f162fe7e-9b42-6a1c-dd50-000000000900}
> ProcessId: 18772
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\BrowserCaches\367827589\Network\db1b5eea-716d-424a-8214-6bb1ebbb8809.tmp
> CreationUtcTime: 2026-05-31 20:36:00.072
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1597","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.022
> ProcessGuid: {f162fe7e-9b46-6a1c-ef50-000000000900}
> ProcessId: 13400
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1596","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.014
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\CachedData.db-journal
> CreationUtcTime: 2026-05-31 20:35:59.985
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1595","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.012
> ProcessGuid: {f162fe7e-9b46-6a1c-ef50-000000000900}
> ProcessId: 13400
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1594","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:36:00.004
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\CachedData.db-journal
> CreationUtcTime: 2026-05-31 20:35:59.985
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1593","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:36:00.000
> ProcessGuid: {f162fe7e-9b4e-6a1c-f350-000000000900}
> ProcessId: 30404
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1592","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:35:59.999
> ProcessGuid: {f162fe7e-9b4e-6a1c-f350-000000000900}
> ProcessId: 30404
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1591","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:35:59.999
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\CachedData.db-journal
> CreationUtcTime: 2026-05-31 20:35:59.985
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1590","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Registry value set:
> RuleName: -
> EventType: SetValue
> UtcTime: 2026-05-31 20:35:59.999
> ProcessGuid: {f162fe7e-9b45-6a1c-e150-000000000900}
> ProcessId: 28220
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetObject: HKLM\System\CurrentControlSet\Services\bam\State\UserSettings\S-1-5-21-1352990077-2347519038-4138506755-1001\\Device\HarddiskVolume5\Program Files (x86)\Battle.net\Battle.net.exe
> Details: Binary Data
> User: Panda-PC\annac","13","2",,"4","13","0","-9223372036854775808","1589","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:36:00 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process terminated:
> RuleName: -
> UtcTime: 2026-05-31 20:35:59.996
> ProcessGuid: {f162fe7e-9b45-6a1c-e150-000000000900}
> ProcessId: 28220
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac","5","3",,"4","5","0","-9223372036854775808","1588","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:58.438
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: false
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50527
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1587","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:58.438
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50527
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1586","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.954
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50521
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1585","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50516
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1584","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50525
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1583","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50523
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1582","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50517
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1581","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50524
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1580","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50519
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1579","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50522
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1578","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50520
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1577","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50518
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1576","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.952
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50526
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1575","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.950
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50515
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1574","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.950
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50513
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1573","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.950
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50514
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1572","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.949
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 50512
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 35.201.91.89
> DestinationHostname: 89.91.201.35.bc.googleusercontent.com
> DestinationPort: 443
> DestinationPortName: https","3","5",,"4","3","0","-9223372036854775808","1571","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:35:59.985
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> TargetFilename: C:\Users\annac\AppData\Local\Battle.net\CachedData.db-journal
> CreationUtcTime: 2026-05-31 20:35:59.985
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1570","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Dns query:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.870
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> QueryName: overwatch.ingest.gdp.blizzard.com
> QueryStatus: 0
> QueryResults: ::ffff:35.201.91.89;
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac","22","5",,"4","22","0","-9223372036854775808","1569","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","28092","Panda-PC","S-1-5-18","5/31/2026 4:35:59 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.971
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1568","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.970
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1567","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.969
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1566","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.969
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1565","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.968
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1564","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.963
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1563","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.963
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1562","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.961
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1561","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.960
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1560","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.959
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1559","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.956
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1558","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.955
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1557","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.955
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1556","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.951
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1555","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.950
> SourceProcessGUID: {f162fe7e-a179-6a18-0c00-000000000900}
> SourceProcessId: 1152
> SourceThreadId: 1632
> SourceImage: C:\WINDOWS\system32\lsass.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\schannel.DLL+7bacb|C:\WINDOWS\system32\schannel.DLL+2b2e0|C:\WINDOWS\system32\schannel.DLL+2b00a|C:\WINDOWS\system32\lsasrv.dll+240d2|C:\WINDOWS\system32\lsasrv.dll+22ad7|C:\WINDOWS\SYSTEM32\SspiSrv.dll+1687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d36a3|C:\WINDOWS\SYSTEM32\RPCRT4.dll+d570e|C:\WINDOWS\SYSTEM32\RPCRT4.dll+8a77c|C:\WINDOWS\SYSTEM32\RPCRT4.dll+88687|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4da74|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4ea88|C:\WINDOWS\SYSTEM32\RPCRT4.dll+3bc14|C:\WINDOWS\SYSTEM32\RPCRT4.dll+4bfdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51fdc|C:\WINDOWS\SYSTEM32\RPCRT4.dll+51163|C:\WINDOWS\SYSTEM32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1554","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File Delete archived:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.773
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> User: Panda-PC\annac
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetFilename: C:\Users\annac\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini_LOCK
> Hashes: MD5=0D542CD521BEA05A4C3D12EE43FD332C,SHA256=B653C87B7FCA89E0005891743B9F60F83254830C940C8FF0A3A9DC24BB419D24,IMPHASH=00000000000000000000000000000000
> IsExecutable: false
> Archived: true","23","5",,"4","23","0","-9223372036854775808","1553","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Error report:
> UtcTime: 2026-05-31 20:35:57.773
> ID: FILE_DELETE
> Description: The ""C:\Sysmon\"" owner is not System. Archiving is disabled.","255","3",,"2","255","0","-9223372036854775808","1552","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Error","Info",,"System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.772
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetFilename: C:\Users\annac\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini
> CreationUtcTime: 2026-05-26 03:17:19.616
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1551","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File Delete archived:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.772
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> User: Panda-PC\annac
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetFilename: C:\Users\annac\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini
> Hashes: MD5=F5816CE03EDED4C63D23E7D4DEAB84C8,SHA256=AE457B305A292DFAB7F454F7062FEC9CA59985AF6DF1D40803744E2A1F0C109A,IMPHASH=00000000000000000000000000000000
> IsExecutable: false
> Archived: true","23","5",,"4","23","0","-9223372036854775808","1550","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Error report:
> UtcTime: 2026-05-31 20:35:57.772
> ID: FILE_DELETE
> Description: The ""C:\Sysmon\"" owner is not System. Archiving is disabled.","255","3",,"2","255","0","-9223372036854775808","1549","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Error","Info",,"System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "File created:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.770
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> TargetFilename: C:\Users\annac\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini_LOCK
> CreationUtcTime: 2026-05-31 20:35:57.770
> User: Panda-PC\annac","11","2",,"4","11","0","-9223372036854775808","1548","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.750
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1547","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.750
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1546","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.677
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1545","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.676
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1544","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:57.664
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1543","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:57 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.724
> ProcessGuid: {f162fe7e-9b51-6a1c-f450-000000000900}
> ProcessId: 21876
> Image: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> User: Panda-PC\annac
> Protocol: udp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 192.168.12.232
> SourceHostname: Panda-PC.lan
> SourcePort: 4242
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 224.0.0.5
> DestinationHostname: ospf-all.mcast.net
> DestinationPort: 4242
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1542","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:56 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.437
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: false
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50511
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1541","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:56 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.437
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50511
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1540","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:56 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.539
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d5cdc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9b8b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1539","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.536
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130608|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+1304d5|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d9761|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1538","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.528
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+da773|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d95cc|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1537","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.526
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 24016
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d95a7|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+d831|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+263d250|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+2639be6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13de20|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+13ed5a|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+16ca9f|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1536","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:55.498
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 12116
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d97dc|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa096|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f2498|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa934|C:\WINDOWS\SYSTEM32\sechost.dll+4208|C:\WINDOWS\SYSTEM32\sechost.dll+29af|C:\WINDOWS\SYSTEM32\sechost.dll+23207|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f43e5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+17d27f|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1535","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:55 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:54.478
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 12116
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d97dc|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa096|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f2498|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa934|C:\WINDOWS\SYSTEM32\sechost.dll+4208|C:\WINDOWS\SYSTEM32\sechost.dll+29af|C:\WINDOWS\SYSTEM32\sechost.dll+23207|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f43e5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+17d27f|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1534","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:54 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:53.751
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1533","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:53 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:53.751
> SourceProcessGUID: {f162fe7e-9b41-6a1c-da50-000000000900}
> SourceProcessId: 28480
> SourceThreadId: 12404
> SourceImage: C:\WINDOWS\system32\wbem\wmiprvse.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\system32\wbem\cimwin32.dll+12816|C:\WINDOWS\system32\wbem\cimwin32.dll+1204d|C:\WINDOWS\SYSTEM32\framedynos.dll+f51a|C:\WINDOWS\SYSTEM32\framedynos.dll+ead5|C:\WINDOWS\system32\wbem\wmiprvse.exe+2b00f|C:\WINDOWS\system32\wbem\wmiprvse.exe+2a25f|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+174bd|C:\WINDOWS\System32\combase.dll+8dcff|C:\WINDOWS\System32\RPCRT4.dll+68cd6|C:\WINDOWS\System32\combase.dll+8dbe2|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f|C:\WINDOWS\System32\combase.dll+4872a|C:\WINDOWS\System32\combase.dll+4ab0c|C:\WINDOWS\System32\combase.dll+53bcf|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4e83a|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc
> SourceUser: NT AUTHORITY\NETWORK SERVICE
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1532","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:53 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.426
> ProcessGuid: {f162fe7e-9b41-6a1c-d850-000000000900}
> ProcessId: 18708
> Image: C:\ProgramData\Battle.net\Agent\Agent.9464\Agent.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: false
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50510
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1531","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:53 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Network connection detected:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.426
> ProcessGuid: {f162fe7e-9b3f-6a1c-d650-000000000900}
> ProcessId: 29036
> Image: C:\Program Files (x86)\Battle.net\Battle.net.exe
> User: Panda-PC\annac
> Protocol: tcp
> Initiated: true
> SourceIsIpv6: false
> SourceIp: 127.0.0.1
> SourceHostname: Panda-PC
> SourcePort: 50510
> SourcePortName: -
> DestinationIsIpv6: false
> DestinationIp: 127.0.0.1
> DestinationHostname: Panda-PC
> DestinationPort: 64517
> DestinationPortName: -","3","5",,"4","3","0","-9223372036854775808","1530","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","2376","Panda-PC","S-1-5-18","5/31/2026 4:35:53 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.647
> SourceProcessGUID: {f162fe7e-83ca-6a1c-0842-000000000900}
> SourceProcessId: 1388
> SourceThreadId: 25024
> SourceImage: C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+12ef68|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130163|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130742|C:\WINDOWS\System32\USER32.dll+3d2d6|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+130701|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+284bd|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95e7b|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95f99|\\?\C:\Users\annac\AppData\Local\Discord\app-1.0.9239\modules\discord_utils-1\discord_utils\discord_utils.node+95d47|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+54ad94|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cd2129|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3d0cee0|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3cbad73|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+f6b198|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+3e1dfb|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+442eab4|UNKNOWN(00007FF7E0E712F0)|UNKNOWN(00007FF7E0F89A8A)|UNKNOWN(00007FF7E0FFC12A)|UNKNOWN(00007FF7E0FB8DC3)|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+4429a9c|C:\Users\annac\AppData\Local\Discord\app-1.0.9239\Discord.exe+44295ff
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1529","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:52 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.446
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 12116
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d97dc|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa096|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f2498|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa934|C:\WINDOWS\SYSTEM32\sechost.dll+4208|C:\WINDOWS\SYSTEM32\sechost.dll+29af|C:\WINDOWS\SYSTEM32\sechost.dll+23207|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f43e5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+17d27f|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1528","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:52 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:52.446
> SourceProcessGUID: {f162fe7e-a17a-6a18-5600-000000000900}
> SourceProcessId: 4724
> SourceThreadId: 12116
> SourceImage: C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.26040.7-0\MsMpEng.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\SYSTEM32\KERNELBASE.dll+360c6|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+2ea868|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6d97dc|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa096|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f2498|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6fa934|C:\WINDOWS\SYSTEM32\sechost.dll+4208|C:\WINDOWS\SYSTEM32\sechost.dll+29af|C:\WINDOWS\SYSTEM32\sechost.dll+23207|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+6f43e5|C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{606E65FA-749B-411F-82E3-19696275586E}\mpengine.dll+17d27f|C:\WINDOWS\SYSTEM32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1527","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:52 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.984
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 8632
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\Windows\System32\TWINAPI.dll+7587|C:\WINDOWS\SYSTEM32\twinui.dll+156d6|C:\WINDOWS\SYSTEM32\twinui.dll+2cb173|C:\WINDOWS\SYSTEM32\twinui.dll+2ca4e2|C:\WINDOWS\System32\user32.dll+3d2d6|C:\WINDOWS\SYSTEM32\twinui.dll+2ca451|C:\WINDOWS\SYSTEM32\twinui.dll+37af6|C:\WINDOWS\SYSTEM32\twinui.dll+35fec|C:\WINDOWS\SYSTEM32\twinui.dll+3781d|C:\WINDOWS\SYSTEM32\twinui.dll+51e03|C:\WINDOWS\SYSTEM32\twinui.dll+acfb|C:\WINDOWS\SYSTEM32\twinui.dll+a92b|C:\WINDOWS\SYSTEM32\twinui.dll+51047|C:\WINDOWS\SYSTEM32\twinui.dll+1ecca|C:\WINDOWS\SYSTEM32\twinui.dll+1ec4c|C:\WINDOWS\System32\user32.dll+c396|C:\WINDOWS\System32\user32.dll+a7ed|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+3d4f|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+1727f|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+52ea1|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+52de9|C:\WINDOWS\System32\KERNEL32.DLL+2e957
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1526","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.524
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1525","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.517
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1524","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.517
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1523","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.516
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1522","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.515
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1521","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.515
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1520","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.514
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1519","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.514
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1518","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.508
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+312b24|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+1cf2c0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7337|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1517","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.507
> SourceProcessGUID: {f162fe7e-a179-6a18-0d00-000000000900}
> SourceProcessId: 1288
> SourceThreadId: 13344
> SourceImage: C:\WINDOWS\system32\svchost.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+983e|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+9a15|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+a0f0|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+8c35|C:\WINDOWS\SYSTEM32\resourcepolicyserver.dll+6e8c|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+d570e|C:\WINDOWS\System32\RPCRT4.dll+8a77c|C:\WINDOWS\System32\RPCRT4.dll+88687|C:\WINDOWS\System32\RPCRT4.dll+4da74|C:\WINDOWS\System32\RPCRT4.dll+4ea88|C:\WINDOWS\System32\RPCRT4.dll+3bc14|C:\WINDOWS\System32\RPCRT4.dll+4bfdc|C:\WINDOWS\System32\RPCRT4.dll+51fdc|C:\WINDOWS\System32\RPCRT4.dll+51163|C:\WINDOWS\System32\RPCRT4.dll+50108|C:\WINDOWS\SYSTEM32\ntdll.dll+25d0e|C:\WINDOWS\SYSTEM32\ntdll.dll+23e33|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: NT AUTHORITY\SYSTEM
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1516","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.505
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b56-6a1c-0251-000000000900}
> TargetProcessId: 27488
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\ErrorReporting\x64\CrashMailer_64.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5ec48|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a5dd0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7326|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1515","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.505
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 23164
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5ec48|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a5dd0|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+a7326|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+22598f|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+5b683|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1514","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.485
> SourceProcessGUID: {f162fe7e-83df-6a1c-6442-000000000900}
> SourceProcessId: 6844
> SourceThreadId: 28972
> SourceImage: C:\WINDOWS\system32\svchost.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\System32\NPSMDesktopProvider.dll+1dc9f|C:\WINDOWS\System32\NPSMDesktopProvider.dll+18488|C:\WINDOWS\System32\NPSMDesktopProvider.dll+161e3|C:\WINDOWS\System32\shcore.dll+a6d6|C:\WINDOWS\System32\shcore.dll+a40a|C:\WINDOWS\System32\shcore.dll+97a7|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1513","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.485
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 8632
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\twinui.dll+1869e|C:\WINDOWS\SYSTEM32\twinui.dll+3b1ac|C:\WINDOWS\SYSTEM32\twinui.dll+842d8|C:\WINDOWS\System32\shcore.dll+517bf|C:\WINDOWS\System32\shcore.dll+51734|C:\WINDOWS\System32\shcore.dll+d0ea|C:\WINDOWS\System32\combase.dll+ac22d|C:\WINDOWS\System32\combase.dll+ac1be|C:\WINDOWS\System32\combase.dll+ab256|C:\WINDOWS\System32\combase.dll+1726c7|C:\WINDOWS\System32\combase.dll+172141|C:\WINDOWS\System32\combase.dll+25d63|C:\WINDOWS\System32\combase.dll+1a18aa|C:\WINDOWS\System32\combase.dll+15cb76|C:\WINDOWS\System32\RPCRT4.dll+d36a3|C:\WINDOWS\System32\RPCRT4.dll+d570e|C:\WINDOWS\System32\RPCRT4.dll+16c50|C:\WINDOWS\System32\combase.dll+8dc9d|C:\WINDOWS\System32\combase.dll+8dbdb|C:\WINDOWS\System32\combase.dll+8d156|C:\WINDOWS\System32\combase.dll+8c468|C:\WINDOWS\System32\combase.dll+d964f
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1512","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.470
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 8632
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1000
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\Windows\System32\TWINAPI.dll+7587|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+32c50|C:\WINDOWS\SYSTEM32\twinui.pcshell.dll+31b38|C:\WINDOWS\SYSTEM32\twinui.dll+51e03|C:\WINDOWS\SYSTEM32\twinui.dll+acfb|C:\WINDOWS\SYSTEM32\twinui.dll+a92b|C:\WINDOWS\SYSTEM32\twinui.dll+51047|C:\WINDOWS\SYSTEM32\twinui.dll+1ecca|C:\WINDOWS\SYSTEM32\twinui.dll+1ec4c|C:\WINDOWS\System32\user32.dll+c396|C:\WINDOWS\System32\user32.dll+a7ed|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+3d4f|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+1727f|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+52ea1|C:\Windows\System32\windows.immersiveshell.serviceprovider.dll+52de9|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1511","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.468
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 19932
> SourceImage: C:\WINDOWS\explorer.exe
> TargetProcessGUID: {f162fe7e-9b51-6a1c-f450-000000000900}
> TargetProcessId: 21876
> TargetImage: C:\Program Files (x86)\Overwatch\_retail_\Overwatch.exe
> GrantedAccess: 0x1410
> CallTrace: C:\WINDOWS\SYSTEM32\ntdll.dll+162164|C:\WINDOWS\System32\KERNELBASE.dll+360c6|C:\WINDOWS\SYSTEM32\AppResolver.dll+31999|C:\WINDOWS\SYSTEM32\AppResolver.dll+2c30b|C:\WINDOWS\SYSTEM32\AppResolver.dll+2c639|C:\Windows\System32\Taskbar.dll+b7c39|C:\Windows\System32\Taskbar.dll+b7ab4|C:\Windows\System32\Taskbar.dll+6bcc9|C:\WINDOWS\System32\windows.storage.dll+b7892|C:\WINDOWS\System32\windows.storage.dll+32719e|C:\WINDOWS\System32\shcore.dll+4b385|C:\WINDOWS\SYSTEM32\ntdll.dll+6f9c2|C:\WINDOWS\SYSTEM32\ntdll.dll+240f0|C:\WINDOWS\System32\KERNEL32.DLL+2e957|C:\WINDOWS\SYSTEM32\ntdll.dll+427c
> SourceUser: Panda-PC\annac
> TargetUser: Panda-PC\annac","10","3",,"4","10","0","-9223372036854775808","1510","Microsoft-Windows-Sysmon","5770385f-c22a-43e0-bf4c-06f5698ffbd9","Microsoft-Windows-Sysmon/Operational","2384","6920","Panda-PC","S-1-5-18","5/31/2026 4:35:51 PM",,,"Microsoft-Windows-Sysmon/Operational","System.UInt32[]","System.Diagnostics.Eventing.Reader.EventBookmark","Information","Info","Process terminated (rule: ProcessTerminate)","System.Collections.ObjectModel.ReadOnlyCollection`1[System.String]","System.Collections.Generic.List`1[System.Diagnostics.Eventing.Reader.EventProperty]"
> "Process accessed:
> RuleName: -
> UtcTime: 2026-05-31 20:35:51.468
> SourceProcessGUID: {f162fe7e-83d0-6a1c-2442-000000000900}
> SourceProcessId: 8124
> SourceThreadId: 8632
> SourceImage: C:\WINDOWS\explorer.exe

> **Prompt 101** (*2026-05-31 20:53:39*)
>
> Has everything been updated, in particular all the files from OS query and sysmon?

> **Prompt 102** (*2026-05-31 20:53:39*)
>
> Create one or more Mermaid diagrams to reflect component interactions, network communications, etc

> **Prompt 103** (*2026-05-31 20:53:39*)
>
> Convert the Mermaid diagrams to PNG files

---

