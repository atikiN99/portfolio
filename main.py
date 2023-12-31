from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:

            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save'
    else:
        return 'something went wrong'

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline="", mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



#@app.route('/')
#def my_landing():
#    return render_template('index.html')
#
#@app.route('/index.html')
#def my_home():
#    url_for('static', filename='assets/favicon.ico')
#    url_for('static', filename='style.css')
#    url_for('static', filename='main.70a66962.js')
#    return render_template('index.html')
#
#
#@app.route('/about.html')
#def my_about():
#    return render_template('about.html')
#
#@app.route('/works.html')
#def my_works():
#    return render_template('works.html')
#
#@app.route('/contact.html')
#def my_contact():
#    return render_template('contact.html')