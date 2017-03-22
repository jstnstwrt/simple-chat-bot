import apiai

# api.ai account info
CLIENT_ACCESS_TOKEN = "78c0e0________________fbcd9404a2"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello api.ai (from Flask!)'

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

        return response

    else:
        return 'I do not understand.'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
