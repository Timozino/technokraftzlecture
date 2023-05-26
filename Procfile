release: python manage.py migrate
web: daphne educa.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --threads 4
worker_beat: python manage.py channels_redisworker