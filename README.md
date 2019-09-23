# paster

基于paster 的中间件认证

cd zhangbiao-auth
python setup.py install 

cd zhangbiao
python setup.py install

gunicorn --paster zhangbiao/etc/config.ini