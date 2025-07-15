from flask import Flask,render_template,redirect,request,url_for
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key='tamil'

app.config['MYSQL_HOST']='db111.ce3goq6c4v62.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER']='admin'
app.config['MYSQL_PASSWORD']='root1234'
app.config['MYSQL_DB']='mydb'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee')
def employee():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM empdetails")
    empinfo = cur.fetchall()
    cur.close()
    return render_template('employee.html',employees=empinfo)

@app.route('/search',methods= ['POST', 'GET'])
def search():
    search_results = []
    search_term=''
    if request.method == "POST":
        search_term=request.form['empid']
        cur = mysql.connection.cursor()
        query="SELECT * FROM empdetails WHERE id like %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results=cur.fetchmany(size=1)
        cur.close()
        return render_template('employee.html',employees=search_results)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        iddata= request.form['empid']
        name = request.form['name']
        email = request.form['email']
        dept = request.form['dept']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO empdetails (id,name,email,dept) VALUES (%s,%s,%s,%s)", (iddata,name,email,dept,))
        mysql.connection.commit()
        return redirect(url_for('employee'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM empdetails WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('employee'))

@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['empid']
        name = request.form['name']
        email = request.form['email']
        dept = request.form['dept']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE empdetails SET name=%s,email=%s,dept=%s WHERE id=%s", (name,email,dept,(id_data,),))
        mysql.connection.commit()
        return redirect(url_for('employee'))









if __name__=="__main__":
    app.run(debug=True)

