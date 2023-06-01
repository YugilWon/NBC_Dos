from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

import sys
import certifi

ca = certifi.where()
client = MongoClient(
   "mongodb+srv://sparta:test@cluster0.8bt9azj.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca
)

db = client.dbsparta