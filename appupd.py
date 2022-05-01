
from flask import Flask, render_template,request
from views import views
from updstat import updatestatus
from bot import send
app = Flask(__name__)

app.register_blueprint(views,url_prefix="/") # Start normal server
#app.register_blueprint(updatestatus,url_prefix="/") #Start Updating server.
app.secret_key = "92837498237498JKHHDIUHdshfkjsdh_(_)(____))"

if __name__ == '__main__':
    app.run(debug=True,port=7777)
    
