from flask_login import login_required,current_user
from . import main
from flask import render_template,request,redirect,url_for, abort
from ..models import User,Pitches,Comments
from .forms import EditProfile, PitchForm, CommentForm
from .. import db




@main.route('/newpitch', methods=['GET','POST'])
@login_required
def pitch_form():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        category=pitch_form.pitch_category.data
        text = pitch_form.pitch_text.data
        new_pitch = Pitches(category=category, text=text, user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.home'))
    return render_template('newpitch.html', pitch_form=pitch_form, )


@main.route('/user/<name>', methods=['GET','POST'])
@login_required
def profile(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)

    form=EditProfile()
    if form.validate_on_submit():
        user.about=form.about.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', name=user.username))
    return render_template('profile/profile.html', user=user, form=form)


