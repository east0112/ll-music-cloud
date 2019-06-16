from flask import Blueprint,render_template,request
from .lyricPlot import Plot

lyriccloud = Blueprint('lyriccloud',__name__,template_folder='templates',static_folder='./static')

@lyriccloud.route('/',methods=['GET','POST'])
def page_open():
    group = []
    unitM = []
    unitA = []
    img_data = ''
    if request.method == 'POST':
        group = request.form.getlist('group')
        unitM = request.form.getlist('unitM')
        unitA = request.form.getlist('unitA')
        img_data = Plot.get_pic(group,unitM,unitA)

        return render_template('top.html',group=group,unitM=unitM,unitA=unitA,img_data=img_data)

    if request.method == 'GET':
        return render_template('top.html',group=group,unitM=unitM,unitA=unitA)
