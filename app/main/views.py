from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from ..models import User, Role
from .forms import NameForm
from ..email import send_simple_message

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            role = Role.query.filter_by(name=form.role.data).first()
            if role is None:
                role = Role(name=form.role.data)
                db.session.add(role)
                db.session.commit()
            user = User(username=form.name.data, role=role)
            db.session.add(user)
            db.session.commit()
            session['known'] = False

            response = send_simple_message(
                subject="Novo usuário cadastrado",
                body=f"Usuário {user.username} foi cadastrado com sucesso com a função {role.name} na Aplicação."
            )
            if response.status_code == 200:
                print("E-mail enviado com sucesso.")
            else:
                print(f"Falha no envio do e-mail: {response.status_code} - {response.text}")
        else:
            session['known'] = True
        session['name'] = form.name.data
        session['role'] = form.role.data
        return redirect(url_for('main.index'))

    users = User.query.all()
    roles = Role.query.all()
    total_users = len(users)
    users_by_role = {role.name: User.query.filter_by(role=role).all() for role in roles}

    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), users=users,
                           total_users=total_users, users_by_role=users_by_role)
