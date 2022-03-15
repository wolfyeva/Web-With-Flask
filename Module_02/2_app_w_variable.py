from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/user/<username>')
def show_user_profile(username):
    # 顯示使用者的個人資料，如名字
    return '<h1>Hello, %s</h1>' % escape(username)

@app.route('/user')
def user_page():
    return '<h1>現在進入的是 /user 路由</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 顯示文章編號，文章編號是整數
    return f'文章編號為：{post_id}'

@app.route('/temp/<float:temp_value>')
def show_post(temp_value):
    # 顯示溫度數值，溫度是浮點數
    return f'現在溫度為：{temp_value}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 顯示包含 '/' 符號的字串，視為路徑(path)
    return 'Subpath %s' % escape(subpath)
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug= True)
