from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# connecting to db 
db = pymysql.connect (
   host = "localhost",
   user = "root",
   password = "r00tpassword.",
   database = "login"
)
cursor = db.cursor()

###################### HANDLING LOGIN ######################
@app.route('/', methods = ['GET', 'POST'])
def login():
   cursor.execute("SELECT * FROM info")
   rows = cursor.fetchall()
   for row in rows:
      print(row)
   # get user input information
   if request.method == 'POST':
      input_username = request.form['username']
      input_password = request.form['password']
      print("Username:", input_username)
      print("Password:", input_password)
   else:
      return render_template('index.html')
   # if user exists check pw
   cursor.execute("SELECT * FROM info WHERE username = '" + input_username + "'")
   username = cursor.fetchone()
   # print("Username db struct:", username)

   if username:
      # if correct go to next page
      if username[1] == input_password:
         return render_template('success.html')
      # else say incorrect pw
      else:
         return render_template('index.html', error = "Error with login info")
   # else go to sign up page
   else:
      return redirect(url_for('signup'))
##############################################################
   
###################### HANDLING SIGN UP ######################
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
   if request.method == 'POST':
      input_username = request.form['username']
      input_password = request.form['password']
      print("Username:", input_username)
      print("Password:", input_password)

      
      print("INSERT INTO info (username, password) VALUES ('" + input_username + "', '" + input_password + "')")
      cursor.execute("INSERT INTO info (username, password) VALUES ('" + input_username + "', '" + input_password + "')")
      db.commit()
      
      return render_template('index.html', success_msg="Account created successfully, you may now login with credentials")
   else:
      return render_template('signup.html')
##############################################################

if __name__ == '__main__':
   app.run(debug=True)