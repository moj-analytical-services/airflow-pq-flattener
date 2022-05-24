ARG DE_ECR
FROM ${DE_ECR}/python:3.7

WORKDIR /pq_flattener

COPY requirements.txt .
COPY pq_flattener.py .
COPY v1 v1

RUN chmod -R 777 .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "pq_flattener.py"]
