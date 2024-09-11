from flask import Blueprint, render_template
from .models import Category

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    categories = Category.query.all()
    return render_template("index.html", categories=categories)
