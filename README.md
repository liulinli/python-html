# python-html
readme 语法：https://www.runoob.com/markdown/md-title.html
#### 思路整理：
1. 用户输入信息读取 input
```python
recCode=input('请输入reccode: ')
```
2. 请求URL并打开网页读取网页信息并解析成json 格式
```python
requestHtml = urllib.request.urlopen(allUrl)
requestJSON = json.loads(requestHtml.read())
```
3. 根据json 文件的格式进行读取
```python
for all in json3:
```
- 存储到列表里面：列表套字典，字典套字典
```python
b=[]
mydicts = {}
    mydicts["label"]= all['label']
    mydicts.setdefault('录制分支',[])
        mydict = {}
            mydict["播放模式"]= node['metadata']['play_mode']
        mydicts["录制分支"].append(mydict)
b.append(mydicts) 
```
4. python与html互传数据，引入flask框架，将列表数据传递到html界面`flask` 还有很多可以尝试的 
```python
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("main.html",contentList=b)
if __name__ == '__main__':
    host = "0.0.0.0"
    port = "8898"
    url = "http://127.0.0.1:%s" % port
    webbrowser.open(url)
    app.debug=True
    app.run(host=host, port=port)
```
5. html界面对传递过来对列表进行读取
```html
{{contentList}}
```
6. 使用css对界面进行了美化(引入的css文件需要修改路径)
```html
<link rel="stylesheet" href="{{ url_for('static',filename='css/main.css') }}">
<script type="text/javascript" src="https://libs.baidu.com/jquery/2.1.1/jquery.min.js"></script>
<script type="text/javascript" src="{{ url_for('static',filename='js/jsmind.js') }}"></script>
```
