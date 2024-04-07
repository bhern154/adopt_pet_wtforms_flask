"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, DataRequired, NumberRange, AnyOf, URL, Optional

class PetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("NAME OF PET*", validators=[InputRequired()]) #string
    species = StringField("SPECIES*", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])]) #string
    photo_url = StringField("PHOTO URL", validators=[Optional(), URL()]) #string
    age = IntegerField("AGE", validators=[Optional(), NumberRange(min=0, max=30)]) #integer
    notes = StringField("TELL US MORE") #string
    available = SelectField("IS YOUR PET AVAILABLE?*", choices=[(True, 'Yes'), (False, 'No')], validators=[DataRequired()]) #boolean

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    name = StringField("NAME OF PET*", validators=[InputRequired()]) #string
    species = StringField("SPECIES*", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'])]) #string
    photo_url = StringField("PHOTO URL", validators=[Optional(), URL()]) #string
    age = IntegerField("AGE", validators=[Optional(), NumberRange(min=0, max=30)]) #integer
    notes = StringField("TELL US MORE") #string
    available = SelectField("IS YOUR PET AVAILABLE?*", choices=[(True, 'Yes'), (False, 'No')], validators=[DataRequired()]) #boolean
