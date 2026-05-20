from flask import Flask, request, jsonify
app = Flask(__name__)

# 根路由（保留！）
@app.route('/')
def index():
    return "✅ 部署成功！"

# 导入网易云解析模块
from api.wyy import *  # 或者导入你需要的具体函数

# 网易云音乐解析接口
@app.route('/api/wyy', methods=['GET'])
def wyy_parse():
    # 这里写你解析的核心逻辑，比如：
    url = request.args.get('url')  # 获取前端传的链接
    result = 你的解析函数(url)    # 调用wyy.py里的解析函数
    return jsonify(result)         # 返回解析结果

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
