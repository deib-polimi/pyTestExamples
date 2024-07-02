from flask import (
    Flask,
    render_template
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/viewMap')
def viewMap():
    return render_template('viewMap.html')

@app.route('/reserveBike')
def reserveBike():
    return 'Congratulations, you have reserved a bike!'

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
