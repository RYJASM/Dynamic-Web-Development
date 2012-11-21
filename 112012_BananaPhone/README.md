## This is a take on the DWD Remote API Example Using Twilio

https://github.com/johnschimmel/itp-py-dwd-remote-apis

It uses TwiML to play a simple MP3 located on a Heroku server.  

To get started setup Twilio

### Getting Twilio Account

* Register [https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio).
* Verify phone number with access code.
* Pick a phone number.
* Poke around all their API endpoints, make and receive calls, make and receive SMS.

When you are registered locate your your Account SID and Auth Token here,[https://www.twilio.com/user/account](https://www.twilio.com/user/account) and add them to your .env file

**.env**	

	TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxx
	TWILIO_AUTH_TOKEN=xxxxxxxxx
	TWILIO_PHONE_NUMBER=+XXXXXXXXX

Now let's add the Twilio account variables to Heroku.

**In your code directory in Terminal run,**

	heroku config:add TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxx
	heroku config:add TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxx
	heroku config:add TWILIO_PHONE_NUMBER=+XXXXXXXXX

Lastly review the App.py file;

Add these lines to include Twilio and the TwiML modules.

# Twilio
from twilio.rest import TwilioRestClient
from twilio.util import TwilioCapability
from twilio import twiml

Create a route for "the call" to take;

app.route('/voice', methods=['POST'])
def voice():
    response = twiml.Response()
    response.play("http://bananaphone.herokuapp.com/static/img/BananaPhone.mp3")
    return str(response) 

Make sure you have the MP3 File in it's appropriate ref. Location.

Lastly go to your Twilio control panel at Twilio.com under

https://www.twilio.com/user/account/phone-numbers/

set the voice URL to your route in app.py: in this case bananaphone.herokuapp.com/voice

