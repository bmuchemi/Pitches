from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField ,SubmitField
from wtforms.validators import Required


CATEGORY_CHOICES=[('Interview Pitch','Interview Pitch'), ('Pickup lines','Pickup lines'), ('The Twitter Pitch','The Twitter Pitch')]

class EditProfile(FlaskForm):
    about = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Update')


class PitchForm(FlaskForm):
    pitch_category = SelectField('Choose a category', choices=CATEGORY_CHOICES, validators=[Required()])
    pitch_text = TextAreaField('Your pitch here', validators=[Required()]) 
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    pitch_comment = TextAreaField('Add a new comment', validators=[Required()])
    submit = SubmitField('Comment')
