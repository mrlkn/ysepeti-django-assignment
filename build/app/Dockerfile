FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY app/requirements.txt /app/

ADD build/app/bootstrap.sh /bootstrap.sh

RUN pip install -r /app/requirements.txt

COPY fixtures /build/fixtures

COPY app/ /app/

EXPOSE 8000

CMD ["/bin/bash", "/bootstrap.sh"]