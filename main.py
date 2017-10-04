from flask import Flask, render_template, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True
    

@app.route('/welcome', methods=['POST'])
def welcome():
    password = request.form['password']
    verify_password = request.form['verify_password']
    name = request.form['user_name']
    email = request.form['email']

    if len(name) < 3:
        name_error = 'Name must be at least three characters.'
        return redirect("/?name_error=" + name_error)

    if len(password) < 3 or len(password) > 20:
        pass_error = '''Password shouldn't be *that* short.'''
        return redirect("/?pass_error=" + pass_error)

    if password != verify_password:
        veri_error = '''Passwords don't match'''
        return redirect("/?veri_error=" + veri_error)

    if len(email) > 1:
        if '@' or '.' not in email:
            if '' in email:
                email_error = '''You need to have a proper email, mate.'''
                return redirect("/?email_error=" + email_error)
    else:
        return render_template('welcome.html', user_name=name)

@app.route('/')
def index():
    form_error1  = request.args.get('name_error', default='')
    form_error2  = request.args.get('pass_error', default='')
    form_error3  = request.args.get('veri_error', default='')
    form_error4  = request.args.get('email_error', default='')
    return render_template('user-signup.html', 
    name_error=form_error1 and cgi.escape(form_error1, quote=True),
    pass_error=form_error2 and cgi.escape(form_error2, quote=True),
    veri_error=form_error3 and cgi.escape(form_error3, quote=True),
    email_error=form_error4 and cgi.escape(form_error4, quote=True))
app.run()