FROM python:3.9-slim-buster

WORKDIR /TimeManager

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "run.py"]