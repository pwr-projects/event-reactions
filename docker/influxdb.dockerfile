FROM influxdb:latest

COPY influxdb.conf /etc/influxdb/influxdb 

# RUN influxdb