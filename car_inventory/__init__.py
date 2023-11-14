from flask import Flask
from .blueprints.site.routes import site

#instatiating our Flask app
app = Flask(__name__)



# @app.route("/")
# def Amelias_luxury_cars():
#     return "<p>Amelia_luxury_cars!</p>"

app.register_blueprint(site)


