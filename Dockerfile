FROM python:3.7

WORKDIR /pq_flattener

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY pq_flattener.py .
COPY v1 v1

ENTRYPOINT ["python3", "pq_flattener.py"]
