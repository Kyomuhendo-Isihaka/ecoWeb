from django.shortcuts import render, redirect
from http.client import HTTPResponse
from urllib.parse import uses_relative
from urllib.request import HTTPCookieProcessor
from ecoApp.models import customer_req
import mysql.connector

# Create your views here.

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "ecosense"
)

mycursor = con.cursor()

def login(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')

        sql="SELECT * FROM users"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for x in result:
            if x[1]==username and x[2]==password:
                
                html = redirect('/dashboard') 
                html.set_cookie("accountname",username,360000)  
                return html
                return redirect('/dashboard') 
            else:
                error = "Invalid Username or Password "    

    return render(request, "login.html",{'error':error})

def admin(request):
    cook = request.COOKIES["accountname"]   
    return render(request,"admin.html",{'name':cook})

def customer_req(request):
    id = "",
    cook = request.COOKIES["accountname"] 
    sql = "SELECT * FROM customer_req WHERE status='pending'"
    mycursor.execute(sql)
    results = mycursor.fetchall()

    for i in results:
        if request.method=="POST":
            print(id)
            id = i[0]
            sq = "UPDATE customer_req SET status='done' WHERE id = 'id' " 
            mycursor.execute(sq)
            con.commit()     

    return render(request,"customer_req.html", {'results':results,'name':cook})

def history(request):
    cook = request.COOKIES["accountname"] 
    sql = "SELECT * FROM customer_req WHERE status != 'pending'"
    mycursor.execute(sql)
    results = mycursor.fetchall()

    return render(request, "history.html", {'results':results, 'name':cook})

def users(request):
    sql = "SELECT * FROM users"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    cook = request.COOKIES['accountname']
    return render(request,"users.html",{'name':cook,'results':results})

def settings(request):
    if request.method=="POST":
        newUname = request.POST.get('uname')
        newUphone = request.POST.get('phone')
        newUpass = request.POST.get('pass')

        sql = "INSERT INTO users(username,password,phone) VALUES(%s,%s,%s)"
        val = (newUname,newUpass,newUphone)
        mycursor.execute(sql,val)
        con.commit()

    cook = request.COOKIES['accountname']
    return render(request,"settings.html",{'name':cook})





