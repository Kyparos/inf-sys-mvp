FROM postgres:alpine
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=postgres
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
