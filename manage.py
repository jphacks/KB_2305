import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from flask import Flask,render_template, request
import datetime

cred = credentials.Certificate("kb2305-5793d-firebase-adminsdk-vtb9d-db56bdc49e.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kb2305-5793d-default-rtdb.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})
app = Flask(__name__, static_folder='/')

@app.route("/")
def hello():
    ##databaseに初期データを追加する
    modify_data = []
    users_ref = db.reference('/Todos')
    data = users_ref.get()
    dt = datetime.datetime.now()
    if data !=None:
        for i in data:
            unmodify_data = [i['name'],i['todo'],int(i['matrix']),i['category'],str(i['start'][0:10])+ ' ' +str(i['start'][11:16]),str(i['finish'][0:10])+ ' ' +str(i['finish'][11:16]),str(i['deadline'][0:10])+ ' ' +str(i['deadline'][11:16]),i['option']]
            unmodify_data.append(int(i['deadline'][0:4])-int(dt.year))
            modify_data.append(unmodify_data)
    modify_data = sorted(modify_data, reverse=False, key=lambda x: x[2]) 
    modify_data = sorted(modify_data, reverse=False, key=lambda x: x[8]) 
    return render_template("index.html", data = modify_data)

@app.route('/', methods=["GET", "POST"])
def require():
    modify_data = []
    if request.method == 'GET': 
        name = ""
        post_todo = ""
        post_matrix = ""
        post_deadline = ""
        post_start = ""
        post_finish = ""
        post_category = ""
        post_option = ""
        
    elif request.method == 'POST':
        name = request.form.get('name') #完了
        post_todo = request.form.get('todo') #完了
        post_matrix = request.form.get('matrix') #完了
        post_deadline = str(request.form.get('deadline'))
        post_start = str(request.form.get('start'))
        post_finish = str(request.form.get('finish'))
        post_category = request.form.get('category')
        post_option = request.form.get('option')
        
        users_ref = db.reference('/Todos')
        data = users_ref.get()
        if data !=None:
            num = str(len(data))
            users_ref.child(num).set({
                    'name': name,
                    'todo': post_todo,
                    'matrix': post_matrix,
                    'deadline': post_deadline,
                    'start': post_start,
                    'finish': post_finish,
                    'category': post_category,
                    'option': post_option
                
                })
        else:
            users_ref.child('0').set({
                    'name': name,
                    'todo': post_todo,
                    'matrix': post_matrix,
                    'deadline': post_deadline,
                    'start': post_start,
                    'finish': post_finish,
                    'category': post_category,
                    'option': post_option
                
                })
        data = users_ref.get()
        dt = datetime.datetime.now()
        for i in data:
            unmodify_data = [i['name'],i['todo'],int(i['matrix']),i['category'],str(i['start'][0:10])+ ' ' +str(i['start'][11:16]),str(i['finish'][0:10])+ ' ' +str(i['finish'][11:16]),str(i['deadline'][0:10])+ ' ' +str(i['deadline'][11:16]),i['option']]
            unmodify_data.append(int(i['deadline'][0:4])-int(dt.year))
            modify_data.append(unmodify_data)
        modify_data = sorted(modify_data, reverse=False, key=lambda x: x[2]) 
        modify_data = sorted(modify_data, reverse=False, key=lambda x: x[8]) 
    return render_template('index.html', data = modify_data) 

##データを取得する

app.run(debug=True)