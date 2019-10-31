import webdav3.client as wc
from io import BytesIO
from webdav3.client import Client

class WebDev(object):
    def __init__(self, options ):
        # self.client = wc.Client(options)
        self.client = Client(options)


    def read(self, name):
        with BytesIO() as buf:
            self.client.download_from(buf, name)
            return buf.getvalue()


    def write(self,content, target):
        data = self.read(target)

        with BytesIO() as buf:
            buf.write(data)
            buf.write(content.encode())
            self.client.upload_to(buf.getvalue(), target)


    def mkdir(self, dir_name):
        self.client.mkdir(dir_name)


    def list(self):
        data = self.client.list()
        print(data)


    def clear(self, target):
        self.client.clean(target)


    def check(self,remote_path):
        data = self.client.check(remote_path)
        if data:
            print('{} is exists'.format(remote_path))
        else:
            print('{} is not exists'.format(remote_path))


    def upload(self,remote_path, local_path):
        self.client.upload(remote_path, local_path)


    def help_dev(self):
        print(dir(self.client))


    def mkfile(self, remote_path):
        with BytesIO() as buf:
            buf.write(b'')
            self.client.upload_to(buf.getvalue(), remote_path)


    def download_file(self, remote_path):
        self.client.download_file(remote_path, remote_path)


    def rename(self, old_name, new_name):
        self.client.copy(old_name, old_name)
        self.client.clean(old_name)


    def set_property(self,remote_path, option):
        self.client.set_property(remote_path, option=[option])



if __name__ == '__main__':
    options = {
        'webdav_hostname': "http://10.104.204.21:80",
        'webdav_root': '/api/file/webdav/'
    }

    dev = WebDev(options)
    dev.list()

    # dev.clear('hello')
    # dev.clear('coco.txt')
