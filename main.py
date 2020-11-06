from flask import Flask, jsonify, request
from dotenv import load_dotenv
from database import cursor, connection
load_dotenv()


app = Flask(__name__)


