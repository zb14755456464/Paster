# Copyright 2019-present Lenovo
# Confidential and Proprietary

import logging

logger = logging.getLogger(__name__)


def service_auth_filter_factory(global_conf):
    def filter(app):
        return ServiceAuthFilter(app)

    return filter


class ServiceAuthFilter(object):

    def __init__(self, app):
        self.app = app


    def __call__(self, environ, start_response):
        print('hahahaahahahahahahahaha')
        print('hahahaahahahahahahahaha')
        print('hahahaahahahahahahahaha')
        print('hahahaahahahahahahahaha')
        print('hahahaahahahahahahahaha')
        print(1111111111111111111111111)
        print(1111111111111111111111111)
        print(1111111111111111111111111)
        print(1111111111111111111111111)
        print(1111111111111111111111111)
        print('zhangbiao zhangbiao zhangbiao')
        print('zhangbiao zhangbiao zhangbiao')
        print('zhangbiao zhangbiao zhangbiao')
        print('zhangbiao zhangbiao zhangbiao')
        print('zhangbiao zhangbiao zhangbiao')
        return self.app(environ, start_response)

