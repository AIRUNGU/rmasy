web: gunicorn rmasy.wsgi:application --log-file -
web2: daphne rmasy.routing:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2