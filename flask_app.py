import json
from flask import Flask,request
import apiai
import twilio.twiml
from twilio.rest import TwilioRestClient
import config

# Configurations for twilio, apiai, and flask.
client = TwilioRestClient(config.account_sid, config.auth_token)
ai = apiai.ApiAI(config.client_access_token)
app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello World!"

@app.route("/", methods=['GET', 'POST'])
def server():

    # get SMS input via twilio
    resp = twilio.twiml.Response()

    # get SMS metadata
    msg_from = request.values.get("From", None)
    msg = request.values.get("Body", None)
    print('msg')

    # # prepare API.ai request
    # req = ai.text_request()
    # req.lang = 'en'  # optional, default value equal 'en'
    # req.query = msg

    #  # get response from API.ai
    # api_response = req.getresponse()
    # responsestr = api_response.read().decode('utf-8')
    # response_obj = json.loads(responsestr)

    # if 'result' in response_obj:
    #     response = response_obj["result"]["fulfillment"]["speech"]

    return str(msg_from)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')