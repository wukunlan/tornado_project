import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import os

from handler import main

define('port', default='8000', help='please chose a number port',type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',main.InderHandler),
            (r'/explore',main.ExploreHandler),
            (r'/post/(?P<post_id>[0-9]{2})',main.PostHandler),
            (r'/upload',main.UploadHandler),
        ]
        settings = dict(
            debug=True,
            template_path='templates',
            static_path='static'
        )
        super(Application,self).__init__(handlers,**settings)
    def ceshi(self):
        print('带入自己的私货')

appliaction = Application()

if __name__ == '__main__':
    tornado.options.parse_command_line()
    appliaction.listen(options.port)
    print('Server start on port:%s' % (str(options.port)))
    print(os.path.join(os.getcwd(), 'templates'))
    tornado.ioloop.IOLoop.current().start()
