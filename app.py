from flask import Flask

from utils.Constants import CONTROLLER, REPOSITORY

# Init app
app = Flask(__name__)


# Run Server
if __name__ == '__main__':
    exec(open(CONTROLLER).read())
    exec(open(REPOSITORY).read())
    app.run(host='0.0.0.0', port=5000,debug=True)
