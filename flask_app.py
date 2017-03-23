import apiai
import json
from flask import Flask

import config

ai = apiai.ApiAI(config.client_access_token)
app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello World!"

@app.route("/<msg>", methods=['GET', 'POST'])
def server(msg):

    # prepare API.ai request
    req = ai.text_request()
    req.lang = 'en'  # optional, default value equal 'en'
    req.query = msg

     # get response from API.ai
    api_response = req.getresponse()
    responsestr = api_response.read().decode('utf-8')
    response_obj = json.loads(responsestr)

    if 'result' in response_obj:
        response = response_obj["result"]["fulfillment"]["speech"]

    return str(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')