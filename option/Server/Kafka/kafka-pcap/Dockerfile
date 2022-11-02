FROM ubuntu

RUN apt clean && \
    apt update && \
    apt -y upgrade && \
    apt -y install \
    tcpdump

RUN mkdir /pcap-src
ADD packet-capture/* /pcap-src/
CMD /pcap-src/capture.sh

VOLUME /pcap
