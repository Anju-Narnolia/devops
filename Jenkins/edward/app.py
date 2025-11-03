from flask import Flask, render_template  # correct import

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # file name in quotes

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
