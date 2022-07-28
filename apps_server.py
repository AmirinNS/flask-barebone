import json, os, requests, string, re, traceback, sys

# Import datetime related
import datetime as dtime, time
from datetime import datetime

# Server
from flask import Flask, app, request, abort, url_for, send_from_directory, jsonify, make_response, render_template
from paste import httpserver

# DB
import pymongo
from sources.config import db_connect as db
from bson.objectid import ObjectId

# Import sources
from sources.variable import HOST, PORT

''' INIT '''
apps = Flask(__name__)

''' ROUTES '''
@apps.errorhandler(500)
def is_error_500(error):
	return render_template("error.html", title="Internal Error", message="Sorry, the page that you requested encounter error. Please try again"), 500

@apps.errorhandler(403)
def is_error_403(error):
	return render_template("error.html", title="Forbidden Access", message="Sorry, the page that you requested encounter error. Please try again"), 403

# # HTTP access
@apps.errorhandler(404)
def is_error_404(error):
	return render_template("error.html", title="Page Not Found", message="The page that your requested is not exist"), 404

@apps.errorhandler(401)
def is_error_401(error):
	return render_template("error.html", title="Unauthorised Error", message="Sorry, the page that you requested encounter error. Please try again"), 401

# @apps.get("/") or @apps.route("/", methods=['GET'])
@apps.route("/")
def index():
	return render_template("bootstrap_example.html", title="Bootstrap Template")

@apps.get("/example")
def example():
	return render_template("bootstrap_example.html", title="Bootstrap Template")

# Static files
@apps.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(apps.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Folder static automatically served

# Run server using paste
# To run development server, use command `flask run` instead
# refer https://flask.palletsprojects.com/en/2.0.x/server/ for more info
if __name__ == '__main__':
	httpserver.serve(apps, host=HOST, port=PORT)

