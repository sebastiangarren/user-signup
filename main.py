from flask import Flask, render_template, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


    

@app.route('/welcome', methods=['POST'])
def welcome():
    password = request.form['password']
    verify_password = request.form['verify_password']
    name = request.form['user_name']

    if len(name) < 3:
        error = 'Name must be at least three characters.'
        return redirect("/?error=" + error)

    if len(password) < 3 or len(password) > 20:
        error = '''Password shouldn't be *that* dumb.'''
        return redirect("/?error=" + error)

    if password != verify_password:
        error = '''Passwords don't match'''
        return redirect("/?error=" + error)
    else: 
        return render_template('welcome.html', user_name=name)

@app.route('/')
def index():
    form_error  = request.args.get('error')
    return render_template('user-signup.html', error=form_error and cgi.escape(form_error, quote=True))

app.run()