from flask import redirect, url_for, render_template, flash, request
from fitness import app, db, bcrypt
from fitness.forms import SignInForm, SignUpForm, itemForm
from fitness.database import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from fitness import nix
import json

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


@app.route("/")
def index():
    return render_template('index copy.html')


@app.route("/home")
def home():
    return render_template('index copy.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')


@app.route("/tracker",methods = ["GET", "POST"])
def tracker():
       # query = nix.search().nxql(
        #filters={
         #   "nf_calories":{
          #      "lte": 500
           # }
        #},
        #fields = ["item_name","item_id","nf_calories"]
        #).json()
        form = itemForm()
        if form.validate_on_submit():
            searchItem = form.item.data
            query = nix.search(searchItem, results="0:1").json()
            objId = query['hits'][0]['_id']
            info = nix.item(id=objId).json()
            
            filterInfo = "Name: " +str(info['item_name']) + "\ncalories: " + str(info['nf_calories']) + "\ncalories from fat: " + str(info['nf_calories_from_fat']) + "\ntotal fat(grams): " + str(info["nf_total_fat"]) + "\nsaturated fat(grams): " + str(info['nf_saturated_fat']) + "\nserving size(grams): " + str(info['nf_serving_weight_grams'])
            filterInfo = filterInfo.split('\n')
            return render_template("tracker.html", form = form, query = filterInfo)
        return render_template("tracker.html", form = form, query = "")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(fname=form.first_name.data, lname=form.last_name.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Thank you for signing up with us', 'success')
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Register', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('signin.html', form=form)
