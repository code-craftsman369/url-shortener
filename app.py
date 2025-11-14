from flask import Flask, request, jsonify, redirect, render_template
import sqlite3
import string
import random
from datetime import datetime

app = Flask(__name__)

# データベース初期化
def init_db():
    """データベースを初期化"""
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL,
            clicks INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()

# 短縮コードを生成
def generate_short_code():
    """6文字のランダムな短縮コードを生成"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def home():
    """ホームページ"""
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten_url():
    """URLを短縮する"""
    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({"error": "URLが必要です"}), 400
    
    original_url = data['url']

    # カスタムコードがあればそれを使う、なければ自動生成
    if 'custom_code' in data and data['custom_code']:
        short_code = data['custom_code']

        # カスタムコードの検証（英数字のみ、3-20文字）
        import re
        if not re.match(r'^[a-zA-Z0-9_-]{3,20}$', short_code):
            return jsonify({"error": "カスタムコードは3-20文字の英数字、ハイフン、アンダースコアのみ使用可能です"}), 400
    else:
        short_code = generate_short_code()

    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # データベースに保存
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO urls (original_url, short_code, created_at) VALUES (?, ?, ?)',
            (original_url, short_code, created_at)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        if 'custom_code' in data and data['custom_code']:
            return jsonify({"error": "このカスタムコードは既に使用されています"}), 409
        else:
            # ランダムコードが重複した場合は再生成
            return shorten_url()
    finally:
        conn.close()

    return jsonify({
        "original_url": original_url,
        "short_url": f"http://localhost:5003/{short_code}",
        "short_code": short_code
    })


@app.route('/<short_code>')
def redirect_url(short_code):
    """短縮からURLから元のURLにリダイレクト"""
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
    result = cursor.fetchone()

    if result:
        original_url = result[0]

        # クリック数を増やす
        cursor.execute('UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?', (short_code,))
        conn.commit()
        conn.close()

        return redirect(original_url)
    else:
        conn.close()
        return jsonify({"error": "URLが見つかりません"}), 404

@app.route('/stats/<short_code>')
def get_stats(short_code):
    """短縮URLの統計情報を取得"""
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute('SELECT original_url, created_at, clicks FROM urls WHERE short_code = ?', (short_code,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({
            "short_code": short_code,
            "original_url": result[0],
            "created_at": result[1],
            "clicks": result[2]
        })
    else:
        return jsonify({"error": "URLが見つかりません"}), 404

@app.route('/delete/<short_code>', methods=['DELETE'])
def delete_url(short_code):
    """短縮URLを削除"""
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM urls WHERE short_code = ?', (short_code,))

    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        return jsonify({"message": "URLを削除しました"}), 200
    else:
        conn.close()
        return jsonify({"error": "URLが見つかりません"}), 404


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5003, debug=True)

