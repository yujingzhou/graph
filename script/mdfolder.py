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






