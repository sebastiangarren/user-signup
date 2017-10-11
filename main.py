from flask import Flask, render_template, request, redirect, url_for
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/welcome', methods=['POST'])
def welcome():
    password = request.form['password']
    verify_password = request.form['verify_password']
    name = request.form['user_name']
    email = request.form['email']

    password = cgi.escape(password)
    verify_password = cgi.escape(verify_password)
    name = cgi.escape(name)
    email = cgi.escape(email)
    is_error = 'False'

    return render_template('welcome.html', user_name=name)



#make only one return of all errors
#errors belong in HTML ready to go
#render page of errors together at '/'

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        password = request.form['password']
        verify_password = request.form['verify_password']
        name = request.form['user_name']
        email = request.form['email']

        password = cgi.escape(password)
        verify_password = cgi.escape(verify_password)
        name = cgi.escape(name)
        email = cgi.escape(email)
        is_error = 'False'

        name_error = ''
        pass_error = ''
        veri_error = ''
        email_error = ''

        if len(name) < 3:
            name_error = 'Name must be at least three characters.'
            is_error = 'True'
       

        if len(password) < 3 or len(password) > 20:
            pass_error = '''Password shouldn't be *that* short.'''
            is_error = 'True'
    

        if password != verify_password:
            veri_error = '''Passwords don't match'''
            is_error = 'True'
    

        if len(email) >= 1:
            if '@' and '.' not in email or ' ' in email:
                email_error = '''You need to have a proper email, mate.'''
                is_error = 'True'
    


        if is_error == 'True':    
            return render_template('user-signup.html', name_error=name_error, pass_error=pass_error, 
            veri_error=veri_error, email_error=email_error, user_name=name, email=email)
        else:
            return render_template('welcome.html', user_name=name)

    return render_template('user-signup.html')
app.run()