FROM python:3.8-slim

RUN pip install weaviate-client flask

COPY app.py /app.py
COPY weaviate_docker-compose.yml /weaviate_docker-compose.yml

# Set environment variables for Weaviate configuration
ENV QUERY_DEFAULTS_LIMIT=100
ENV AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED="false"
ENV PERSISTENCE_DATA_PATH="./data"
ENV DEFAULT_VECTORIZER_MODULE="text2vec-transformers"
ENV ENABLE_MODULES="text2vec-transformers"
ENV TRANSFORMERS_INFERENCE_API="https://inference-api.your-transformers-service.com"
ENV WEAVIATE_AUTHENTICATION_ADMIN_USERNAME=$WEAVIATE_AUTHENTICATION_ADMIN_USERNAME
ENV WEAVIATE_AUTHENTICATION_ADMIN_PASSWORD=$WEAVIATE_AUTHENTICATION_ADMIN_PASSWORD

CMD ["sh", "-c", "docker-compose -f /weaviate_docker-compose.yml up"]
