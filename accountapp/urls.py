from django.urls import path

from accountapp.views import hello_world
from accountapp.views import test

#"127.0.0.1:8000/account/hello_world"  <-- 이렇게 들어와야 하는데
#app_name 을 만들어 줌으로써  접급이 용이해짐... 나중에 ..

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),
    #path('', hello_world, name = 'hello_world'),
    path('test/', test, name = 'test')
]
