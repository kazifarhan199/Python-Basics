from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
	return "<h1> What is your naem ?<h1><h2> Name of you'r school/coledge <h2>"	

if __name__=='__main__':
	app.run(debug=True)
