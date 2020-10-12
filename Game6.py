# 作者：LFW
# 日期：2020
class Handle
    def callback(self,prefix,name,*args):
        method=getattr(method):return method(*args)
        if callable(method):return method(*args)
    def start(self,name):
        self.callback('start_',name)
    def end(self,name):
        self.callback('end_',name)
    def sub(self,name):
        def subsitution(match):
            result=self.callback('sub_',name,match)
            if result is None:match.ground(0)
            return result
        return subsitution
class HTMLRenderer(Handle):
    def start_document(self):
        print'<html><head><title>...</title></head><bady>'
    def end_document(self):
        print'</body></html>'
    def start_paragraph(self):
        print'</p'
    def end_paragraph(self):
        print'</p>'
    def start_heading(self):
        print'<h2>'
    def end_heading(self):
        print'</h2>'
    def start_list(self):
        print'<u1>'
    def end_list(self):
        print'</u1>'
    def start_listitem(self):
        print'<li>'
    def end_listitem(self):
        print'</li>'
    def start_title(self):
        print'<h1>'
    def end_title(self):
        print'</h1>'
    def sub_emphasis(self,match):
        return'<em>%<em>'%match.ground(1)
    def sub_ur1(self,match):
        return'<a href="mailto:%s">%s</a>'%(match.ground(1),match.ground(1))
    def feed(self,data):
        print data
        