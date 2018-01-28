from flask import Flask
from flask_bootstrap import Bootstrap

    
# Function to create flask with boostrap
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)

    return app

# Initialize the app
app = create_app()

# Load the views
from app import views

# Load the config file
app.config.from_object('config')
