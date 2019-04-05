#验证flask模块的py文件
#发现系统在5000端口开启web服务，直接访问http://127.0.0.1:5000/
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world!'
if __name__ == '__main__':
    app.run()