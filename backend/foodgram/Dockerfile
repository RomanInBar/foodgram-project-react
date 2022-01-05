FROM python:3.8.5
WORKDIR /diplom
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
CMD gunicorn foodgram.wsgi:application --bind 0:8000

ENV DB_ENGINE=django.db.backends.postgresql
ENV DB_NAME=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV DB_HOST=db
ENV DB_PORT=5432

LABEL file="backend-dokerfile" author="barabinr@list.ru"