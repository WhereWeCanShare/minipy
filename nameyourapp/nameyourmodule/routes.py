from flask import Blueprint

yourmodule = Blueprint('yourmodule', __name__)

@yourmodule.route('/')
def yourmodule_main():
    return '<div align="center"><img src="https://source.unsplash.com/1200x800/?technology,matrix,hacker,women"><p>Thanks Unsplash for nice photo</p></div>', 200
