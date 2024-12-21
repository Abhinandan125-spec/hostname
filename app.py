from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def index():
    # Get the hostname of the server (not the client machine)
    server_hostname = socket.gethostname()
    return render_template('index.html', server_hostname=server_hostname)

if __name__ == '__main__':
    app.run(debug=True)
