FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install .

ENV AWS_REGION=
ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=

ENTRYPOINT ["python", "run.py"]