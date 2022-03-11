# laravel-docker

## 使用技術
- Laravel v8.49.1 (PHP v8.0.5)
- PostgreSQL v13.3

## 構築方法
1. ビルド
```
docker compose build
```

2. ライブラリのインストール
```
docker compose run --rm app composer install
```

3. コンテナ作成 ＆ 起動
```
docker compose up
```

4. http://localhost:8080/ にアクセス
5. 初期画面ページが表示されれば構築成功！

#### よく使うコマンド(おまけ)
マイグレーション実行
```
docker compose exec app php artisan migrate
```

upしたコンテナでコマンド実行
```
docker compose exec ＜サービス名＞ ＜実行したいコマンド＞
docker compose exec db echo 'hello'
```

upしたコンテナに入る
```
docker compose exec ＜サービス名＞ sh
# または
docker compose exec ＜サービス名＞ bash

docker compose exec db sh
# または
docker compose exec db bash
```

## pgadmin4 の使い方
1. http://localhost:8000/ にアクセス
2. ログイン画面にてアカウント名とパスワードを入力  
アカウント名：root  
パスワード：pass  
![ログイン画面](https://user-images.githubusercontent.com/57606507/124541663-dcefe980-de5c-11eb-98ab-99b19f84be06.png)
3. 「新しいサーバを追加」を押下
![ダッシュボード画面](https://user-images.githubusercontent.com/57606507/124542679-cd71a000-de5e-11eb-80f9-129fbcc0900e.png)

4. 名称に任意のサーバ名を入力し、「接続」を押下
![接続画面1](https://user-images.githubusercontent.com/57606507/124542673-cc407300-de5e-11eb-94a2-d78282b656ac.png)
5. DBの接続情報を入力し、「保存」を押下  
ホスト名/アドレス：db  
ユーザ名：root  
パスワード：pass  
![接続画面2](https://user-images.githubusercontent.com/57606507/124542675-ccd90980-de5e-11eb-9a15-d7d07f5aca98.png)

6. 接続が成功した場合、左に作成したDBが表示される
![プロパティ画面](https://user-images.githubusercontent.com/57606507/124542676-cd71a000-de5e-11eb-9390-a1aa23023ecb.png)

---
## 参考記事
- [最強のLaravel開発環境をDockerを使って構築する \- Qiita](https://qiita.com/ucan-lab/items/5fc1281cd8076c8ac9f4)
- [【超入門】20分でLaravel開発環境を爆速構築するDockerハンズオン \- Qiita](https://qiita.com/ucan-lab/items/56c9dc3cf2e6762672f4)
- [docker composeを使ってPostgreSQLを構築する \| mebee](https://mebee.info/2020/12/04/post-24686/)
- [Docker \+ Nginx \+ Laravelの開発環境構築からHerokuへのDeployまで](https://zenn.dev/nagi125/articles/ea1d314c94409341a3b0)