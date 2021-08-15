from flask_login import login_required,current_user
from . import main
from ..models import User,Pitches,Comments




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