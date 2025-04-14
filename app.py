from flask import Flask, render_template
from signup import signup_bp  # Ensure signup is a Blueprint
from login import login_bp    # Ensure login is a Blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)

if __name__ == '__main__':
    app.run()

