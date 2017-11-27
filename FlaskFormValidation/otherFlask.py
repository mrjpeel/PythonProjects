from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)


def index():
    return 'index.html'


def signup():
    fullName = request.form['fullName']
    subject = request.form['subject']
    noName = "There was no name entered"
    noSubject = "There was no subject entered"

    if fullName == "" and subject == "":
        print("Name field was blank")
        return 'index.html', noName = noName, noSubject = noSubject
    elif fullName == "":
        print("Subject field was blank")
        return 'index.html', noName = noName
    elif subject == "":
        return 'index.html', noSubject = noSubject
    else:
        print("The name is '" + fullName + "' and the subject was '" + subject)
        return 'thankyou.html')


def reset():
    print("reset called")
    return redirect('/')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)