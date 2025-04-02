from flask import Blueprint, render_template, redirect, url_for, request, flash, session, get_flashed_messages
from strike_app import db
from strike_app.strike.models import Striker
from strike_app.strike.forms import StrikeForm
from flask_login import login_required, current_user

strike_blueprint = Blueprint('staking', __name__, template_folder='templates')

### Routes

@strike_blueprint.route("/bedankt", methods=["GET"])
def thanks():
    return render_template("bedankt.html")

@strike_blueprint.route("/", methods=["GET", "POST"])
def index():
    session['_flashes'] = []
    my_form = StrikeForm()

    if request.method == "POST":
        if my_form.validate_on_submit():
            flash("Het formulier is succesvol gePOST")

            session["name"] = my_form.name.data
            session["strike"] = my_form.strike.data
            session["age"] = my_form.age.data
            flash("De gegevens zijn in de sessie opgeslagen")

            new_striker = Striker(name=my_form.name.data, strike=my_form.strike.data, age=my_form.age.data)
            db.session.add(new_striker)
            db.session.commit()
            flash("De gegevens zijn in de database opgeslagen")

            return redirect(url_for("staking.thanks"))
        else:
            flash("Het formulier is niet goed ingevuld")
            
    return render_template("strike.html", form=my_form)

@strike_blueprint.route("/stakers")
@login_required
def strikers():
    rows = Striker.query.all()
    return render_template("strikers.html", rows=rows, user=current_user.username)