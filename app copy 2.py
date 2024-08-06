from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Get the client IP address
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr
    return f'Your IP address is: {client_ip}'

@app.route('/')
def indexs():
    # Get the client IP address
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr
    return f'Your IP address is: {client_ip}'

if __name__ == '__main__':
    app.run(debug=True)
