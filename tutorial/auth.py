from flask import (Blueprint, render_template, request, session, url_for)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/did", methods=["GET"])
def get_page():
    if request.method == "GET" :
        return render_template("auth/auth.html")

      