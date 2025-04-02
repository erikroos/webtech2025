from strike_app import app
from flask import render_template

### Only one (home) route

@app.route("/")
def index():
    return render_template("home.html")

### Deploy app

if __name__ == "__main__":
    app.run(debug=True, port=5000)