FROM python:3.10-bullseye

ARG WORKDIR=/opt/user/src

WORKDIR ${WORKDIR}

# fix to execute test within src.x.y module import
ENV PYTHONPATH=${WORKDIR}/../

COPY ./src ./

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask", "run"]