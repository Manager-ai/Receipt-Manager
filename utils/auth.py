# from flask import Flask, redirect, url_for
# from flask_dance.contrib.google import make_google_blueprint, google
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
# import os
# # Initialize Flask app
# server = Flask(__name__)
# server.secret_key = os.urandom(24)

# client_id = "1011422062791-k61s2f5r07te7h6bb8n86qvgijt26dq5.apps.googleusercontent.com"
# client_secret = "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"
# redirect_url = "http://127.0.0.1:8050/upload"
# # Configure Google OAuth
# google_bp = make_google_blueprint(
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_to="redirect_url"
# )
# server.register_blueprint(google_bp, url_prefix="/login")

# # Configure Flask-Login
# login_manager = LoginManager()
# login_manager.init_app(server)

# # User model
# class User(UserMixin):
#     def __init__(self, id):
#         self.id = id

# @login_manager.user_loader
# def load_user(user_id):
#     return User(user_id)

# # Routes
# @server.route("/")
# def home():
#     return "Home Page"

# @server.route("/login/google")
# def google_login():
#     if not google.authorized:
#         return redirect(url_for("google.login"))
#     resp = google.get("/oauth2/v1/userinfo")
#     assert resp.ok, resp.text
#     user_info = resp.json()
#     user_id = user_info["id"]
#     user = User(user_id)
#     login_user(user)
#     return redirect(url_for("dashboard"))

# @server.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("home"))

# @server.route("/dashboard")
# @login_required
# def dashboard():
#     return "Dashboard Page for logged in users"

# # Protected routes
# @login_manager.unauthorized_handler
# def unauthorized_callback():
#     return redirect('/login/google')

# # Error handling
# @server.errorhandler(500)
# def server_error(e):
#     return "An internal server error occurred", 500
