FROM python:3.8.5
WORKDIR /diplom
COPY . .
RUN pip install --upgrade pip && pip install -r /diplom/requirements.txt
ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000