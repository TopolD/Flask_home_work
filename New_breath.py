import os
import random
from Utils import Db, Db_moduls
from flask import Flask, render_template, session, request

# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_wtf import Form
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import InputRequired, Email

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
        Users = Db.db_session.query(Db_moduls.User).all()
        New_user = request.form.to_dict()
        for User in Users:
            if New_user:

                if User.User_name == New_user['User_name']:
                    return app.redirect('/user/signup', 302)

                else:
                    Add_user = Db_moduls.User(
                        User_name=New_user['User_name'],
                        Password=New_user['Password'],
                        Type=1
                    )
                    Db.db_session.add(Add_user)
                    Db.db_session.commit()
                    return app.redirect('/user/signin', 302)

        return app.redirect('/', 302)


@app.route('/user/signin', methods=['POST', 'GET'])
def Signin():
    if request.method == 'GET':
        return render_template('User.html')
    if request.method == 'POST':
        Db.init_db()
        Users = Db.db_session.query(Db_moduls.User).all()
        New_user = request.form.to_dict()
        if New_user:
            for User in Users:
                if User.User_name == New_user['User_name']:
                    session['ID'] = User.ID
                    session['Type'] = User.Type
                    return render_template('User.html')
                else:
                    return app.redirect('/user/signin', 302)

        return app.redirect('/', 302)


@app.route('/user/logout', methods=['POST', 'GET'])
def Logout():
    if session.get('ID'):
        session.pop('user.ID', None)
        session.pop('user.Type', None)
    return render_template('User.html')


@app.route('/cart', methods=['GET'])
def Cart():
    if request.method == 'GET':
        # if session.get('ID'):
        user_id = 1
        Db.init_db()
        Carts = Db.db_session.query(Db_moduls.Orders).filter(Db_moduls.Orders.User_id == user_id).all()
        Status = Db.db_session.query(Db_moduls.Orders).filter(Db_moduls.Orders.User_id == user_id).all()

        return render_template('Cart.html', Carts=Carts, Status=Status)
    # else:
    #     return app.redirect('/user/signin', 302)


@app.route('/cart/cartadd', methods=['POST', 'GET'])
def CartAdd():
    if request.method == 'GET':
        Db.init_db()
        user_id = 1
        Dishes = Db.db_session.query(Db_moduls.Dish).all()
        return render_template('Cart.html', Dishes=Dishes)

    if request.method == 'POST':
        user_id = 1
        req_cart = request.form.to_dict()
        if req_cart:
            Db.init_db()
            status_values = ''.join(map(str, [status[0] for status in
                                              Db.db_session.query(Db_moduls.Status.Status_name).filter(
                                                  Db_moduls.Status.ID == 1).all()]))
            price_values = ''.join(
                map(str, [price[0] for price in Db.db_session.query(Db_moduls.Dish.Dish_price).filter(
                    Db_moduls.Dish.Dish_name == req_cart["Dish_name"]).all()]))
            New_car = Db_moduls.Orders(
                User_id=user_id,
                Dish_name=req_cart['Dish_name'],
                Status=status_values,
                Price=price_values
            )
            Db.db_session.add(New_car)
            Db.db_session.commit()
            return render_template('Cart.html')
    else:
        return render_template('Cart.html')

    return render_template('Cart.html')


@app.route('/cart/delete', methods=['POST', 'GET'])
def CartDelete():
    if request.method == 'GET':
        user_id = 1

        Dishes = Db.db_session.query(Db_moduls.Orders.Dish_name).filter(Db_moduls.Orders.User_id == user_id).all()
        return render_template('Cart.html', Dishes=Dishes)
    if request.method == 'POST':

        req_cart = request.form.to_dict()
        user_id = 1
        if req_cart:
            dish_to_delete = Db.db_session.query(Db_moduls.Orders).filter_by(
                User_id=user_id, Dish_name=req_cart.get("Dish_name")).first()

            if dish_to_delete:
                Db.db_session.delete(dish_to_delete)
                Db.db_session.commit()
        return render_template('Cart.html', )
    return render_template('Cart.html')


@app.route('/menu', methods=['GET'])
def Menu():
    if request.method == 'GET':
        Db.init_db()
        Dishes = Db.db_session.query(Db_moduls.Dish).all()
        return render_template('Menu.html', Dishes=Dishes)
    return render_template('Menu.html')


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
