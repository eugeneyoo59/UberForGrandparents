from flask import (Blueprint, render_template, request, session, url_for)

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route("/", methods=["GET"])
def search():
    if request.method == "GET" :
        return "john"