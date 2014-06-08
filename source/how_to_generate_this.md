# 怎么才能生成这么一篇文档
## 对于mac
### 安装python

*假设你已经安装了 brew , 如果没有，猛击 [**这里**](http://webmedia.blog.163.com/blog/static/416695020123261226695/)*

```sh
    # 安装python
	sudo brew install python
    # 安装easy_install
	sudo curl https://bootstrap.pypa.io/ez_setup.py -o - | python
	# 安装pip和各种依赖包
	sudo easy_install pip
	sudo pip install markdown
	#还没确定最后用哪个，现在用的是markdown
	sudo pip install markdown2
	sudo pip install pygments 
```

### 安装配置sublime

下载安装破解，天朝优势就不说了，比如 [**就是不要钱1**](http://pan.baidu.com/share/link?shareid=2975870065&uk=2452735089) .
	

安装ok后，Tools -》 Build System -》 new Build System ，输入以下脚本并保存为 markdown.sublime-build

```javascript
	{
		"shell_cmd": "python /Users/otupia/Script/python/mdfolder.py '${file}'"
	}
```

其中的mdfolder.py的路径取决于你存放文件的位置，mdfolder.py的代码：

```python
	# coding=utf-8
import markdown
import shutil
import os,codecs,sys

OUT_PUT_HTML_FLODER = "target/html"
SOURCE_FLODER = "source"
TEMPLATE_HTML = """
<html>
    <head>
        <meta charset='utf-8'>
        <link href="${basedir}/static/emac.css" media="all" rel="stylesheet" type="text/css" />
        <link href="${basedir}/static/markdown.default.css" media="all" rel="stylesheet" type="text/css" />
    </head>
    <body>
        ${body}
    </body>
</html>
"""

def markdownfile(basedir, filepath):
    if(os.path.exists(basedir + "/" + OUT_PUT_HTML_FLODER )):
        shutil.rmtree(basedir + "/" + OUT_PUT_HTML_FLODER)

    inputfile = basedir + "/" + SOURCE_FLODER + "/" + filepath
    outputfile = basedir + "/" + OUT_PUT_HTML_FLODER + "/" + filepath[:filepath.rfind(".")] + ".html"
    outputfolder = outputfile[:outputfile.rfind("/")]

    if(not os.path.exists(outputfolder)):
        os.makedirs(outputfolder)


    print "markdownfile", "from" , inputfile, "to",outputfile
    if(not os.path.exists(inputfile)):
        print "找不到文件： " + inputfile
    else:
        text = readutf8file(inputfile)
        print text.encode("utf-8")
        #html = markdown2.markdown(text, extras=["fenced-code-blocks","wiki-tables"])
        html = markdown.markdown(text, extensions=["extra","codehilite(linenums=True)"])
        print html.encode("utf-8")
       
        html = TEMPLATE_HTML.replace("${body}",html).replace("${basedir}",basedir);
        print html.encode("utf-8")
        outpututf8file(outputfile,html)

def readutf8file(filename):
    input_file = codecs.open(filename, mode="r", encoding="utf-8")
    return input_file.read()
def outpututf8file(filename,text):
    output_file = codecs.open(filename, "w", 
                          encoding="utf-8", 
                          errors="xmlcharrefreplace"
    )
    output_file.write(text)

    

if "__main__" == __name__:
    inputfile = sys.argv[1]
    print inputfile
    basedir = inputfile[:inputfile.find("/source/")]
    filename = inputfile[inputfile.find("/source/") + len("/source/"):]
    print "正在处理项目：",basedir,"  文件： ",filename
    markdownfile(basedir,filename)

```


### 如何使用