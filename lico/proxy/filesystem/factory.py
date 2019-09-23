import falcon

class FileManager:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = ('zhangbiao')

def create_app(global_conf, work_space=None):
    api = falcon.API()
    print(11111111111111111)
    print(work_space)

    api.req_options.strip_url_path_trailing_slash = True
    api.add_route('/zhangbiao/test/', FileManager())
    return api

