ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}-slim-bullseye

ARG MARIADB_CLIENT_VERSION=10.5

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    mariadb-client-${MARIADB_CLIENT_VERSION} && \
    rm -rf /var/lib/apt/lists/*

ARG directory=./mlflow
COPY $directory/requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

ENV MLFLOW_HOST=0.0.0.0
ENV MLFLOW_PORT=5000
ENV MLFLOW_BACKEND_STORE_URI="${DB_TYPE}://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:${DB_MLFLOW_PORT}/${DB_NAME}"
ENV MLFLOW_DEFAULT_ARTIFACT_ROOT="s3://${ARTIFACT_S3_BUCKET}/${ARTIFACT_S3_KEY_PREFIX}"

ENV MLFLOW_SQLALCHEMYSTORE_POOL_SIZE=10
ENV MLFLOW_SQLALCHEMYSTORE_MAX_OVERFLOW=10

CMD ["/bin/bash", "-c", "mlflow server --host=${MLFLOW_HOST} --port=${MLFLOW_PORT} --backend-store-uri=${MLFLOW_BACKEND_STORE_URI} --default-artifact-root=${MLFLOW_DEFAULT_ARTIFACT_ROOT}"]

