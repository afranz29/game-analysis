from lxml import etree
import pandas as pd
import sys

def parse_pdml(file_path):
    print(f"Parsing {file_path}...")
    context = etree.iterparse(file_path, events=('end',), tag='packet')
    packets = []

    count = 0
    for event, elem in context:
        packet_data = {}

        # Basic info from geninfo and other protos
        for proto in elem.findall('proto'):
            proto_name = proto.get('name')

            # Frame number and length
            if proto_name == 'geninfo':
                num = proto.find(".//field[@name='num']")
                if num is not None: packet_data['frame_number'] = num.get('show')

                ts = proto.find(".//field[@name='timestamp']")
                if ts is not None: packet_data['timestamp'] = ts.get('show')

                len_field = proto.find(".//field[@name='len']")
                if len_field is not None: packet_data['length'] = int(len_field.get('show'))

            # IP Addresses
            elif proto_name == 'ip':
                src = proto.find(".//field[@name='ip.src']")
                if src is not None: packet_data['src_ip'] = src.get('show')

                dst = proto.find(".//field[@name='ip.dst']")
                if dst is not None: packet_data['dst_ip'] = dst.get('show')

            # IPv6 Addresses
            elif proto_name == 'ipv6':
                src = proto.find(".//field[@name='ipv6.src']")
                if src is not None: packet_data['src_ip'] = src.get('show')

                dst = proto.find(".//field[@name='ipv6.dst']")
                if dst is not None: packet_data['dst_ip'] = dst.get('show')

            # Ports (TCP/UDP)
            elif proto_name in ['tcp', 'udp']:
                packet_data['protocol'] = proto_name.upper()

                # Use xpath for robust field finding
                src_port_elem = proto.xpath(".//field[@name='tcp.srcport' or @name='udp.srcport']")
                if src_port_elem:
                    packet_data['src_port'] = int(src_port_elem[0].get('show'))

                dst_port_elem = proto.xpath(".//field[@name='tcp.dstport' or @name='udp.dstport']")
                if dst_port_elem:
                    packet_data['dst_port'] = int(dst_port_elem[0].get('show'))

        # If protocol not set by TCP/UDP, get the highest layer protocol name
        if 'protocol' not in packet_data:
            # Get the last proto that isn't geninfo, frame, or eth
            protos = [p.get('name') for p in elem.findall('proto') if p.get('name') not in ['geninfo', 'frame', 'eth', 'ip', 'ipv6']]
            if protos:
                packet_data['protocol'] = protos[-1].upper()
            else:
                packet_data['protocol'] = 'OTHER'

        packets.append(packet_data)
        count += 1
        if count % 1000 == 0:
            print(f"Processed {count} packets...")

        # Clean up element to save memory
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]

    return pd.DataFrame(packets)

if __name__ == "__main__":
    input_file = "D:/WindowsInvestigations/ow-network-traffic.pdml"
    output_file = "D:/WindowsInvestigations/ow-network-traffic.parquet"

    df = parse_pdml(input_file)
    print(f"Saving {len(df)} packets to {output_file}...")
    df.to_parquet(output_file, engine='pyarrow')
    print("Done!")
    print(f"Total packets converted: {len(df)}")
