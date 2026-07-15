FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN mkdir -p logs
RUN pip install -r requirements.txt
CMD ["python3", "src/main.py"]