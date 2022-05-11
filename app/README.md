# Scraping app

github apiを使ってリポジトリのissueを収集する

## Getting Started

環境変数について

.envの作成

TOKENについては下部のReferenceを参考にしてください

example:

```
USERNAME="examplename"
TOKEN="aaaaaaaaaaaaaaaaa"
```


docker環境の立ち上げ

```
docker-compose up -d --build
```





## reference
- [docker環境構築について](https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5)
- [認証方式について](https://docs.github.com/ja/rest/overview/other-authentication-methods)
- [GithubAPIについて色々とまとめてみた](https://qiita.com/syossan27/items/dd3bd152792360c29d01)