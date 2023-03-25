from django.shortcuts import render,redirect
import urllib.request, json 
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from .models import UserAnswerSheet,UserInfo
# Create your views here.
def get_longest_list(lst):
    return max(lst, key=len)

class QuestionList(View):
    def get(self, request):
            user=request.session.get('user_id',default=False)
            if user ==  False:
                return redirect('register')
            else:
                user_name=UserInfo.objects.get(id=request.session.get('user_id'))
                url='http://127.0.0.1:5050/static/json/sentences.json/'
                # url='http://127.0.0.1:8001/static/json/sentences.json/'
                with urllib.request.urlopen(f"{url}") as url:
                    data = json.loads(url.read().decode())

                question_list = []
                for key, value in data.items():
                    dict_1 = {}
                    dict_1[key]=data[key]
                    question_list.append(dict_1)

                new_list_1 = question_list[::2]
                new_list_2 = question_list[1::2]

                final_data = []
                for i in range(40):
                    l = []
                    l.append(new_list_1[i])
                    l.append(new_list_2[i])
                    final_data.append(l)    
                
                
                return render(request,'question.html',{'data':final_data,'name':user_name.name.upper()})
    def post(self,request):
        user=request.session.get('user_id',default=False)
        if user == False:
            return redirect('register')
        else:
            x=range(80)     
            style_1=[]
            style_2=[]
            style_3=[]
            style_4=[] 
            final_lst=[]  

            for i in x[1:80:2]:
                num=int(request.POST[f'ques_{i}'])
                if num in [1,8,9,13,17,24,26,31,33,40,41,48,50,53,57,63,65,70,74,79]:
                    style_1.append(num)
                elif num in [2,7,10,14,18,23,25,30,34,37,42,47,51,55,58,62,66,69,75,78]:
                    style_2.append(num)
                elif num in [3,6,11,15,19,22,27,29,35,38,43,46,49,56,59,64,67,71,76,80]:
                    style_3.append(num)
                else:
                    style_4.append(num)
      
            final_lst.append(style_1)
            final_lst.append(style_2)
            final_lst.append(style_3)
            final_lst.append(style_4)
            user=UserInfo.objects.get(pk=request.session.get('user_id'))
            a=get_longest_list(final_lst)
            style1=len(style_1)
            style2=len(style_2)
            style3=len(style_3)
            style4=len(style_4)

            if a == style_1:
                ans=" ".join([' '.join([str(c) for c in lst]) for lst in final_lst])
                user_ans_sheet=UserAnswerSheet.objects.create(user=user,answer_key=ans,style='style_1')
                user_ans_sheet.save()
                del request.session['user_id']
                
                
                data={

                    'name':user.name,
                    'position':user.position,
                    'style1':style1,
                    'style2':style2,
                    'style3':style3,
                    'style4':style4,
                    'ans':ans,
                    'style':user_ans_sheet.style,

                }
                return render(request,'user_answer_list.html',data)
            elif a == style_2:
                ans=" ".join([' '.join([str(c) for c in lst]) for lst in final_lst])
                user_ans_sheet=UserAnswerSheet.objects.create(user=user,answer_key=ans,style='style_2')
                user_ans_sheet.save()
                del request.session['user_id']
                
                data={

                    'name':user.name,
                    'position':user.position,
                    'ans':ans,
                    'style':user_ans_sheet.style,
                    'style1':style1,
                    'style2':style2,
                    'style3':style3,
                    'style4':style4,

                }
                return render(request,'user_answer_list.html',data)
            elif a==style_3:
                ans=" ".join([' '.join([str(c) for c in lst]) for lst in final_lst])
                user_ans_sheet=UserAnswerSheet.objects.create(user=user,answer_key=ans,style='style_3')
                user_ans_sheet.save()
                del request.session['user_id']
                
                data={

                    'name':user.name,
                    'position':user.position,
                    'ans':ans,
                    'style1':style1,
                    'style2':style2,
                    'style3':style3,
                    'style4':style4,
                    'style':user_ans_sheet.style,

                }
                return render(request,'user_answer_list.html',data)
            else:
                ans=" ".join([' '.join([str(c) for c in lst]) for lst in final_lst])
                user_ans_sheet=UserAnswerSheet.objects.create(user=user,answer_key=ans,style='style_4')
                user_ans_sheet.save()   
                del request.session['user_id']
                
                data={
                    
                    'name':user.name,
                    'position':user.position,
                    'ans':ans,
                    'style1':style1,
                    'style2':style2,
                    'style3':style3,
                    'style4':style4,
                    'style':user_ans_sheet.style,
                    
                }
                return render(request,'user_answer_list.html',data)

class Register(View):
    def get(self,request):
        id=request.session.get('user_id',default=False)
        if id == False:
            return render(request,'register.html')
        else:
            del request.session['user_id']
            return redirect('register')
        
    def post(self,request):
        if UserInfo.objects.filter(email=request.POST['email']).exists():
            messages.info(request, 'Email Already Exists..')
            return redirect('register')
        else:           
            user_data=UserInfo.objects.create(name=request.POST['name'],email=request.POST['email'],position=request.POST['position'],experience=request.POST['experience'])
            request.session['user_id']=user_data.id
            return redirect('question-list')
