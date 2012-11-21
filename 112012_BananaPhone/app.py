# -*- coding: utf-8 -*-
import os, datetime
import re
from unidecode import unidecode

from flask import Flask, request, redirect, render_template, abort

# Twilio
from twilio.rest import TwilioRestClient
from twilio.util import TwilioCapability
from twilio import twiml

 

# create Flask app
app = Flask(__name__)   # create our flask app


# --------- Routes ----------
@app.route('/', methods=['GET'])
def main():
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    # This is a special Quickstart application sid - or configure your own
    # at twilio.com/user/account/apps
    application_sid = os.environ.get('TWILIO_APP_SID')

    capability = TwilioCapability(account_sid, auth_token)
    capability.allow_client_outgoing(application_sid)
    token = capability.generate()

    return render_template('index.html', token=token)

@app.route('/voice', methods=['POST'])
def voice():
    response = twiml.Response()
    response.play("http://bananaphone.herokuapp.com/static/img/BananaPhone.mp3")
    return str(response)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# --------- Server On ----------
# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	