from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Length


class CreateCourse(FlaskForm):
    name = StringField(
        label="Name",
        name="name",
        validators=[InputRequired(),
                    Length(min=4, max=30)])
    duration = IntegerField(
        label="Duration (hours)",
        name="duration",
        validators=[InputRequired()])


