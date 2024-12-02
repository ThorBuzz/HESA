from flask import render_template,request, session, flash,redirect, url_for
from . import app, bcrypt,db
from .forms import RegistrationForm, LoginForm, EditProfileForm, PostForm, CommentForm, ContactForm
from .models import User, Post, Comment
from flask_login import login_user, logout_user, current_user, login_required

# HOME PAGE
@app.route("/")
def home():
   # create an explore/updates page??
   posts=Post.query.all()
   return render_template('home.html',posts=posts)

# LOGIN PAGE IF NO STUDENT DATABSE
@app.route("/login", methods=['POST', 'GET'])
def login():
   if current_user.is_authenticated:
      print(current_user)
      return redirect(url_for('profile'))
   form=LoginForm()
   if form.validate_on_submit():
      user=User.query.filter_by(id=form.id.data).first()
      if user:
         if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.rememberMe.data)
            flash(f'Logged in as {user.username}','success')
            next_page=request.args.get('next')
            print(next_page)
            return redirect(next_page) if next_page else redirect(url_for('home'))
         else:
            flash(f'Incorrect password. Please try again','danger')
      else:
         flash('Account not found', 'warning')
   return render_template('login.html', form=form)

      
# REGISTRATION PAGE
@app.route("/register", methods=['POST', 'GET'])
def register():
   if current_user.is_authenticated:
      return redirect(url_for('profile'))
   form = RegistrationForm()
   if form.validate_on_submit():
      hashedPassword=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      # until we have a database, this is what we're going to use
      user=User(id=form.id.data, username=form.username.data, password=hashedPassword, email= form.email.data)
      db.session.add(user)
      db.session.commit()
      flash('Account created successfully. Please log in.', 'success')
      return redirect(url_for('login'))
   else:
      print(form.errors)
   return render_template('register.html', form=form)

# PROFILE PAGE
@app.route("/profile", methods=['POST', 'GET'])
@login_required
def profile():
   return render_template('profile.html')

# LOGOUT
@app.route("/logout")
def logout():
   logout_user()
   flash('You have been logged out', 'warning')
   return redirect(url_for('login'))

# EDIT PROFILE
@app.route("/editProfile", methods=['POST', 'GET'])
@login_required
def editProfile():
   form=EditProfileForm()
   if form.validate_on_submit():
      hashedPassword=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user=User(username=form.username.data, password=hashedPassword, email= form.email.data)
      db.session.add(user)
      db.session.commit()
      flash('Edited profile successfully', 'success')
      return redirect(url_for('profile'))
   return render_template('editprofile.html', form=form)
   
# UPDATES PAGE??
@app.route("/post/<int:post_id>")
@login_required
def post(post_id):
   post=Post.query.get_or_404(post_id)
   comments=Comment.query.filter_by(post=post).all()
   form = CommentForm()
   if form.validate_on_submit():
      if form.content.data!='':
         comment=Comment(content= form.content.data, author=current_user, post=post)
         db.session.add(comment)
         db.session.commit()
         flash('Comment posted', 'success')
         return redirect(url_for('post', post_id=post_id, form=form))
   else:
      print(form.errors)
   return render_template('updates.html', post=post, comments=comments, form=form)

# CREATE POST ON UPDATES
@app.route("/post/new", methods=['POST', 'GET'])
@login_required
def newPost():
   form = PostForm()
   if form.validate_on_submit():
      post=Post(title=form.title.data, content= form.content.data, author=current_user)
      db.session.add(post)
      db.session.commit()
      flash('Post made successfully', 'success')
      return redirect(url_for('home'))
   else:
      print(form.errors)
   return render_template('newUpdate.html', form=form)

# EDIT POST PAGE
@app.route("/post/<int:post_id>/edit", methods=['POST', 'GET'])
@login_required
def editPost(post_id):
   post=Post.query.get_or_404(post_id)
   return render_template('editUpdate.html', post=post)

# DELETE POST PAGE
@app.route("/post/<int:post_id>/delete", methods=['POST', 'GET'])
@login_required
def deletePost(post_id):
   post=Post.query.get_or_404(post_id)

# COMMENT ON POST PAGE
@app.route("/post/<int:post_id>/comment", methods=['POST', 'GET'])
@login_required
def comment(post_id):
   post=Post.query.get_or_404(post_id)
   form=CommentForm()
   if form.validate_on_submit():
      comment=Comment(content= form.content.data, author=current_user, post=post)
      db.session.add(comment)
      db.session.commit()
      flash('Comment posted', 'success')
      return redirect(url_for('post', post_id=post_id))
   else:
      print(form.errors)

# ABOUT
@app.route("/about")
def about():
   return render_template('about.html')

#CONTACT US
@app.route('/contact', methods=['GET', 'POST'])
def contact():
   form = ContactForm()
   if form.validate_on_submit():
      # Process form data here (e.g., send an email)
      return redirect(url_for('index'))
   return render_template('contact.html', form=form)

# SUPPORT PAGE
@app.route("/support")
def support():
   pass

# EXPLORE
@app.route("/explore")
def explore():
   pass