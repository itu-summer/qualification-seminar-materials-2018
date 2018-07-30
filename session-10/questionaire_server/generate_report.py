import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='')


@app.route('/')
def serve_report():
    db = 'survey_replies.db'
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM Replies')
        contents = c.fetchall()

        for idx, line in enumerate(contents):
            print(f'Reply {idx}: {line}')
    return render_template('report.html', reply_lines=contents)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
