import requests
import urllib.request 
import json
import ssl 
import webbrowser 
from flask import Flask, render_template
ssl._create_default_https_context = ssl._create_unverified_context

allUrl='https://airecsim-cdn.cn/rec-v2/REC2007405706/latest.json'
#allUrl='https://airecqa-cdn.cn/rec-v2/REC2009005505/latest.json'
#recCode=input('请输入reccode: ')
#environment=input('请输入录像环境： ')
#allUrl=' https://airec'+environment+'-cdn.cn/rec-v2/'+recCode+'/latest.json'
#函数，请求地址，获取到请求网页的内容，解析成json字符串
def postUrlgetjson(allUrl):
    #print(allUrl)
    requestHtml = urllib.request.urlopen(allUrl)
    requestJSON = json.loads(requestHtml.read())
    return requestJSON   
json1 = postUrlgetjson(allUrl) 
print(json1['url'])
json2=postUrlgetjson(json1['url'])
#print(json2['slots'])
json3=json2['slots']
a=['']
b=[]
n=1
for all in json3:
    mydicts = {}
    #mydicts.setdefault('age',30)
    mydicts["页数"] = '第'+str(n)+'页'
    n=n+1
    mydicts["label"]= all['label']
    mydicts["断点标记"]= all['metadata']['guid']
    mydicts.setdefault('录制分支',[])
    for node in all['nodes']:
        mydict = {}
        mydict["分支ID"]= node['id']
        mydict["章节"]= node['metadata']['slug']
        mydict["分支名称"]= node['label']
        mydict["播放模式"]= node['metadata']['play_mode']
        if 'mutation' in node['metadata'].keys():
            mydict["分支类型"]= node['metadata']['mutation']
        if 'timeout'  in node['metadata'].keys():
            mydict["超时时间"]= node['metadata']['timeout']
        if 'attachment' in node['metadata'].keys():
            for source in node['metadata']['attachment']['sources']:
                if 'fullscreen' in source.keys() and source['fullscreen'] != '':
                    mydict["是否勾选全屏"]= source['fullscreen']
        mydicts["录制分支"].append(mydict)
    for edge in all['edges']:
        if  'expectations' in  edge['metadata'].keys():
            if edge['label'] == '识别结果1'and edge['metadata']['expectations']!='':
                mydicts["识别结果1"]= edge['metadata']['expectations']
            elif edge['label'] == '识别结果2'and edge['metadata']['expectations']!='':
                mydicts["识别结果2"]= edge['metadata']['expectations']
            elif edge['label'] == '识别结果3' and edge['metadata']['expectations']!='' :
                mydicts["识别结果3"]= edge['metadata']['expectations'] 
            else:
                print('')
    b.append(mydicts)    
    
#print(a)
print(b)
app = Flask(__name__)
@app.route("/")
def index():
    #return render_template("new.html",contentList=b)
    return render_template("main.html",contentList=b)
@app.route("/data")
def data():
    return json.dumps(b)
if __name__ == '__main__':
    host = "0.0.0.0"
    port = "8898"
    url = "http://127.0.0.1:%s" % port
    webbrowser.open(url)
    app.debug=True
    app.run(host=host, port=port)
#在浏览器新打开一个tap页面
#webbrowser.open(allUrl,new = 0,autoraise = True )
#https://blog.csdn.net/qq_41619796/article/details/88552029