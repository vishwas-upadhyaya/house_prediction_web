from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.forms import Form
from django.shortcuts import render,redirect,resolve_url
from django.http import JsonResponse
from .model_related import get_all_locations,get_estimated_price
# Create your views here.
class predict(TemplateView):
    template_name='home.html'
    def post(self,request):
        form=Form(request.POST)
        if form.is_valid():
            print('true')
        return redirect('predict')

class get_location(View):
    def get(self,request):
        id = request.GET.get('ids', None)
        if id is not None:
            locations=get_all_locations()
        else:
            locations=[]
        data={
            'location':locations
        }
        return JsonResponse(data)

class estimate(View):
    def get(self,request):
        sqfeet=request.GET.get('sqfts',None)
        bhk = request.GET.get('bhks', None)
        bath = request.GET.get('baths', None)
        location = request.GET.get('locations', None)
        print(sqfeet,bhk,bath,location)
        price=get_estimated_price(location,sqfeet,bhk,bath)
        data={
            'a':price
        }
        return JsonResponse(data)

