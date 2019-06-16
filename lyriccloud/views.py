from flask import Blueprint,render_template,request
from .lyricPlot import Plot

lyriccloud = Blueprint('lyriccloud',__name__,template_folder='templates',static_folder='./static')

@lyriccloud.route('/',methods=['GET','POST'])
def page_open():
    group = []
    unit = []
    img_data = ''
    if request.method == 'POST':
        group = request.form.getlist('group')
        unit = request.form.getlist('unit')
        img_data = Plot.get_pic(group,unit)

        return render_template('top.html',group=group,unit=unit,img_data=img_data)

    if request.method == 'GET':
        return render_template('top.html',group=group,unit=unit)
