FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 10000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
