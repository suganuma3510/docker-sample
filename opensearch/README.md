# OpenSearch - Docker sample
## 必要条件
- Docker Desktop >=4.20.1, Docker Engine and CLI >=24.0.6
- GNU Make 3.81

## 構築方法
1. イメージをビルド ＆ コンテナ立ち上げ
```
make build
make up
```

2. 初期データを登録
```
make setup
```

## ダッシュボード接続方法
1. ダッシュボードに[ログイン](http://localhost:5601/)（Username:admin, Password:admin）
2. Dev Tools を開く
3. 以下のクエリを実行
    ```
    GET posts/_search
    {
      "query": {
        "match_all": {}
      }
    }
    ```
4. 登録したデータが取得できればOK

## Analyzerの動作確認方法
1. 以下のクエリを実行
    ```
    GET posts/_search
    {
      "analyzer": "kuromoji_analyzer",
      "text" : "サイバーセキュリティのベストプラクティスと最新の脅威に対する対策を紹介します。"
    }
    ```

## kuromoji プラグインについて
公式：[kuromoji analyzer \| Elasticsearch Plugins and Integrations](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-analyzer.html)

### Character Filters
|kuromojiアナライザ|用途|例）解析前 → 解析後|
|:-|:-|:-|
|[kuromoji_iteration_mark](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-charfilter.html)|踊り字の正規化|刻々、すゞめ、シヾミ → 刻刻、すずめ、シジミ|

### Tokenizer
|kuromojiアナライザ|用途|例）解析前 → 解析後|
|:-|:-|:-|
|[kuromoji_tokenizer](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-tokenizer.html)|トークン化|東京スカイツリー → 東京, スカイツリー|

トークン化 - ある文章に対して文を構成する最小の意味単位（単語）に分解すること

### Token filters
|kuromojiアナライザ|用途|例）解析前 → 解析後|
|:-|:-|:-|
|[kuromoji_baseform](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-baseform.html)|原型化|飲み → 飲む|
|[kuromoji_part_of_speech](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-speech.html)|不要な品詞の除去|寿司がおいしいね → 寿司, おいしい|
|[kuromoji_readingform](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-readingform.html)|読み仮名付与|寿司 → スシ, sushi|
|[kuromoji_stemmer](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-stemmer.html#analysis-kuromoji-stemmer)|長音の除去|サーバー → サーバ|
|[kuromoji_number](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-number.html)|漢数字の半角数字化|一〇〇〇 → 1000|
|[ja_stop](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-stop.html)|ストップワードの除去|ストップは消える → 消える|
|[Lowercase](https://www.elastic.co/guide/en/elasticsearch/reference/8.10/analysis-lowercase-tokenfilter.html)|小文字に変換|THE Quick FoX JUMPs → the, quick, fox, jumps|


<details><summary>参考</summary>

- [kuromoji analyzer \| Elasticsearch Plugins and Integrations | Elastic](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji-analyzer.html)
- [pythonでOpensearchの検索機能を扱う \- Qiita](https://qiita.com/water12312/items/f66c60c3bd8493847024)
- [Elasticsearch のアナライザをカスタマイズする \- Linkode\.TechBlog](https://blog.linkode.co.jp/entry/2020/07/20/150701)
- [Elasticsearchで日本語検索を扱うためのマッピング定義 \- ZOZO TECH BLOG](https://techblog.zozo.com/entry/elasticsearch-mapping-config-for-japanese-search)
- [お金をかけずにサーバーの勉強をしよう \- OpenSearchで日本語の検索をする \-](https://subro.mokuren.ne.jp/0930.html)
- [Docker \- OpenSearch documentation](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/)

</details>
