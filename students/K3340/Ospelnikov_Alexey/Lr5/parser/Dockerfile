FROM python:3.9-slim-buster

WORKDIR /parser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

CMD ["python", "run.py"]