from pcapfile import savefile

packets_file = "packets.pcap"

with open(packets_file, "rb") as f:
    pcap_data = savefile.load_savefile(f)
    if len(pcap_data.packets) > 0:
        print(pcap_data.packets[0])
    else:
        print("Pcap file is empty!")
