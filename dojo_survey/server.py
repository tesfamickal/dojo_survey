from flask import Flask, session, redirect, request, render_template

app = Flask(__name__)
app.secret_key = "dkfjr9yu59834u890fj43ur9482"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    return redirect('/results')


@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True)
