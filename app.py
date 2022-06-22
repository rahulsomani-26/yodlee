from flask import Flask 

app = Flask(__name__)

@app.route('/')  # decorator 
def home():
    return '<h1> Hello World </h1>'


@app.route('/about')
def about():
    return """<h1> About page
            <p> This is the about section of the page 
            <h5> A headline 5 </h5>
     </h1>"""



app.run(debug=True)


