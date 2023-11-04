import os
import random
from Utils import Db, Db_moduls
from flask import Flask, render_template, session, request

app = Flask(__name__)

session_secret = os.environ.get('SESSION_SECRET')
if not session_secret:
    if not os.path.exists('session.secret'):
        secret_file = open('session.secret', 'w')
        secret_file.write(str(random.randint(10000000, 999999999)))
        secret_file.close()
    secret_file = open('session.secret')
    session_secret = secret_file.read()
    secret_file.close()

app.secret_key = session_secret

user_id = session.get('ID')


@app.route('/')
def Window():
    return render_template('Base.html')


@app.route('/admin')
def Admin():
    if session.get('Type') == 1:
        return app.redirect('/user', 302)

    if not session.get('Type'):
        return app.redirect('/user/signin', 302)

    else:
        return render_template('Admin.html')


@app.route('/admin/currentorders', methods=['GET'])
def CurrentOrders():
    return render_template('Admin.html')


@app.route('/admin/Menu', methods=['POST', 'GET'])
def Admin_Menu():
    return render_template('Admin.html')


@app.route('/admin/addish', methods=['POST', 'GET'])
def Addish():
    return render_template('Admin.html')


@app.route('/admin/addcat', methods=['POST', 'GET'])
def Addcat():
    return render_template('Admin.html')


@app.route('/admin/cat', methods=['POST', 'GET'])
def cat():
    return render_template('Admin.html')


@app.route('/user', methods=['POST', 'GET'])
def User():
    if request.method == 'GET':
        return render_template('User.html')
    else:
        return app.redirect('/', 302)


@app.route('/user/signup', methods=['POST', "GET"])
def Signup():
    if not session.get('ID'):
        Db.init_db()
        User = request.form.to_dict()

        return render_template('User.html')
    else:
        return app.redirect('user/signin', 302)


@app.route('/user/signin', methods=['POST', 'GET'])
def Signin():
    if request.method == 'GET':
        return render_template('User.html')
    if request.method == 'POST':
        Db.init_db()
        User = request.form.to_dict()
        return render_template('User.html')
    else:
        return render_template('User.html')


@app.route('/user/logout', methods=['POST', 'GET'])
def Logout():
    if session.get('ID'):
        session.pop('user.ID', None)
    return render_template('User.html')


@app.route('/cart', methods=['GET', 'POST'])
def Cart():
    if session.get('ID'):

        Db.init_db()
        Cart = Db.db_session.query(Db_moduls.Orders).filter(Db_moduls.Orders.ID_USER == user_id).all()
        for Carts in Cart:
            return render_template('Cart.html', Carts=Carts)

    else:
        return app.redirect('user/signin', 302)


@app.route('/cart/cartadd', methods=['POST', 'GET'])
def CartAdd():
    Db.init_db()
    req_cart = request.form.to_dict()
    if req_cart:
        New_car = Db_moduls.Orders(
            Dish_name=req_cart['Dish_name'],
        )
        Db.db_session.add(New_car)
        Db.db_session.commit()
    else:
        return render_template('Cart.html')

    return render_template('Cart.html')


@app.route('/cart/delete', methods=['POST', 'GET'])
def CartDelete():
    return render_template('Cart.html')


@app.route('/menu', methods=['POST', 'GET'])
def Menu():
    return render_template('Menu.html')


if __name__ == "__main__":
    app.run()
