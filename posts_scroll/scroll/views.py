from django.shortcuts import render
from django.http import JsonResponse
import time

# Create your views here.
def index(request):
    return render(request, 'scroll/index.html')

def posts(request):

    start = int(request.GET['start'] or 0)
    end = int(request.GET['end'] or 9)

    posts_list = []
    for i in range(start, end+1):
        posts_list.append(f"Post {i}")

    time.sleep(1)

    return JsonResponse({'Posts': posts_list})





