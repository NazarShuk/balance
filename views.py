import random
from flask import *
import socket
import os
import threading
from bot import send
import re
views = Blueprint(__name__,"views")

@views.route("/")
def home():
    print("Hello")
    return "<center><h1>Nothing here</h1></center>"

@views.route("/profile/<usern>",methods=['GET','POST'])
def getname(usern):
    if request.method == 'POST':
        if request.form['sendb'] == 'Запросить':
            return redirect(url_for('views.requestt', user = usern))
        elif request.form['sendb'] == 'Отправить':
            return redirect(url_for('views.sendd', user = usern))
        elif request.form['sendb'] == 'Робота':
            return redirect(url_for('views.work', user = usern))
        else:
            pass # unknown
    
    elif request.method == 'GET':
        global money
        money = str()
        if os.path.exists(f"accounts/{usern}/{usern}.money"):
            file = open(f'accounts/{usern}/{usern}.money', 'r+')
            money = file.readlines()[0]
            file.close()
            return render_template('index.html',name = usern, mon = money)
        else:
            
            filea = open(f'accounts/{usern}/{usern}.money','w')
            filea.write(f"0")
            filea.write(f"")
            money = 0
            filea.close()
            return render_template('index.html',name = usern, mon = money)


           


       

@views.route("/profile/<user>/send", methods=['GET','POST'])
def sendd(user):
    if request.method == 'POST':
        if request.form['sendb'] == 'Отправить':
            allmon = False
            outmon = int(request.form['count'].upper())
            name = request.form['ip'].upper()
            name = re.sub(f'\s+', '',name)
            fileee = open(f'accounts/{user}/{user}.money','r')
            curmon = fileee.readlines()[0]
            fileee.close()
            if outmon > int(curmon):
                allmon = True

            
            recvfile = open(f'accounts/{name}/{name}.money','r+')
            recvmoncur = recvfile.readlines()[0]
            recvfile.close()
            os.remove(f"accounts/{name}/{name}.money")

            recvfile2 = open(f'accounts/{name}/{name}.money','w')
            if allmon:
                recvmon = int(recvmoncur) + int(curmon)
            else:
                recvmon = int(recvmoncur) + int(outmon)
            
            recvfile2.write(f"{str(recvmon)}")
            recvfile2.write(f"")
            recvfile2.close()

            sendfile = open(f'accounts/{user}/{user}.money','r+')
            curmoncur = sendfile.readlines()[0]
            if allmon:
                curmon = "0"
            else:
                curmon = int(curmoncur) - outmon
            sendfile.close()
            os.remove(f"accounts/{user}/{user}.money")

            sendfile2 = open(f'accounts/{user}/{user}.money','w')
            sendfile2.write(f"{str(curmon)}")
            sendfile2.write(f"")
            sendfile2.close()
            print(user," Sent ",outmon," UAH to ",name)
            return redirect(url_for('views.getname', usern = user))
        else:
            pass # unknown
    elif request.method == 'GET':
        filer = open(f'accounts/{user}/{user}.money', 'r+')
        money = filer.readlines()[0]
        filer.close()
        return render_template("send.html",name=user,mon=money)

#strrand ="""
@views.route("/profile/<user>/requ", methods=['GET','POST'])
def requestt(user):
    if request.method == 'POST':
        if request.form['requb'] == 'Запрос':
            why = request.form['why'].lower()
            howmuch = request.form['count'].upper()
            send(f"🔵 {user} просит {howmuch} UAH! Причина: {why}")
            return redirect(url_for('views.getname', usern = user))
        else:
            pass # unknown
    elif request.method == 'GET':
        global money
        money = str()
        try:
            file = open(f'accounts/{user}/{user}.money', 'r+')
            money = file.readlines()[0]
            file.close()
            return render_template('request.html',mon = money)
        except:
            filea = open(f'accounts/{user}/{user}.money','w')
            filea.write(f"0")
            money = 0
            filea.close()
            return render_template('request.html',mon = money)#"""

@views.route("/profile/<user>/work", methods=['GET','POST'])
def work(user):
    if request.method == 'POST':
        if request.form['butt'] == 'Готово':
            workname = request.form['name'].lower()
            description = request.form['desc'].lower()
            timework = request.form['time'].lower()
            cost = request.form['cost'].lower()
            send(f"🔵 {user} может обеспечить вам услоги {workname}a - {description}. Цена: {cost} UAH, работает до {timework}")
            return redirect(url_for('views.getname', usern = user))
        else:
            pass # unknown
    elif request.method == 'GET':
        global money
        money = str()
        try:
            file = open(f'accounts/{user}/{user}.money', 'r+')
            money = file.readlines()[0]
            file.close()
            return render_template('work.html',mon = money)
        except:
            filea = open(f'accounts/{user}/{user}.money','w')
            filea.write(f"0")
            money = 0
            filea.close()
            return render_template('work.html',mon = money)#"""