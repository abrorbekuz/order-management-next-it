FROM python:3.10-slim
WORKDIR /app
COPY requirements/prod.txt .
RUN pip install --no-cache-dir -r prod.txt
COPY . .

RUN python manage.py collectstatic --noinput --settings=config.settings.prod

EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--log-level", "debug"]