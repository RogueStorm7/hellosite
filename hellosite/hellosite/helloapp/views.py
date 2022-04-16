from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return render(request=request, template_name='hello_world.html')
        
class HelloView(View):
    def get(self, request, name='world'):
        context = {'name': name}
        return render(
            request=request, template_name='hello_name.html', context=context,
        )  

class GoodbyeWorldView(View):
  def get(self, request):
    return render(request=request, template_name='goodbye_world.html')

class GoodbyeView(View):
  def get(self, request, name='name'):
    context = {'name':name}
    return render(
      request=request, template_name='goodbye_name.html', 
      context=context
    )