
FROM python:3.14-slim

COPY     requirements.txt /
RUN      pip3 install  -r /requirements.txt

WORKDIR  /app
COPY     src  /app
CMD ["python3", "main.py"]

