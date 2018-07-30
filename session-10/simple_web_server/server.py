import socket
from flask import Flask, render_template, send_from_directory


app = Flask(__name__, static_url_path='')


@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/image')
def serve_file():
    return send_from_directory('./static', 'commander_keen.png')


@app.route('/complete')
def complete():
    return app.send_static_file('index_img.html')


@app.route('/hello_from')
def hello_from():
    host_name = socket.gethostname()
    return render_template('hello_from.html', hostname=host_name,
                           hostip=socket.gethostbyname(host_name))


if __name__ == '__main__':
    # app.run(host='127.0.0.1', debug=True)
    app.run(host='0.0.0.0', debug=True)
