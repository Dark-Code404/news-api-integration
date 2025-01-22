from datetime import datetime
import json
from django.shortcuts import render
import requests
from decouple import config




# Create your views here.
def home(request):
    api_key=config('api_key')
  
    q = request.GET.get('q') 
    if q is None or q == '':
        q='us'
    category = request.GET.get('category', '')


    if category:
        url = f'https://newsapi.org/v2/top-headlines?country={q}&category={category}&apiKey={api_key}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?country={q}&apiKey={api_key}'
    
    response = requests.get(url)
    data=  response.json() 
                                
                         
    

    
    if 'articles' in data:
        articles = data['articles']
        for art in articles:
            publish = art['publishedAt']
            art['date'] = datetime.strptime(publish, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
    else:
        articles = []
        



    context={"data":data,"articles":articles,"category":category}
    
    return render(request,"index.html",context)