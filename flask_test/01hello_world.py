from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    print request.headers
    print request.method

    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
