# paster

基于paster 的中间件认证, 添加记录日志

cd zhangbiao-auth
python setup.py install 

cd zhangbiao
python setup.py install

gunicorn --paster etc/lico-file-manager.ini -c etc/lico-file-manager-gunicorn.conf 

curl http://127.0.0.1/zhangbiao/test/
