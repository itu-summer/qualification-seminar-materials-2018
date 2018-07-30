from random import choice
from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET', 'POST'])
def serve_file():
    if request.method == 'GET':
        return render_template('index.html', eliza='Hej, how are you today?')
    elif request.method == 'POST':
        users_reply = request.form['myreply']
        print(users_reply)
        elizas_replies = ['I lost my brain... I do not know what to say!',
                          'I feel a bit dumb today...',
                          'Blubblubblub']
        return render_template('index.html', eliza=choice(elizas_replies))


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
