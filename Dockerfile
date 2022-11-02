FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requeriments.txt .
RUN pip install -r requeriments.txt
COPY . . 
CMD ["flask","run","--host","0.0.0.0"]