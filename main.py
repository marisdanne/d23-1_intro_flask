from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about_html():
  return render_template('about.html')

@app.route('/contact')
def contacts_html():
  return render_template('contact.html', phone = "22140077")

@app.route('/params')
def params():
  return request.args

@app.route('/post', methods = ['POST'])
def post():
  return request.get_json()

if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5020, debug=True)