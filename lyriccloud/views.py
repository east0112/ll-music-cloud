from flask import Blueprint,render_template,request
lyriccloud = Blueprint('lyriccloud',__name__,template_folder='templates',static_folder='./static')

@lyriccloud.route('/')
def index():
    return render_template('top.html')
