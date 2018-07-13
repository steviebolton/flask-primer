import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title = 'home')
    
    
@app.route('/about')
def about():
    return render_template('about.html', page_title = 'about')
    
    
@app.route('/careers')
def careers():
    return render_template('careers.html', page_title = 'careers')
   
    
@app.route('/contact')
def contact():
    return render_template('contact.html', page_title = 'contact')
        
if __name__ == '__main__':
    app.run(host = os.environ.get("IP"),
            port =  os.environ.get("PORT"),
            debug = True)

