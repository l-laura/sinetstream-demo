FROM ubuntu

RUN apt clean && \
    apt update && \
    apt -y upgrade && \
    apt -y install \
    tcpdump

RUN mkdir /pcap
ADD packet-capture/* /pcap/

CMD /pcap/capture.sh