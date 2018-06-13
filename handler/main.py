import tornado.web
import os

from utils import photo


class InderHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        images_path = os.path.join(self.settings.get('static_path'),'upload')
        images = photo.get_images(images_path)
        self.render('index.html',images=images)

class ExploreHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        images_path = os.path.join(self.settings.get('static_path'), 'upload')
        images = photo.get_images(images_path)
        self.render('explore.html',images=images)
class PostHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('post.html',post_id=kwargs['post_id'])

class UploadHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('upload.html')

    def post(self, *args, **kwargs):
        static_path = os.path.join(os.getcwd(),'static')
        img_files  = self.request.files.get('Newimg',NameError)
        for img_file in img_files:
            with open(static_path+'/upload/'+img_file['filename'],'wb') as f:
                f.write(img_file['body'])

            self.write({'get file':img_file['filename']})