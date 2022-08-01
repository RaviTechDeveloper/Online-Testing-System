from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testPaper(request):
    q="who is prime minister of india"
    a="Rahul ghandhi"
    b="Narendra modi"
    c="adityanath"
    d="piyush goyal"
    d1={'que':q,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/show_test.html',d1)
    return res
def testResult(request):
    s="Test Result"
    return HttpResponse(s)    