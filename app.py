from flask import Flask, jsonify, request
from flask_cors import CORS

from utils import Story
from middleware import Generate

import logging as log

log.basicConfig(
    format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s] %(message)s', 
    level=log.INFO
)
app = Flask(__name__)
CORS(app)
    

@app.route('/')
def index_request() -> jsonify:
    return jsonify({"body": "Application is running!"})

  
@app.route('/generate', methods=["POST"])
def generate_request() -> jsonify:
    if Generate(request.get_json()).check():
        return Story().get()
    
    
if __name__ == '__main__': 
    app.run(debug=True)
