from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="??"

@app.route('/')
def submit():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submittedInfo():
    print("Submitted user info")
    session['name'] = request.form['name']
    session['Location'] = request.form['Location']
    session['Language'] = request.form['Language']
    # session['comments'] = request.form['comments']
    return redirect('/process')

@app.route('/process')
def showResult():
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)