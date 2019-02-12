FROM localstack/localstack:0.8.7

RUN pip install awscli

env AWS_ACCESS_KEY_ID foo
env AWS_SECRET_ACCESS_KEY bar
env AWS_DEFAULT_REGION us-east-1

HEALTHCHECK --interval=5s --timeout=60s --retries=5 \
  CMD aws --endpoint-url http://localhost:4572 s3 ls
