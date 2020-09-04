学习笔记
django初始化数据库
python manage.py makemigrations
python manage.py migrate

django创建用户
python manage.py shell
from django.contrib.auth.models import User
User.objects.create_user("gtzheng","gtzheng@163.com","gtzheng123")
修改密码
u = User.objects.get(username="gtzheng")                                            
u.set_password('gtzheng456')                                                         
u.save()