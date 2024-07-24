#!/bin/sh

docker rm -f boilerplate-dev
docker run -d --name boilerplate-dev --rm -e POSTGRES_PASSWORD=changeme -e POSTGRES_DB=boilerplate_dev -p 55555:5432 postgres
docker start boilerplate-dev