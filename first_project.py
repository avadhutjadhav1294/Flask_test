from flask import Flask, redirect, url_for, request, render_template
#in django request was the argumrnt for each method but in flask it is imported from flask,

app = Flask(__name__)

@app.route('/home/') #decorator drfines the   -- called controller function
def home():  
    return "hello, this is our first flask website"  

@app.route('/home/<name>/') #decorator drfines the   -- called controller function
def home_name(name):  
    return f"hello,{name} this is our first flask website" 

@app.route('/home/<name>/<int:age>') #decorator drfines the   -- called controller function
def home_name_age(name,age):  
    return f"hello,{name} : {age} this is our first flask website" 

# Another way of adding the url
def home_url_rule():
    return "hello This is from home_url_rule"

app.add_url_rule("/home-url/", "home_url", home_url_rule)

@app.route('/admin/')  
def admin():  
    return 'admin'  
  
@app.route('/librarion/')  
def librarion():  
    return 'librarion'  
  
@app.route('/student/')  
def student():  
    return 'student'  
  
@app.route('/user/<name>/')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  
    
@app.route('/login/',methods = ['POST', 'GET'])  
def login():  
    if request.method == 'POST': 
        uname=request.form['uname']  # in django we use to get the data by using request.post 
        passwrd=request.form['pass'] 
        if uname=="ayush" and passwrd=="google":  
            return f"Welcome {uname}"
        else:
            return "Unauthorised User,You are not Welcome"
    uname=request.args.get('uname')  
    passwrd=request.args.get('pass')  
    if uname=="ayush" and passwrd=="google":  
        return "Welcome %s" %uname  
    else:
        return "Unauthorised User,You are not Welcome"
    
@app.route("/message/") # returns html message
def message():
    return "<html><body><h1>Hi, welcome to the website</h1></body></html>"  

@app.route("/message-page/") # returns html page
def message_page():
    return render_template("message.html") #it will automatically detect templates folder and search for file if u put the html anywhere else its error

@app.route("/message/<name>/")
def message_name(name):
    return render_template("dynamic_msg.html", name=name)


@app.route("/table/<int:num>")
def table_num(num):
    return render_template("table.html", no=num)

@app.route("/customer/")
def customer():
    return render_template("customer.html")

@app.route('/success/',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("result_data.html",result = result) 

@app.route("/upload/")
def upload():
    return render_template("upload.html")

@app.route("/done/", methods = ["POST"])
def done():
    if request.method == 'POST':
       f = request.files["file"]
       f.save(f.filename)
       return render_template("done.html", name = f.filename)


if __name__ =='__main__':  
    app.run(debug = True)  