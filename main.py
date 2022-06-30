from app import app
from app.routes import auth

app.register_blueprint(auth)

print(app.url_map)

if __name__ == "__main__":
    app.run()