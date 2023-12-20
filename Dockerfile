FROM python:3.10-alpine3.13

WORKDIR /opt/user/src

COPY ./src ./

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask", "run"]