FROM library/python:3.7.2-alpine3.8

# site-downloader requirements
ADD ./utils /opt/utils

RUN pip install -r /opt/utils/requirements/site-downloader.txt

env AWS_ACCESS_KEY_ID foo
env AWS_SECRET_ACCESS_KEY bar
env AWS_DEFAULT_REGION us-east-1

RUN chmod +x /opt/utils/tests_unit.sh
RUN chmod +x /opt/utils/tests_integration.sh

ADD ./src /src/

EXPOSE 80
ENTRYPOINT []