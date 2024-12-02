from flask import render_template, request, redirect, url_for
from . import app
from .formsGPT import ContactForm
from .modelsGPT import Department, Course

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process form data here (e.g., send an email)
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)

@app.route('/academics')
def academics():
    departments = Department.query.all()
    return render_template('academics.html', departments=departments)
