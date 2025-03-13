docker build -t producter:txx --progress=plain  .
docker run -p 8888:8000 --env DOCKER_CMD="python manage.py migrate && python manage.py loaddata expanded_data && python manage.py runserver 0.0.0.0:8000" --env ALLOWED_HOSTS=* producter:txx
