FROM opensearchproject/opensearch:latest

COPY . .
RUN /usr/share/opensearch/bin/opensearch-plugin install analysis-kuromoji && \
    /usr/share/opensearch/bin/opensearch-plugin install analysis-icu