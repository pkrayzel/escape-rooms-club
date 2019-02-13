FROM library/python:alpine3.7

RUN pip install Flask==0.12.2

ADD ./docker/website /src/website
WORKDIR /src/website

EXPOSE 5000
CMD ["python", "app.py"]