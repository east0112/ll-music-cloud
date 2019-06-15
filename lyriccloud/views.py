from flask import Blueprint,render_template,request
lyriccloud = Blueprint('lyriccloud',__name__,template_folder='templates',static_folder='./static')

@lyriccloud.route('/',methods=['GET','POST'])
def page_open():
    if request.method == 'POST':
        group = request.form.getlist('group1')
        unitM = request.form.getlist('unitM')
        unitA = request.form.getlist('unitA')

    return render_template('top.html')

#@lyriccloud.route('/',methods=['POST'])
#def exec_cloud():
    # POSTメソッド（実行ボタン）処理時
    #request.method == "POST":
#    group = request.form.getlist('group1')
    #group = result['group']
    #unitM = request.form["unitM"]
    #unitA = request.form["unitA"]

#    return render_template('top.html')
