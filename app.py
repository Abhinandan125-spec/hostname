from flask import Flask, render_template_string
import socket
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the hostname of the server (not the client machine)
    server_hostname = socket.gethostname()

    # Open the index.html file from the same directory as app.py
    with open(os.path.join(os.path.dirname(__file__), 'index.html'), 'r') as file:
        index_html = file.read()

    # Render the HTML content with the server hostname
    return render_template_string(index_html, server_hostname=server_hostname)

if __name__ == '__main__':
    app.run(debug=True)
