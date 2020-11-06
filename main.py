from flask import Flask
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


from controllers.books_controller import books
app.register_blueprint(books)

