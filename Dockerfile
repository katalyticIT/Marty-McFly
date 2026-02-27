#
# Dockerfile to build Marty McFly Demo Application
# (showcase for moving containers in time=
# 

FROM python:3.14-slim

# updates for basic image, then install libfaketime
RUN  apt-get upgrade && apt-get update
RUN  apt-get install -y libfaketime

# install the necessary python libraries
COPY requirements.txt /
RUN  pip3 install  -r /requirements.txt

# copy the webapp into the image
WORKDIR  /app
COPY     src  /app

# using CMD, not ENTRYPOINT, to keep it open for quick experiments
CMD ["python3", "main.py"]

