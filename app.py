from flask import Flask, render_template
#You need to use following line [app Flask(__name__]
app = Flask(__name__)

@app.route('/')
def index():
    headline = "Hello, World"
    return render_template("index.html", headline=headline)

@app.route('/bye')
def bye():
    headline = "Goodbye! Loser!!!"
    return render_template("index.html", headline=headline)

if __name__ == '__main__':
    app.run(port=5000,debug=True)