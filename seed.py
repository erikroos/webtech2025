from strike_app import db, app
from strike_app.strike.models import Striker
from strike_app.auth.models import User
from werkzeug.security import generate_password_hash

new_strikers = [
    Striker(name="Erik", strike="y", age=44),
    Striker(name="Henk", strike="n", age=88)
]

new_user = User(username="admin", password=generate_password_hash("1234"))

with app.app_context():
    # Remove all existing
    Striker.query.delete()
    User.query.delete()
    db.session.commit()
    # Then add new
    db.session.add_all(new_strikers)
    db.session.add(new_user)
    db.session.commit()