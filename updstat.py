from flask import *

updatestatus = Blueprint(__name__,"updstat")

@updatestatus.route('/profile/<usern>')
def Home(usern):
    return render_template("Updating.html")
