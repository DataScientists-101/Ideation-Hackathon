from flask import Flask, g
from flask import request, url_for, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

token = {
    'status': []
    }

#@app.route('/')
@app.route("/",methods=['GET'])
def index():
    live = request.args.get('status')
    if live != None:
        token['status'].append(live)
        print(token['status'])
        return 'status added'
    else:
        result = {
            'status': token['status']
            }
        #result = json.dumps(result)
        print('fetching')
        token['status'] = []
        return result
    

if __name__ == '__main__':
    app.run()
