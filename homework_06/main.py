from os import getenv

from flask import Flask, render_template, request, url_for, redirect, flash

from models import db, Course

from forms import CreateCourse

app = Flask(__name__)

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", endpoint="list")
def get_courses():
    courses = Course.query.order_by(Course.id).all()
    return render_template("list.html", courses=courses)


@app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_user():
    form = CreateCourse()

    if request.method == "GET":
        return render_template("add.html", form=form)

    name = form.name.data
    duration = form.duration.data

    course = Course(name=name, duration=duration)
    db.session.add(course)
    db.session.commit()

    flash(f"New course {course.name} added")
    url = url_for("list")
    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True)
