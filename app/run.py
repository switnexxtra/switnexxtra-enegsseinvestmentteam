from app.app import app
from flask import Blueprint
from flask import render_template


# app = create_app()
home = Blueprint('home', __name__, static_folder='static', template_folder='templates')


@home.route('/')  
def index():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)