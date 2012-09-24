import os
from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template
app = Flask(__name__)   # create our flask app

# # this is our main page
# @app.route("/")
# def index():
#     return """Hello World!<br/><br/>
#     <a href='/page2'>Visit page #2</a><br>
#     <a href='/form'>Visit form page</a>"""

# # this is my main page
@app.route("/")
def index():
    return render_template('main.html')


# this is the about route - can be access with /about
@app.route("/about")
def about():
	return render_template('about.html')


# new route will accept both a GET and POST request from the client (web browser)
@app.route("/form", methods=["POST"])
def simpleform():

	# Did the client make a POST request?
	if request.method == "POST":

		# get the form data submitted and store it in a variable
		first_name = request.form.get('first_name', 'you did not enter a first name!')

		last_name = request.form.get('last_name', 'you did not enter a last name!')
		# return custom HTML using the user submitted data
		
		return render_template('formresponse.html', first_name =first_name, last_name =last_name, )


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 4777)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)