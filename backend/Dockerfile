FROM python:3.11-alpine3.18

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code

CMD ["/bin/sh", "./scripts/start.sh"]