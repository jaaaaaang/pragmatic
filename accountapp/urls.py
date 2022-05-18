from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import hello_world, test, AccountCreateView

#"127.0.0.1:8000/account/hello_world"  <-- 이렇게 들어와야 하는데
#app_name 을 만들어 줌으로써  접급이 용이해짐... 나중에 ..

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),
    #path('', hello_world, name = 'hello_world'),
    path('test/', test, name = 'test'),
    path('create/', AccountCreateView.as_view(), name='create'),  #view.py에서 class를 사용한 경우 .as_view()를 붙여주라
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'), #template 설정을 해줘야 함
    path('logout/', LogoutView.as_view(), name='logout')
]
