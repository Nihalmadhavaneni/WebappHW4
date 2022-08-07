from flask import Flask, request, render_template, redirect
import sqlite3
import uuid

app = Flask(__name__)


@app.route('/stds', methods=['GET'])
def hw4():

    hw4 = sqlite3.connect('hw4.db')
    d_cur = hw4.cursor()
    d_cur.execute('select * from hw4')
    vals = d_cur.fetchall()

    return render_template('company.html', content=vals)




@app.route('/update', methods=['POST'])
def hw4_update():
    hw4 = sqlite3.connect('hw4.db')
    d_cur = hw4.cursor()
    if(request.method == 'POST'):
        cnumber = request.form['cnumber']
        name = request.form['name']
        email = request.form['email']
        addr = request.form['addr']
        d_cur.execute("update hw4 set st_name = '{0}', st_email = '{1}', st_addr = '{2}' where c_number = '{3}' ".format( 
            name, email, addr, cnumber))
        hw4.commit()
        hw4.close()
        return redirect('/', code=302)



@app.route('/delete', methods=['POST'])
def hw4_del():
    hw4 = sqlite3.connect('hw4.db')
    d_cur = hw4.cursor()
    if(request.method == 'POST'):
        delete_id = request.form['del']
        d_cur.execute('delete from hw4 where c_number= ?', [delete_id])
        hw4.commit()
        hw4.close()
        return redirect('/',  code=302)


@app.route('/', methods=['GET', 'POST'])
def start():
    if(request.method == 'POST'):
        hw4 = sqlite3.connect('hw4.db')
        d_cur = hw4.cursor()
        d_cur.execute(
            'create table if not exists hw4 (c_number varchar(255), st_name varchar(255), st_email varchar(255),st_addr varchar(255));')
        hw4.commit()
        
        cnumber = request.form['cnumber']
        name = request.form['name']
        email = request.form['email']
        addr = request.form['addr']
        d_cur.execute("insert into hw4 (c_number, st_name, st_email, st_addr) values (?,?,?,?)", [str(cnumber), str(name), str(email), str(addr) ])
        hw4.commit()
        hw4.close()

    return render_template('Index.html')


app.run(host='localhost', port=5002, debug=True)
