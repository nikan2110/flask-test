from flask import Flask
import logging

from utils.Constants import CONTROLLER, REPOSITORY

# Init app
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s %(message)s %(filename)s',level=logging.INFO)


# Run Server
if __name__ == '__main__':
    exec(open(CONTROLLER).read())
    exec(open(REPOSITORY).read())
    app.run(host='0.0.0.0', port=5000,debug=True)
