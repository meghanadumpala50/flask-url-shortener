from flask_wtf import FlaskForm
from wtforms import validators, StringField


class UrlForm(FlaskForm):
    old = StringField('Title', [
        validators.InputRequired(),
        validators.Length(
            min=4,
            max=2027,
            message="If URL's were that short, would you even be here?"
        )
    ])

    custom = StringField('Custom Alias')

    def save_url(self, url):
        self.populate_obj(url)

        if not url.old.startswith(("http://", "https://")):
            url.old = "https://" + url.old

        return url