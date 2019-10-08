# paster

基于paster 的中间件认证, 添加记录日志

cd zhangbiao-auth
python setup.py install 

cd zhangbiao
python setup.py install

gunicorn --paster etc/lico-file-manager.ini -c etc/lico-file-manager-gunicorn.conf 

curl http://127.0.0.1/zhangbiao/test/

可以使用配置文档中详细介绍的各种标志 或通过创建日志记录配置文件来配置日志记录
https://github.com/benoitc/gunicorn/blob/master/examples/logging.conf