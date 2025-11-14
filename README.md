# URL Shortener

FlaskとSQLiteを使ったURL短縮サービス

## 🌟 機能

- ✅ 長いURLを短い6文字のコードに変換
- ✅ 短縮URLから元のURLへ自動リダイレクト
- ✅ クリック数の統計情報
- ✅ SQLiteデータベースで永続化

## 🛠 技術スタック

- **Python** 3.11
- **Flask** - Webフレームワーク
- **SQLite** - データベース

## 📦 インストール

### 1. リポジトリをクローン
```bash
git clone https://github.com/code-craftsman369/url-shortener.git
cd url-shortener
```

### 2. 依存パッケージをインストール
```bash
pip install flask
```

## 🚀 使い方

### サーバーを起動
```bash
python app.py
```

サーバーが `http://localhost:5003` で起動します。

## 📝 API エンドポイント

### 1. ホームページ
```bash
GET /
```

**レスポンス例**：
```json
{
  "message": "URL短縮サービスへようこそ",
  "endpoints": {
    "shorten": "POST /shorten",
    "redirect": "GET /<short_code>",
    "stats": "GET /stats/<short_code>"
  }
}
```

---

### 2. URLを短縮
```bash
POST /shorten
Content-Type: application/json

{
  "url": "https://www.example.com/very/long/url"
}
```

**レスポンス例**：
```json
{
  "original_url": "https://www.example.com/very/long/url",
  "short_code": "aB3xY9",
  "short_url": "http://localhost:5003/aB3xY9"
}
```

**curlでの実行例**：
```bash
curl -X POST http://localhost:5003/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com"}'
```

---

### 3. 短縮URLからリダイレクト
```bash
GET /<short_code>
```

**例**：
```
http://localhost:5003/aB3xY9
```

元のURLに自動リダイレクトされます。

---

### 4. 統計情報を取得
```bash
GET /stats/<short_code>
```

**レスポンス例**：
```json
{
  "short_code": "aB3xY9",
  "original_url": "https://www.example.com/very/long/url",
  "created_at": "2025-11-14 11:18:00",
  "clicks": 42
}
```

**curlでの実行例**：
```bash
curl http://localhost:5003/stats/aB3xY9
```

## 💡 使用例

### シナリオ：GitHubのURLを短縮
```bash
# 1. URLを短縮
curl -X POST http://localhost:5003/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com/code-craftsman369"}'

# レスポンス:
# {
#   "short_url": "http://localhost:5003/KX9s7r",
#   "short_code": "KX9s7r"
# }

# 2. ブラウザでアクセス
# http://localhost:5003/KX9s7r → GitHubページに飛ぶ

# 3. 統計を確認
curl http://localhost:5003/stats/KX9s7r

# レスポンス:
# {
#   "clicks": 5,
#   "created_at": "2025-11-14 11:49:53"
# }
```

## 🗄️ データベース構造

### urls テーブル

| カラム | 型 | 説明 |
|--------|-----|------|
| id | INTEGER | 主キー |
| original_url | TEXT | 元のURL |
| short_code | TEXT | 短縮コード（6文字） |
| created_at | TEXT | 作成日時 |
| clicks | INTEGER | クリック数 |

## 📚 学習内容

このプロジェクトを通じて学んだこと：

- FlaskでのREST API作成
- SQLiteデータベースの基本操作
- HTTPリダイレクトの実装
- ランダム文字列の生成
- データベーストランザクション
- エラーハンドリング

## 🔜 今後の改善予定

- [ ] カスタムURL対応（ユーザーが短縮コードを指定）
- [ ] 有効期限機能
- [ ] QRコード生成
- [ ] HTMLフロントエンド
- [ ] ユーザー認証
- [ ] URL削除機能
- [ ] アクセス履歴（日時、IPアドレス）

## ⚠️ 注意事項

- このプロジェクトは学習目的です
- 本番環境で使用する場合は、セキュリティ対策を追加してください
- データベースファイル（urls.db）は `.gitignore` に含まれています

## 📄 ライセンス

MIT License

## 👤 作成者

Tatsu - Python Developer
- GitHub: [@code-craftsman369](https://github.com/code-craftsman369)

## 🙏 謝辞

- [Flask](https://flask.palletsprojects.com/) - Webフレームワーク
- [SQLite](https://www.sqlite.org/) - データベース
