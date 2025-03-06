FROM python:3.11

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY WebServer /home/backend/WebServer/WebServer
COPY API /home/backend/WebServer/API
COPY manage.py /home/backend/WebServer/
COPY initDB.py /home/backend/WebServer/initDB.py

WORKDIR /home/backend/WebServer

EXPOSE 8000

CMD ["python", "initDB.py"]
