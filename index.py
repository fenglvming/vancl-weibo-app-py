import web
import os,sys
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
import view
from view import render
urls = ('/','index')

class index:
    def GET(self):
        return render.index('fenglvming')
  
app = web.application(urls, globals(), autoreload=False)
app.internalerror = web.debugerror
application = app.wsgifunc()