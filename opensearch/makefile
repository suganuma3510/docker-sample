up:
	docker compose up -d

build:
	docker compose build

down:
	docker compose down

setup:
	docker exec -it -u 0 opensearch yum -y install python3 python3-pip
	docker exec -it -u 0 opensearch python3 -m pip install opensearch-py
	docker exec -it -u 0 opensearch python3 init/setup.py
