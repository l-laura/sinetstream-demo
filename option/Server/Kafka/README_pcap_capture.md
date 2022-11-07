# kafka-pcap

Packet data logging contanier usage reference.

```bash
# Startup:
docker volume create --name=pcap-capture
docker-compose up -d

# Start test apps as separate processes. Let the system run, PCAP data will be logged.

# When done:
docker-compose down --volumes
docker container create --name temp -v pcap-capture:/data hello-world
docker cp temp:/data ./pcap-capture
docker rm temp

# To remove logged data:
docker volume rm pcap-capture
docker volume prune
```

Starting applications (note that kafka takes ca 10 seconds to start).
Python virtual environment recommended.

```bash
pip install -r requirements.txt
python test-apps/test-producer.py -s text-1
```

```bash
python test-apps/test-consumer.py -s text-1
```