FROM python:latest

WORKDIR api

ADD ./requirements.txt   /api/
RUN  pip install -r requirements.txt

ADD ./api /api

EXPOSE 8081
ENV PYTHONUNBUFFERED 0

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
