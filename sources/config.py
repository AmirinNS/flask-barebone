# DB
import pymongo
from pymongo import MongoClient

import os, sys

def db_connection(db_type="local"):
	'''db_type = "onsite" (production) | "local" (development)'''
	if db_type=="onsite":
		return MongoClient("mongodb://localhost:27017").example # Change this to remote db
	else:
		return MongoClient("mongodb://localhost:27017").example

if 'FLASK_ENV' in os.environ:
	db_connect = db_connection('local') if str(os.environ['FLASK_ENV']).lower()=="development" else db_connection('onsite')
else:
	db_connect = db_connection('local') if len(sys.argv) > 1 and  str(sys.argv[1]).lower()=="development" else db_connection('onsite')
