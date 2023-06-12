from flask import Flask

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

if __name__ =='__main__':  
    app.run(debug = True)  