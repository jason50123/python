from flask import Flask
from flask import request
from flask import redirect
import json

app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
    ) 


@app.route("/")
def home():
    print("請求方法",request.method)    
    print("通訊協定",request.scheme)
    print("主機名稱",request.host)
    print("路徑",request.path)
    print("完整的網址",request.url)
    print("瀏覽器和作業系統",request.headers.get("user-agent"))
    print("語言偏好",request.headers.get("accept-language"))
    print("引薦網址",request.headers.get("referrer"))
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en")
    else:
        return redirect("/zh_tw")

@app.route("/test")
def test():
    return "This is test page"

@app.route("/getSum")
def getSum():
    number = request.args.get("max",50)
    number = int(number)
    result = 0
    answer = []
    for i in range(1,number+1):
        result += i
        answer.append(result)
    return  "結果 : " + str(answer)

@app.route("/en")
def engVer():
    return json.dumps({
        "status":"ok",
        "text" :"welecome to my website"
        })

@app.route("/zh_tw")
def chVer():
    return json.dumps({
        "status" : "ok",
        "text" : "歡迎來到我的網站"
        },ensure_ascii=False)


if __name__ == "__main__":
    app.run()