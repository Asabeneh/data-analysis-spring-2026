from flask import Flask, render_template, jsonify



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contact():
    return render_template('contacts.html')


@app.route('/cats')
def cats():
    return render_template('cats.html')



if __name__ ==  '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug=True)