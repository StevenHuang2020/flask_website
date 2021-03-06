from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from first_website.models import User, Post
from first_website import db, bcrypt
from first_website.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from first_website.users.forms import RequestResetForm, ResetPasswordForm
from first_website.users.utils import save_picture, send_reset_email


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Your account have been! You are now able to login!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

        # if form.email.data == 'admin@t.com' and form.password.data == '123':
        #     flash('You have been logged in!', 'success')
        #     return redirect(url_for('main.home'))
        # else:
        #     flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        print('brn=', request.form, type(request.form))
        if 'submit' in request.form.keys():
            if form.picture.data:
                # print('form.picture.data=', form.picture.data, type(form.picture.data))
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file

            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()

            flash('Your account have been updated!', 'success')
            return redirect(url_for('users.account'))
        elif 'delete_account' in request.form.keys():
            print('delete accounting...')
            User.query.filter_by(username=current_user.username).delete()
            db.session.commit()
            flash('Your account have been deleted!', 'success')
            return redirect(url_for('users.login'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='profile_imgs/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@users.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_post.html', posts=posts, user=user)


@users.route('/reset_password',  methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An emial has been sent to reset your password!', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route('/reset_password/<token>',  methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token!', 'warning')
        return redirect(url_for('users.reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password have been updated! You are now able to login!', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
