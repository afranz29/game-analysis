# PDML to Parquet Conversion Workflow

This document outlines the process and rationale for converting Wireshark PDML (Packet Details Markup Language) exports into the Parquet format for efficient data analysis.

## Overview

Working with raw packet captures in XML format (PDML) presents significant challenges due to the extreme file size expansion. For example, a ~25MB `.pcapng` file expanded to a **1.62GB** `.pdml` file. To solve this, we converted the data to **Parquet**, a columnar storage format, which reduced the 50MB test PDML down to just **24KB**.

## Conversion Process

### 1. Data Extraction
We first extracted a smaller subset of packets to validate the conversion logic:
```powershell
# Extract first 1000 packets
tshark -r ow-network-traffic.pcapng -c 1000 -T pdml > ow-test.pdml
```

### 2. Environment Setup
We used `uv` for fast, isolated dependency management:
```powershell
uv venv .venv
.\.venv\Scripts\activate
uv pip install pandas pyarrow lxml
```

### 3. Streaming Parser (`pdml_to_parquet.py`)
The conversion script was designed with the following priorities:
- **Memory Efficiency:** Used `lxml.etree.iterparse` to stream the XML. By calling `elem.clear()` and removing previous siblings during iteration, we keep the memory footprint constant regardless of the input file size.
- **Robustness:** Switched from standard `xml.etree` to `lxml` to better handle encoding declarations and complex XPaths.
- **Protocol Awareness:** Implemented logic to extract IPv4/IPv6 addresses and TCP/UDP ports, defaulting to the highest-layer protocol name for non-transport packets (e.g., ARP, ICMP).

## Rationale: Why Parquet?

| Feature | PDML (XML) | Parquet |
| :--- | :--- | :--- |
| **Storage** | Very Large (Text/Verbose) | Highly Compressed (Columnar) |
| **Loading** | Slow (requires full parsing) | Fast (supports partial reads) |
| **Analysis** | Difficult (Nested structure) | Native to Pandas/Polars/SQL |
| **Scalability** | Poor (Memory intensive) | Excellent (Disk-based) |

## Usage
The conversion script `pdml_to_parquet.py` can be pointed at the full 1.6GB file to generate a production-ready dataset for deep traffic analysis.
