# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ARG directory=./frontend-streamlit

COPY $directory/requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY $directory /app

#EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]
