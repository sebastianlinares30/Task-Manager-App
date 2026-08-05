from flask import Flask
from flask_cors import CORS

from core.router import register_routes


app = Flask(
   __name__,
    template_folder="views",
    static_folder="static"
)

app.secret_key = "task-manager-secret-key"

CORS(app)

register_routes(app)


if __name__ == "__main__":
    app.run(debug=True)