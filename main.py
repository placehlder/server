from app import app, db
from app.routes import auth

app.register_blueprint(auth)

from app.models import User


if __name__ == "__main__":
    db.create_all()
    db.session.add(User(username="pakt", password="test", lastlogin=0))
    app.run()