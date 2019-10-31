import falcon
import os


class FileManager:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = ('zhangbiao')

def create_app(global_conf, work_space=None):
    api = falcon.API()
    print(work_space)

    api.req_options.strip_url_path_trailing_slash = True
    api.add_route('/zhangbiao/test/', FileManager())
    return api

def create_webdav_app(
        global_config,
        mount_path='/api/file/webdav',
        workspace=None
):
    from wsgidav.wsgidav_app import WsgiDAVApp
    from wsgidav.dir_browser import WsgiDavDirBrowser
    from wsgidav.error_printer import ErrorPrinter
    from wsgidav.request_resolver import RequestResolver
    from wsgidav.fs_dav_provider import FilesystemProvider

    if workspace is None:
        workspace = os.getcwd()

    config = dict(
        mount_path=mount_path,
        provider_mapping={
            '/': FilesystemProvider(workspace)
        },
        middleware_stack=[
            ErrorPrinter,
            WsgiDavDirBrowser,
            RequestResolver,
        ],
        verbose=2
    )

    return WsgiDAVApp(config)
