python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn clg_adminstration.wsgi:application --bind 0.0.0.0:$PORT