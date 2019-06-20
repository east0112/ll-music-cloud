from flask import Blueprint,render_template,request,Flask
from .lyricPlot import Plot
#2019/06/20 ADD START モバイル端末対応
from user_agents import parse
#2019/06/20 ADD END

lyriccloud = Blueprint('lyriccloud',__name__,template_folder='templates',static_folder='./static')

@lyriccloud.route('/',methods=['GET','POST'])
def page_open():
    group = []
    unit = []
    img_data = ''
    #2019/06/20 ADD START モバイル端末対応
    #ユーザエージェントの情報取得
    app = Flask(__name__)
    user_agent = request.headers.get('User-Agent')
    mobile_flag = parse(user_agent).is_mobile
    #2019/06/20 ADD END

    if request.method == 'POST':
        group = request.form.getlist('group')
        unit = request.form.getlist('unit')
        img_data = Plot.get_pic(group,unit)
        #2019/06/20 ADD START モバイル端末対応
        if mobile_flag:
            return render_template('top_mobile.html',group=group,unit=unit,img_data=img_data)
        else:
            return render_template('top.html',group=group,unit=unit,img_data=img_data)
        #2019/06/20 ADD END

    if request.method == 'GET':
        #2019/06/20 ADD START モバイル端末対応
        if mobile_flag:
            return render_template('top_mobile.html',group=group,unit=unit)
        else:
            return render_template('top.html',group=group,unit=unit)
        #2019/06/20 ADD END
