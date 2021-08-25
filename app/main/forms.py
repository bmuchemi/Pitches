from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField ,SubmitField
from wtforms.validators import Required


CATEGORY_CHOICES=[('Blog Pitch','Blog Pitch'), ('Pickup lines','Pickup lines'), ('Jokes','Jokes')]

class EditProfile(FlaskForm):
    about = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Update')


class PitchForm(FlaskForm):
    pitch_category = SelectField('Choose a category', choices=CATEGORY_CHOICES, validators=[Required()])
    pitch_text = TextAreaField('Entre pitch', validators=[Required()]) 
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    pitch_comment = TextAreaField('Make a new comment', validators=[Required()])
    submit = SubmitField('Comment')