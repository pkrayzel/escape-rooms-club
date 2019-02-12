FROM library/python:alpine3.7

RUN pip install Flask==0.12.2

ADD website /opt/website
WORKDIR /opt/website

EXPOSE 80
CMD ["python", "app.py"]