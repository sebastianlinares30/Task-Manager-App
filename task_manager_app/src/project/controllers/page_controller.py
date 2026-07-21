"""
Controller for displaying the application's HTML pages.
"""

from flask import Blueprint, render_template


page_bp = Blueprint("pages", __name__)


@page_bp.route("/", methods=["GET"])
def index_page():
    """Display the initial page."""
    return render_template("index.html")


@page_bp.route("/index.html", methods=["GET"])
def index_html_page():
    """Display the initial page using the HTML filename."""
    return render_template("index.html")


@page_bp.route("/login.html", methods=["GET"])
def login_page():
    """Display the login page."""
    return render_template("login.html")


@page_bp.route("/sign_up.html", methods=["GET"])
def sign_up_page():
    """Display the sign-up page."""
    return render_template("sign_up.html")


@page_bp.route("/dashboard.html", methods=["GET"])
def dashboard_page():
    """Display the dashboard page."""
    return render_template("dashboard.html")


@page_bp.route("/add_task.html", methods=["GET"])
def add_task_page():
    """Display the add-task page."""
    return render_template("add_task.html")