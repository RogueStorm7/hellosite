from django.urls import path
from helloapp.views import HelloWorldView, HelloView, GoodbyeView, GoodbyeWorldView


urlpatterns = [
    ## helloapp/
    # path('', HelloWorldView.as_view(), name='hello_world'),
    # path('<name>', HelloView.as_view(), name='hello_name'),
    path('', GoodbyeWorldView.as_view(), name='goodbye_world'),
    path('<name>', GoodbyeView.as_view(), name='goodbye_name'),
]