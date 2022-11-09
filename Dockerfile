FROM python:3.10
WORKDIR /app
COPY requeriments.txt .
RUN pip install -r requirements.txt
COPY . . 
CMD ["/bin/bash", "docker-entrypoint.sh"]

