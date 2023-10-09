import csv
from opensearchpy import OpenSearch

host = "host.docker.internal"
port = 9200
auth = ("admin", "admin")
client = OpenSearch(
    hosts=[{"host": host, "port": port}],
    http_compress=True,
    http_auth=auth,
    use_ssl=True,
    verify_certs=False,
)

index_name = "posts"

settings = {
    "settings": {
        "analysis": {
            "analyzer": {
                "kuromoji_analyzer": {
                    "type": "custom",
                    "char_filter": ["icu_normalizer"],
                    "tokenizer": "kuromoji_tokenizer",
                    "filter": [
                        "kuromoji_baseform",
                        "kuromoji_part_of_speech",
                        "ja_stop",
                        "kuromoji_number",
                        "kuromoji_stemmer",
                    ],
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "id": {"type": "keyword"},
            "title": {"type": "text", "analyzer": "kuromoji_analyzer"},
            "description": {"type": "text", "analyzer": "kuromoji_analyzer"},
            "created_at": {
                "type": "date",
            },
        }
    },
}

if not client.indices.exists(index=index_name):
    client.indices.create(index=index_name, body=settings)

id = 1
with open("init/data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for data in reader:
        client.index(index=index_name, body=data, id=id)
        id += 1
