from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, "onepage/index.html")

Texts = [
    "Computer science is the study of algorithmic processes, computational machines and computation itself As a discipline, computer science spans a range of topics from theoretical studies of algorithms, computation and information to the practical issues of implementing computational systems in hardware and software.",
    "Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from noisy, structured and unstructured data, and apply knowledge and actionable insights from data across a broad range of application domains.",
    "Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy. ... Machine learning is an important component of the growing field of data science."
]

def section(request, num):
    if num >=1 and num <=3:
        return HttpResponse(Texts[num-1])
    else:
        raise Http404('No such section')


