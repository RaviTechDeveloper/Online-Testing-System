from urllib import request
from winreg import REG_RESOURCE_REQUIREMENTS_LIST
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from OTS.models import Question,User
import random
# from firstproject.OTS.models import 

# # Create your views here.
def createAdmin():
    user=User()
    user.username="admin"
    user.password="password"
    user.role="ADMIN"
    user.realname="Super User"
    user.save()
def startTest(request):
    no_of_que=5
    questions_pool=list(Question.objects.all())
    random.shuffle(questions_pool)
    questions_list=questions_pool[:no_of_que]    
    res=render(request,'OTS/start_test.html',{'questions':questions_list})
    return res
def testResult(request):
    total_attempt=0
    total_right=0
    total_wrong=0
    qno_list=[] 
    for k in request.POST:
        if k.startswith("qno"):
            qno_list.append(int(request.POST[k]))
    for n in qno_list:
        question=Question.objects.get(qno=n)    
        try: 
            if question.answer==request.POST['q'+str(n)]:
                total_right+=1
            else:
                total_wrong+=1
            total_attempt+=1
        except:
            pass
    d={'total_attempt':total_attempt,'total_right':total_right,'total_wrong':total_wrong}  
    res=(render(request,'OTS/test_result.html',d))
    return res   
def signup(request):
    d1={} 
    try:
        print("My Error Value:",request.GET['error'])                  
        if request.GET['error']==str(1):
            d1['errmsg']='Username already taken'
    except:
            d1['errmsg']=''
    res=render(request,'OTS/signup.html',d1)
    return res    

# def home(request):
#     try:

#         realname=request.session['realname']
#     except KeyError:
#         return HttpResponseRedirect("http://localhost:8000/OTS/login")    
#     res=render(request,'OTS/home.html',{'realname':realname})
#     return res
def home(request):
    try:
        realname=request.session['realname']    
    except KeyError:
        return HttpResponseRedirect("http://localhost:8000/OTS/login/")
    res = render(request,'OTS/home.html')
    return res    
# def signup(request):
#     d1={}
#     try:
#        print("My Error Value: ",request.GET['error'])
#        if request.GET['error']==str(1):  
#            d1['errmsg']='username already taken'
#     except:
#         d1['errmsg']=''       
#     res=render(request,'OTS/signup.html',d1)
#     return res                  
def saveUser(request):
    user=User()
    u=User.objects.filter(username=request.POST['username'])
    if not u:
        user.username=request.POST['username']
        user.password=request.POST['password']
        user.realname=request.POST['realname']
        user.role="LEARNER"
        user.save()
        url="http://localhost:8000/OTS/login/"
    else:
        url="http://localhost:8000/OTS/signup?error=1" 
    return HttpResponseRedirect(url)
def logout(request):
    request.session.clear()
    return HttpResponseRedirect("http://localhost:8000/OTS/login/")
def login(request):
    user=User.objects.filter(username="admin")
    if not user:
        createAdmin()
    res=render(request,'OTS/login.html')
    return res
def loginValidation(request):
    # user=User()
    # user=User.objects.filter(username=request.POST['username'],password=request.POST['password'])
    try:
        user=User.objects.get(username=request.POST['username'],password=request.POST['password'])
        # user=User.objects.get(username=request.POST['username'])
        request.session['username']=user.username
        request.session['realname']=user.realname
        request.session['role']=user.role
        url="http://localhost:8000/OTS/home/"
    except:
        url="http://localhost:8000/OTS/login/"
        userNotValidated = True
        return render(request,'OTS/login.html',{'userNotValidated':userNotValidated})

    return HttpResponseRedirect(url) 
    # print(type(user))
    # if user:  #login successful
    #     request.session['username']=user.username 
    #     request.session['realname']=user.realname  
    #     url="http://localhost:8000/OTS/home/"   
    # else:
    #     url="http://localhost:8000/OTS/login/"  
    # return HttpResponseRedirect(url)                                 
def newQuestion(request):
    res=render(request,'OTS/new_question.html')
    return res
def saveQuestion(request):
    question=Question()
    print(request.POST['question'])
    question.que = request.POST['question']
    question.optiona = request.POST['optiona']
    question.optionb = request.POST['optionb']
    question.optionc = request.POST['optionc']
    question.optiond = request.POST['optiond']
    question.answer = request.POST['answer']
    print(question.que)
    question.save() 
    return HttpResponseRedirect('http://localhost:8000/OTS/view_questions/')

def viewQuestions(request):
    questions = Question.objects.all()
    # print(questions)
    print(questions[0].optiona)
    res=render(request,'OTS/view_question.html',{'questions':questions})
    return res
def  editQuestion(request):
    q=request.GET['qno']
    question=Question.objects.get(qno=int(q))
    res=render(request,'OTS/edit_question.html',{'question':question})
    return res
def editsaveQuestion(request):
    question=Question()
    question.qno=request.POST['qno']
    question.que=request.POST['question']
    question.optiona=request.POST['optiona']
    question.optionb=request.POST['optionb']
    question.optionc=request.POST['optionc']
    question.optiond=request.POST['optiond']
    question.answer=request.POST['answer']
    question.save()
    return HttpResponseRedirect('http://localhost:8000/OTS/view_questions/')
def deleteQuestion(request):
    q=request.GET['qno']
    question=Question.objects.filter(qno=int(q))
    question.delete()
    return HttpResponseRedirect('http://localhost:8000/OTS/view_questions/')
    
