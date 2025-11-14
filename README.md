# URL Shortener

FlaskとSQLiteを使った本格的なURL短縮サービス

## 🌟 機能

- ✅ 長いURLを短い6文字のコードに自動変換
- ✅ **カスタムURL対応**（好きな短縮コードを指定可能）
- ✅ 短縮URLから元のURLへ自動リダイレクト
- ✅ クリック数の統計情報
- ✅ **美しいHTMLフロントエンド**
- ✅ ワンクリックコピー機能
- ✅ URL削除機能
- ✅ SQLiteデータベースで永続化
- ✅ エラーハンドリング

## 🛠 技術スタック

- **Python** 3.11
- **Flask** - Webフレームワーク
- **SQLite** - データベース
- **HTML/CSS/JavaScript** - フロントエンド

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

### ブラウザでアクセス
```
http://localhost:5003/
```

綺麗なWebインターフェースが表示されます！

## 🎨 Webインターフェース

### 特徴

- グラデーション背景
- レスポンシブデザイン
- リアルタイムエラー表示
- ワンクリックコピー機能
- カスタムURL入力フォーム

### 使い方

1. **短縮したいURL**を入力
2. （オプション）**カスタムコード**を入力（例：my-link）
3. **「短縮URLを作成」**をクリック
4. 短縮URLが表示されます
5. **「📋 コピー」**でクリップボードにコピー

## 📝 API エンドポイント

### 1. ホームページ（HTML）
```bash
GET /
```

Webインターフェースを表示

---

### 2. URLを短縮
```bash
POST /shorten
Content-Type: application/json

{
  "url": "https://www.example.com/very/long/url",
  "custom_code": "my-link"  // オプション
}
```

**レスポンス例**：
```json
{
  "original_url": "https://www.example.com/very/long/url",
  "short_code": "my-link",
  "short_url": "http://localhost:5003/my-link"
}
```

**curlでの実行例（自動生成）**：
```bash
curl -X POST http://localhost:5003/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com"}'
```

**curlでの実行例（カスタムコード指定）**：
```bash
curl -X POST http://localhost:5003/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com/code-craftsman369", "custom_code": "my-github"}'
```

---

### 3. 短縮URLからリダイレクト
```bash
GET /<short_code>
```

**例**：
```
http://localhost:5003/my-link
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
  "short_code": "my-link",
  "original_url": "https://www.example.com/very/long/url",
  "created_at": "2025-11-14 11:18:00",
  "clicks": 42
}
```

**curlでの実行例**：
```bash
curl http://localhost:5003/stats/my-link
```

---

### 5. URLを削除
```bash
DELETE /delete/<short_code>
```

**レスポンス例**：
```json
{
  "message": "URLを削除しました"
}
```

**curlでの実行例**：
```bash
curl -X DELETE http://localhost:5003/delete/my-link
```

## 💡 使用例

### シナリオ1：Webインターフェースで短縮

1. ブラウザで `http://localhost:5003/` を開く
2. URLに `https://github.com/code-craftsman369` を入力
3. カスタムコードに `my-github` を入力
4. 「短縮URLを作成」をクリック
5. `http://localhost:5003/my-github` が作成される
6. 「📋 コピー」でクリップボードにコピー

---

### シナリオ2：APIで短縮（自動生成）
```bash
# 1. URLを短縮（ランダムコード生成）
curl -X POST http://localhost:5003/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com"}'

# レスポンス:
# {
#   "short_url": "http://localhost:5003/aB3xY9",
#   "short_code": "aB3xY9"
# }

# 2. ブラウザでアクセス
# http://localhost:5003/aB3xY9 → YouTubeに飛ぶ

# 3. 統計を確認
curl http://localhost:5003/stats/aB3xY9

# 4. URLを削除
curl -X DELETE http://localhost:5003/delete/aB3xY9
```

---

### シナリオ3：カスタムURLで短縮
```bash
# カスタムコード "portfolio" を指定
curl -X POST http://localhost:5003/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://myportfolio.com", "custom_code": "portfolio"}'

# 短縮URL: http://localhost:5003/portfolio
```

## 🗄️ データベース構造

### urls テーブル

| カラム | 型 | 説明 |
|--------|-----|------|
| id | INTEGER | 主キー（自動増分） |
| original_url | TEXT | 元のURL |
| short_code | TEXT | 短縮コード（3-20文字、ユニーク） |
| created_at | TEXT | 作成日時 |
| clicks | INTEGER | クリック数（デフォルト0） |

## 📁 ファイル構成
```
url-shortener/
├── app.py                 # メインアプリケーション
├── templates/
│   └── index.html        # Webインターフェース
├── urls.db               # SQLiteデータベース（自動生成）
├── .gitignore
└── README.md
```

## 🎓 学習内容

このプロジェクトを通じて学んだこと：

- FlaskでのREST API設計
- SQLiteデータベース操作
- HTTPリダイレクトの実装
- ランダム文字列生成
- 正規表現によるバリデーション
- カスタムURL機能の実装
- HTMLフロントエンドとAPIの連携
- JavaScriptでのfetch API使用
- CRUD操作（作成・読取・更新・削除）
- エラーハンドリング

## ⚙️ カスタムURL機能

### ルール

- 3-20文字
- 英数字、ハイフン（-）、アンダースコア（_）のみ
- 既に使用されているコードは使用不可

### 例
```bash
✅ 有効なカスタムコード
- my-github
- portfolio_2024
- important-link
- ABC123

❌ 無効なカスタムコード
- ab (短すぎる、3文字以上必要)
- this-is-a-very-long-custom-code-name (長すぎる、20文字以内)
- my link (スペース不可)
- リンク (日本語不可)
```

## 🔜 今後の改善予定

- [ ] 有効期限機能
- [ ] QRコード生成
- [ ] ユーザー認証・ログイン
- [ ] アクセス履歴（日時、IPアドレス、リファラー）
- [ ] URL編集機能
- [ ] バルク削除機能
- [ ] ダッシュボード（統計グラフ）
- [ ] PostgreSQL対応
- [ ] Docker対応

## ⚠️ 注意事項

- このプロジェクトは学習目的です
- 本番環境で使用する場合は、以下の対策を追加してください：
  - HTTPS対応
  - レート制限
  - セキュリティヘッダー
  - XSS対策
  - CSRF対策
  - SQLインジェクション対策（現在はプレースホルダーで対応済み）

## 📄 ライセンス

MIT License

## 👤 作成者

Tatsu - Python Developer
- GitHub: [@code-craftsman369](https://github.com/code-craftsman369)

## 🙏 謝辞

- [Flask](https://flask.palletsprojects.com/) - Webフレームワーク
- [SQLite](https://www.sqlite.org/) - データベース
