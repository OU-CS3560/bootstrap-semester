FROM python:3.11-alpine3.18
ARG INCLUDE_DEV_DEPS

WORKDIR /code
COPY ./requirements.txt ./
COPY ./requirements.dev.txt ./
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN if [[ -n "$INCLUDE_DEV_DEPS" ]] ; then pip install --no-cache-dir --upgrade -r /code/requirements.dev.txt ; fi
COPY ./ /code

CMD ["/bin/sh", "./scripts/start.sh"]