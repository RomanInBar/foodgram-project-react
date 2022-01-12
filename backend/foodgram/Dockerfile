FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip \
    && pip3 install -r /code/requirements.txt --no-cache-dir
COPY . .
ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
