from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "change-this-in-production"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        flash('Thank you. Your enquiry has been received. Contact-form delivery will be connected before launch.', 'success')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
