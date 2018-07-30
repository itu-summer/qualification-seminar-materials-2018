import os
import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='')


def init_db(db='survey_replies.db'):
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        sql_cmd = '''CREATE TABLE Replies
                     (gender text, mob integer, dob integer, yob integer, nation text, fav_icecream text, icecream text, cake text, cookies text, ingredient text, comment text, email text)'''
        c.execute(sql_cmd)
        conn.commit()


def save_reply_to_db(data, db='survey_replies.db'):
    if not os.path.isfile(db):
        init_db(db)
    with sqlite3.connect(db) as conn:
        (gender, mob, dob, yob, nation, fav_icecream, icecream, cake, cookies,
         ingredient, comment, email) = data
        mob, dob, yob = int(mob), int(dob), int(yob)

        c = conn.cursor()
        c.execute('INSERT INTO Replies VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
                  (gender, int(mob), int(dob), int(yob), nation, fav_icecream,
                   icecream, cake, cookies, ingredient, comment, email))


@app.route('/', methods=['GET', 'POST'])
def serve_file():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        users_reply = request.form
        save_reply_to_db(users_reply.values())
        return 'Thank you! Your answers are saved.'


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
