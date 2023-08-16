FROM python:3.10-slim
WORKDIR keylogger-server/
COPY . simple_keylogger_HTTP
CMD ["python3", "simple_keylogger_HTTP/server.py"]
