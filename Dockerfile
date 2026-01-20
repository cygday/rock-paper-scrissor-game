FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .

RUN pip install flask --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "-c", "gnicorn app:app --bind", "0.0.0.0:$PORT"]
