from flask import (Blueprint, render_template, request, session, url_for)
from config import config
import pyrebase

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/did", methods=["GET"])
def get_page():
    if request.method == "GET" :
        return render_template("auth/auth.html")

@bp.route("/register/<id>/<pw>", methods=["GET"])
def register_user(id, pw):
    email = id + "@xxx.com"
    password = pw
    auth.create_user_with_email_and_password(email, password)

    return "Successfully registered with ID!"

#we need to maintain login state via token
@bp.route("/login/<id>/<pw>", methods=["GET"])
def login(id, pw):
    email = id + "@xxx.com"
    password = pw
    user = auth.sign_in_with_email_and_password(email, password)
    #return user["idToken"]
    return user

@bp.route("/getInfo", methods=["GET"])
def getInfo():
    userToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjVhNTA5ZjAxOWY3MGQ3NzlkODBmMTUyZDFhNWQzMzgxMWFiN2NlZjciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdWJlcmZvcmdyYW5kcGFyZW50cyIsImF1ZCI6InViZXJmb3JncmFuZHBhcmVudHMiLCJhdXRoX3RpbWUiOjE2NzU1MTYyNjYsInVzZXJfaWQiOiJzTE9zY29zN2ZwUWNLU1lXSGtwYXVDcTdZSDMzIiwic3ViIjoic0xPc2NvczdmcFFjS1NZV0hrcGF1Q3E3WUgzMyIsImlhdCI6MTY3NTUxNjI2NiwiZXhwIjoxNjc1NTE5ODY2LCJlbWFpbCI6ImV1Z2VuZXlvb0B4eHguY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImV1Z2VuZXlvb0B4eHguY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.bZUjOQUuv1LNt1GtVy8zIjkO7-__7-EHCsLFKwhSrFz-pxV3GPNYYqakGV0-T4J8YvIjjWkdXfKtLmQJGsAez9YOcvLfzQNXCe1F2-7rzaFA_vC_sbCcK-d4YrVCadj1x6S9CoHbAjC53-UcxLmlU2qAKUVgfLRT-CWBlygWKo4lFSvOhyVvesgTExMVh9IStKQC-fI_QASL0MD2JV77h899j3hp-nLrhv8yowPChdQS_bIzvjCLc7f94fMA5ksrVnD1aZZMfAG_m3Yg6iWUi7R1xOD7D3ESsUmZ-M_sLxDbNH8qWr70wwo_hl1Lo-0Yx2E4SJLHr9Gw-VwsKnEjrQ"
    res = auth.get_account_info(userToken)
    return res

@bp.route("/setUserInfo", methods=["GET"])
def setInfo():
    userToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjVhNTA5ZjAxOWY3MGQ3NzlkODBmMTUyZDFhNWQzMzgxMWFiN2NlZjciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdWJlcmZvcmdyYW5kcGFyZW50cyIsImF1ZCI6InViZXJmb3JncmFuZHBhcmVudHMiLCJhdXRoX3RpbWUiOjE2NzU1MTYyNjYsInVzZXJfaWQiOiJzTE9zY29zN2ZwUWNLU1lXSGtwYXVDcTdZSDMzIiwic3ViIjoic0xPc2NvczdmcFFjS1NZV0hrcGF1Q3E3WUgzMyIsImlhdCI6MTY3NTUxNjI2NiwiZXhwIjoxNjc1NTE5ODY2LCJlbWFpbCI6ImV1Z2VuZXlvb0B4eHguY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImV1Z2VuZXlvb0B4eHguY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.bZUjOQUuv1LNt1GtVy8zIjkO7-__7-EHCsLFKwhSrFz-pxV3GPNYYqakGV0-T4J8YvIjjWkdXfKtLmQJGsAez9YOcvLfzQNXCe1F2-7rzaFA_vC_sbCcK-d4YrVCadj1x6S9CoHbAjC53-UcxLmlU2qAKUVgfLRT-CWBlygWKo4lFSvOhyVvesgTExMVh9IStKQC-fI_QASL0MD2JV77h899j3hp-nLrhv8yowPChdQS_bIzvjCLc7f94fMA5ksrVnD1aZZMfAG_m3Yg6iWUi7R1xOD7D3ESsUmZ-M_sLxDbNH8qWr70wwo_hl1Lo-0Yx2E4SJLHr9Gw-VwsKnEjrQ"
    res = auth.get_account_info(userToken)
    email = res["users"][0]["email"]
    id = email.split("@")[0]
    new_data = {"addresa": "the white "}
    real_user_info = db.child("users").child(id).update(new_data)
    #replace update to set to "rewrite" all values under ID
    # replace update to push to append a random key under ID, and then put new_data udner that random unique ID
    return real_user_info

@bp.route("/future/register", methods=["POST"])
def register():
    params = request.get_json()
    id = params["id"]
    pw = params["pw"]
    email = id + "@xxx.com"
    user = auth.sign_in_with_email_and_password(email, pw)
    session.clear()
    session["IdToken"] = user["idToken"]
    return "good"