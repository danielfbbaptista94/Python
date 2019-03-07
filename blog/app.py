from flask import flask

app = Flask(__name__)

@app.route('/')
def index:
    render_template('index.html')

@app.route('/about')
def about:
    render_template('about.html')



if __name == '__main__':
    app.run(debug=True)