from flask import Flask, render_template, url_for, request, flash, redirect, session, abort
import config
import prepate



app = Flask(__name__)
app.config.from_object(__name__)

menu = [{"name": 'Установка', "url": "install-flask"},
        {"name": 'Первое приложение', "url": "first-app"},
        {"name": 'Обратная связь', "url": "contact"}]


@app.route("/")
@app.route("/index")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
        print(request.form)
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route("/userbase")
def userbase():
    users = prepate.get_users_from_db(config.select_all_users)
    users_list = []
    for user in users:
        name = f'{user.user_first_name} {user.user_second_name} {user.user_surname}'
        url = url_for('person', userid=user.user_employeeid)
        user_dict = {"name": name, "url": url}
        users_list.append(user_dict)

    return render_template('usersbase.html', title="Список пользователей", menu=menu, users=users_list)


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "selfedu" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title="Авторизация", menu = menu)


@app.route("/person/<userid>")
def person(userid):
    current_user = prepate.get_one_user_from_db(userid)[0]
    title = current_user.user_first_name + " " + current_user.user_surname
    return render_template('userprofile.html', title=title, menu=menu, first_name=current_user.user_first_name,
                           second_name=current_user.user_second_name, surname=current_user.user_surname,
                           age=current_user.user_age)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)

# with app.test_request_context():
#    print(url_for('about'))
