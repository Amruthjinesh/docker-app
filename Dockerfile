FROM python:3.14

WORKDIR /app

COPY app.py .

EXPOSE 8000

CMD ["python3", "app.py"]
