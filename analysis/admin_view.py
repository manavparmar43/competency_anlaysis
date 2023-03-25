from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .models import UserAnswerSheet,UserInfo
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
import time
from django.conf import settings
# def send_order_email_confirmation(sender, instance, **kwargs):

import string
import random  
from django.contrib.auth.hashers import check_password ,make_password
#     return mail.send()

class ForgottenPasswordAndLoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        if 'username' in request.POST:
            if request.POST['username'] and request.POST['password']:
                usernames = request.POST['username']
                password = request.POST['password']
                if User.objects.filter(username=usernames).exists():
                
                    user = auth.authenticate(username=usernames, password=password)
                    if user is not None:
                        auth.login(request, user)
                        if user.is_superuser:
                            return redirect('dashboard')
                        else:
                            return redirect('dashboard')
                    else:

                        messages.info(request, '*** INVAID INPUT ***')
                        return redirect('login')
                else:
                    messages.info(request, '*** USER NOT AVAILABLE ***')
                    return redirect('login')
            else:    
                messages.info(request, '*** SOME FIELD EMPTY ***')
                return redirect('login')
        else:
            if request.POST['forgottenusername'] and  request.POST['forgottenemail']:
                usernames = request.POST['forgottenusername']
                email = request.POST['forgottenemail']
                user =User.objects.get(username=usernames)
                
                if user:
                    if user.email==email:
                        N = 7
                        res = str(''.join(random.choices(string.ascii_letters, k=N)))
                        user.set_password(res)
                        user.save()
                        message = get_template("tempory_forgottenpwd_mail.html").render({
                        "password":res

                        })
                        mail = EmailMessage(
                            subject="Temporary Password Information",
                            body=message,
                            from_email=settings.EMAIL_HOST_USER,
                            to=[user.email],
                        )
                        mail.content_subtype = "html"
                        mail.send(fail_silently=False)
                        messages.success(request,"Temporary password sending on your register mail")
                        return redirect('login')
                    else:
                        messages.info(request,"Register Email not valid")
                        return redirect('login')
                else:
                    messages.info(request,"User not valid")
                    return redirect('login')
            else:
                    messages.info(request,"Some Field Empty")
                    return redirect('login')  




class RegisterCandidateList(View):
    def get(self,request):
        if request.user.is_authenticated:
            user_info=UserInfo.objects.all()
            return render(request,'register_candidates_list.html',{"user_info":user_info})
        else:
            return redirect('login')
    def post(self,request):
        if request.POST['filter'] != 'filter':
            if request.POST['filter'] == 'name':
                if request.POST['search']:
                    filter_data=UserInfo.objects.filter(name=request.POST['search'])
                    if filter_data:
                        messages.success(request,'*** DATA FOUND ***')
                        return render(request,'register_candidates_list.html',{"filter_data":filter_data})
                    else:
                        messages.info(request,'*** DATA NOT FOUND ***')
                        return redirect('candidate-list') 
                else:
                    messages.info(request,'*** PLEASE ENTER THE SEARCH VALUE ***')
                    return redirect('candidate-list') 

            elif request.POST['filter'] == 'email':
                if request.POST['search']:
                    filter_data=UserInfo.objects.filter(email=request.POST['search'])
                    if filter_data:
                        messages.success(request,'*** DATA FOUND ***')
                        return render(request,'register_candidates_list.html',{"filter_data":filter_data})
                    else:
                        messages.info(request,'*** DATA NOT FOUND ***')
                        return redirect('candidate-list')
                else:
                    messages.info(request,'*** PLEASE ENTER THE SEARCH VALUE ***')
                    return redirect('candidate-list')

            elif request.POST['filter'] == 'position':
                if request.POST['search']:
                    filter_data=UserInfo.objects.filter(position=request.POST['search'])
                    if filter_data:
                        messages.success(request,'*** DATA FOUND ***')
                        return render(request,'register_candidates_list.html',{"filter_data":filter_data})
                    else:
                        messages.info(request,'*** DATA NOT FOUND ***')
                        return redirect('candidate-list')
                else:
                    messages.info(request,'*** PLEASE ENTER THE SEARCH VALUE ***')
                    return redirect('candidate-list')

            else:
                if request.POST['search']:
                    filter_data=UserInfo.objects.filter(experience=request.POST['search'])
                    if filter_data:
                        messages.success(request,'*** DATA FOUND ***')
                        return render(request,'register_candidates_list.html',{"filter_data":filter_data})
                    else:
                        messages.info(request,'*** DATA NOT FOUND ***')
                        return redirect('candidate-list')
                else:
                    messages.info(request,'*** PLEASE ENTER THE SEARCH VALUE ***')
                    return redirect('candidate-list')

        else:
            
            messages.info(request,"*** SELECT FILTER TYPE ***")
            return redirect('candidate-list')
                

class DeleteCandidate(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            user_info=UserInfo.objects.get(pk=id)
            user_info.delete()
            return redirect('candidate-list')
        else:
            return redirect('login')

class CandidateAnswerSheetList(View):
    def get(self,request):
        if request.user.is_authenticated:
            user_ans=UserAnswerSheet.objects.all()
            return render(request,'candidate_answer_list.html',{'user_ans':user_ans})
        else:
            return redirect('login')
    def post(self,request):
        if request.POST['filter'] != 'filter':
            if request.POST['filter'] == 'email':
                if request.POST['search']:
                    user_info=UserInfo.objects.get(email=request.POST['search'])
                    if user_info:
                        user_answer=UserAnswerSheet.objects.filter(user=user_info)
                        if user_answer:
                            messages.success(request,"*** DATA FOUND ***")
                            return render(request,'candidate_answer_list.html',{'filter_data':user_answer})
                        else:
                            messages.info(request,"*** CANDIDATE ANSWERSHEET NOT FOUND ***")
                            return redirect('candidate-answersheet-list')
                        

                    else:
                        messages.info(request,"*** CANDIDATE DATA NOT FOUND ***")
                        return redirect("candidate-answersheet-list")
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect("candidate-answersheet-list")
            else :
                if request.POST['search']:
                    user_answer=UserAnswerSheet.objects.filter(style=request.POST['search'])
                    if user_answer:
                            messages.success(request,"*** DATA FOUND ***")
                            return render(request,'candidate_answer_list.html',{'filter_data':user_answer})
                    else:
                        # style=
                        messages.info(request,f"*** NO ANY DATA {request.POST['search']} ***")
                        return redirect('candidate-answersheet-list')
                else:
                    messages.info(request,f"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('candidate-answersheet-list')



        else:
            messages.info(request,"*** SELECT FILTER TYPE ***")
            return redirect("candidate-answersheet-list")
    
class CandidateAnswerSheetDelete(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            user_ans=UserAnswerSheet.objects.get(id=id)
            user_ans.delete()
            return redirect('candidate-answersheet-list')
        else:
            return redirect('login')
class UserRegister(View):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return render(request,'user_register.html')
            else:
                return redirect('dashboard')
        else:
            return redirect('login')
    def post(self,request):
        choice=request.POST['choice']
        if choice == 'admin':
            if User.objects.filter(email=request.POST['email']).exists():
                messages.info(request,'Email already exists....')
                return redirect('user-register')
            elif User.objects.filter(username=request.POST['username']).exists():
                messages.info(request,'Username already exists....')
                return redirect('user-register')
            else:
                user_data=User.objects.create_user(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    username=request.POST['username'],
                    password=request.POST['password'],
                    is_staff=False,
                    is_superuser=True
                    )
                user_data.save()
                message = get_template("mail.html").render({
                    
                    "firstname":user_data.first_name,
                    "lastname":user_data.last_name,
                    "username":user_data.username,
                    "email":user_data.email,
                    "password":request.POST['password'],
                    "role":"Admin"

                })
                mail = EmailMessage(
                    subject="Register Information",
                    body=message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[user_data.email],
                )
                mail.content_subtype = "html"
                mail.send(fail_silently=False)
                messages.success(request,'Registration Successfully and mail are sended...')
                return redirect('user-register')
        else:
            if User.objects.filter(email=request.POST['email']).exists():
                messages.info(request,'Email already exists....')
                return redirect('user-register')
            elif User.objects.filter(username=request.POST['username']).exists():
                messages.info(request,'Username already exists....')
                return redirect('user-register')
            else:
                user_data=User.objects.create_user(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    username=request.POST['username'],
                    password=request.POST['password'],
                    is_staff=True,
                    is_superuser=False
                    )
                user_data.save()
                message = get_template("mail.html").render({
                    
                    "name":user_data.first_name.capitalize()+' '+ user_data.last_name.capitalize(),
                    "firstname":user_data.first_name,
                    "lastname":user_data.last_name,
                    "username":user_data.username,
                    "email":user_data.email,
                    "password":request.POST['password'],
                    "role":"Staff"

                })
                mail = EmailMessage(
                    subject="Register Information",
                    body=message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[user_data.email],
                )
                mail.content_subtype = "html"
                mail.send(fail_silently=False)
                messages.success(request,'Registration Successfully and mail are sended...')
                return redirect('user-register')
            


        
        
            
            

class AdminListView(View):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser :
                admin_data=User.objects.filter(is_superuser=True)
                return render(request,'register_admin_list.html',{"admin_data":admin_data})
            else:
                admin_data=User.objects.filter(is_superuser=True)
                return render(request,'register_admin_list.html',{"admin_data":admin_data})
        else:
            return redirect('login')
    def post(self,request):
        if request.POST['filter'] != 'filter':
        
            if request.POST['filter'] == 'firstname':
                if request.POST['search']:
                    filter_data=User.objects.filter(first_name=request.POST['search'],is_superuser=True)
                    if filter_data:
                        messages.success(request,"*** DATA FOUND ***")
                        return render(request,'register_admin_list.html',{"filter_data":filter_data})   
                    else:
                        messages.info(request,"*** DATA NOT FOUND ***")
                        return redirect('admin-list')
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('admin-list')
                    
            elif request.POST['filter'] == 'lastname':
                if request.POST['search']:
                    filter_data=User.objects.filter(last_name=request.POST['search'],is_superuser=True)
                    if filter_data:
                        messages.success(request,"*** DATA FOUND ***")
                        return render(request,'register_admin_list.html',{"filter_data":filter_data})   
                    else:
                        messages.info(request,"*** DATA NOT FOUND ***")
                        return redirect('admin-list')
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('admin-list')
            elif request.POST['filter'] == 'email':
                if request.POST['search']:
                    filter_data=User.objects.filter(email=request.POST['search'],is_superuser=True)
                    if filter_data:
                        messages.success(request,"*** DATA FOUND ***")
                        return render(request,'register_admin_list.html',{"filter_data":filter_data})   
                    else:
                        messages.info(request,"*** DATA NOT FOUND ***")
                        return redirect('admin-list')
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('admin-list')
            else:
                if request.POST['search']:
                    filter_data=User.objects.filter(username=request.POST['search'],is_superuser=True)
                    if filter_data:
                        messages.success(request,"*** DATA FOUND ***")
                        return render(request,'register_admin_list.html',{"filter_data":filter_data})   
                    else:
                        messages.info(request,"*** DATA NOT FOUND ***")
                        return redirect('admin-list')
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('admin-list')

        else:
            
            messages.info(request,"*** SELECT FILTER TYPE ***")
            return redirect('admin-list')
    

class StaffListView(View):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser :
                
                staff_data=User.objects.filter(is_superuser=False)
                return render(request,'register_staff_list.html',{"staff_data":staff_data})
            else:
                staff_data=User.objects.filter(is_superuser=False)
                return render(request,'register_staff_list.html',{"staff_data":staff_data})
        else:
            return redirect("login")
    def post(self,request):
        if request.POST['filter'] != 'filter':

            if request.POST['filter'] == 'firstname':
                if request.POST['search']:
                    filter_data=User.objects.filter(first_name=request.POST['search'],is_superuser=False)
                    if filter_data:
                        messages.success(request,"*** DATA FOUND ***")
                        return render(request,'register_staff_list.html',{"filter_data":filter_data})   
                    else:
                        messages.info(request,"*** DATA NOT FOUND ***")
                        return redirect('staff-list')
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('staff-list')
            elif request.POST['filter'] == 'lastname':
                if request.POST['search']:
                    filter_data=User.objects.filter(last_name=request.POST['search'],is_superuser=False)
                    if filter_data:
                        messages.success(request,"*** DATA FOUND ***")
                        return render(request,'register_staff_list.html',{"filter_data":filter_data})   
                    else:
                        messages.info(request,"*** DATA NOT FOUND ***")
                        return redirect('staff-list')
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('staff-list')

            elif request.POST['filter'] == 'email':
                if request.POST['search']:
                    filter_data=User.objects.filter(email=request.POST['search'],is_superuser=False)
                    if filter_data:
                        messages.success(request,"*** DATA FOUND ***")
                        return render(request,'register_staff_list.html',{"filter_data":filter_data})   
                    else:
                        messages.info(request,"*** DATA NOT FOUND ***")
                        return redirect('staff-list')
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('staff-list')
            else:
                if request.POST['search']:
                    filter_data=User.objects.filter(username=request.POST['search'],is_superuser=False)
                    if filter_data:
                        messages.success(request,"*** DATA FOUND ***")
                        return render(request,'register_staff_list.html',{"filter_data":filter_data})   
                    else:
                        messages.info(request,"*** DATA NOT FOUND ***")
                        return redirect('staff-list')
                else:
                    messages.info(request,"*** PLEASE ENTER THE SEARCH VALUE ***")
                    return redirect('staff-list')
        else:
            
            messages.info(request,"*** SELECT FILTER TYPE ***")
            return redirect('staff-list')
            

class DeleteAdminView(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            if request.user.is_superuser :
                admindata=User.objects.get(id=id)
                admindata.delete()
                return redirect('admin-list')
            else:
                return redirect('dashboard')
        else:
            return redirect('login')
    
class DeleteStaffView(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            if request.user.is_superuser :
                staffdata=User.objects.get(id=id)
                staffdata.delete()
                return redirect('staff-list')
            else:
                return redirect('dashboard')
        else:
            return redirect('login')
class EditUserView(View):
    def get(self,request,id):
        if request.user.is_authenticated:
            if request.user.is_superuser :
                if User.objects.filter(pk=id).exists():
                    user_data=User.objects.get(pk=id)
                    return render(request,'edit_user.html',{"user_data":user_data})
                else:
                    return redirect('dashboard')
            else:
                return redirect('dashboard')
        else:
            return redirect('login')
    def post(self,request,id):
        if User.objects.filter(pk=id).exists():
            
            if request.POST['choice'] == 'admin':
                    user_data=User.objects.get(pk=id)
                    if user_data:
                        if request.POST['first_name'] and request.POST['last_name'] and request.POST['username'] and request.POST['email']:
                            if user_data.first_name == request.POST['first_name'] and user_data.last_name == request.POST['last_name'] and user_data.username == request.POST['username'] and user_data.email == request.POST['email']: 
                                messages.success(request,"No Any Update Data...")
                                return redirect('edit-user',id=id)
                            else:
                                user_data.first_name = request.POST['first_name']
                                user_data.last_name = request.POST['last_name']
                                user_data.username = request.POST['username']
                                user_data.email = request.POST['email']
                                user_data.is_staff = False
                                user_data.is_superuser = True
                                user_data.save()
                                
                                message = get_template("edit_user_mail.html").render({
                                       
                                        "name":user_data.first_name.capitalize()+' '+ user_data.last_name.capitalize(),
                                        "firstname":user_data.first_name,
                                        "lastname":user_data.last_name,
                                        "username":user_data.username,
                                        "email":user_data.email,
                                        "role":"Admin"

                                })
                                mail = EmailMessage(
                                    subject="Update Information",
                                    body=message,
                                    from_email=settings.EMAIL_HOST_USER,
                                    to=[user_data.email],
                                )
                                mail.content_subtype = "html"
                                mail.send(fail_silently=False)
                                messages.success(request,'Your data updated successfully and mail sended......')
                                return redirect('edit-user',id=id)
                        else:
                            messages.info(request,'Some Fields Empty......')
                            return redirect('edit-user',id=id)

            else:
                user_data=User.objects.get(pk=id)  
                if user_data:  
                    if request.POST['first_name'] and request.POST['last_name'] and request.POST['username'] and request.POST['email']:
                        if user_data.first_name == request.POST['first_name'] and user_data.last_name == request.POST['last_name'] and user_data.username == request.POST['username'] and user_data.email == request.POST['email']: 
                                messages.success(request,"No Any Update Data...")
                                return redirect('edit-user',id=id)
                        else:
                            
                            user_data.first_name = request.POST['first_name']
                            user_data.last_name = request.POST['last_name']
                            user_data.username = request.POST['username']
                            user_data.email = request.POST['email']
                            user_data.is_staff = True
                            user_data.is_superuser = False
                            user_data.save()
                            message = get_template("edit_user_mail.html").render({
                                    "id":user_data.pk,
                                    "name":user_data.first_name.capitalize()+' '+ user_data.last_name.capitalize(),
                                    "firstname":user_data.first_name,
                                    "lastname":user_data.last_name,
                                    "username":user_data.username,
                                    "email":user_data.email,
                                    "role":"Staff"

                            })
                            mail = EmailMessage(
                                subject="Update Information",
                                body=message,
                                from_email=settings.EMAIL_HOST_USER,
                                to=[user_data.email],
                            )
                            mail.content_subtype = "html"
                            mail.send(fail_silently=False)
                            messages.success(request,'Your data updated successfully and mail sended......')
                            return redirect('edit-user',id=id) 
                    else:
                        messages.info(request,'Some Fields Empty......')
                        return redirect('edit-user',id=id)  
                else:
                    messages.info(request,'User Not Found......')
                    return redirect('edit-user',id=id)  

        else:
            return redirect('dashboard')
        
    

class Dashboard(View):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                data=User.objects.all()
                return render(request,'base.html',{"data":data})
            else:
                data=User.objects.all()
                return render(request,'base.html',{"data":data})
                #  return render(request,'base.html')
        else:
            return redirect('login')

        
class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                auth.logout(request)
                return redirect('login')
            else:
                auth.logout(request)
                return redirect('login')
        else:
            return redirect('login')
        
class UserProfile(View):
    def get(self,request):
        if request.user.is_authenticated:
                return render(request,'user_profile.html')
        else:
            return redirect('login')
    def post(self,request):
        if request.user.is_superuser:
            user_data=User.objects.get(pk=request.user.id)
            if user_data:
                
                if request.POST['first_name'] and request.POST['last_name'] and request.POST['username'] and request.POST['email']:
                    if user_data.first_name == request.POST['first_name'] and user_data.last_name == request.POST['last_name'] and user_data.username == request.POST['username'] and user_data.email == request.POST['email']:
                        messages.success(request,'No Any Update Field......')
                        return redirect('user-profile')  
                    else:      
                            user_data.first_name = request.POST['first_name']
                            user_data.last_name = request.POST['last_name']
                            user_data.username = request.POST['username']
                            user_data.email = request.POST['email']
                            user_data.is_staff = False
                            user_data.is_superuser = True
                            user_data.save()
                            message = get_template("edit_profile_mail.html").render({
                                    "id":user_data.pk,
                                    "name":user_data.first_name.capitalize()+' '+ user_data.last_name.capitalize(),
                                    "firstname":user_data.first_name,
                                    "lastname":user_data.last_name,
                                    "username":user_data.username,
                                    "email":user_data.email,
                                    "role":"Admin"

                            })
                            mail = EmailMessage(
                                subject="Profile Update Information",
                                body=message,
                                from_email=settings.EMAIL_HOST_USER,
                                to=[user_data.email],
                            )
                            mail.content_subtype = "html"
                            mail.send(fail_silently=False)
                            messages.success(request,'Your profile updated successfully and mail sended......')
                            return redirect('user-profile')
                else:
                    messages.info(request,'Some Fields Empty......')
                    return redirect('user-profile')
            else:
                messages.info(request,'User Not Found......')
                return redirect('user-profile')
        else:
            user_data=User.objects.get(pk=request.user.id)    
            if user_data:
                if request.POST['first_name'] and request.POST['last_name'] and request.POST['username'] and request.POST['email']:
                    if user_data.first_name == request.POST['first_name'] and user_data.last_name == request.POST['last_name'] and user_data.username == request.POST['username'] and user_data.email == request.POST['email']:
                        messages.success(request,'No Any Update Field......')
                        return redirect('user-profile')  
                    else:
                        user_data.first_name = request.POST['first_name']
                        user_data.last_name = request.POST['last_name']
                        user_data.username = request.POST['username']
                        user_data.email = request.POST['email']
                        user_data.is_staff = True
                        user_data.is_superuser = False
                        user_data.save()
                        message = get_template("edit_profile_mail.html").render({
                                    "id":user_data.pk,
                                    "name":user_data.first_name.capitalize()+' '+ user_data.last_name.capitalize(),
                                    "firstname":user_data.first_name,
                                    "lastname":user_data.last_name,
                                    "username":user_data.username,
                                    "email":user_data.email,
                                    "role":"Staff"

                            })
                        mail = EmailMessage(
                            subject="Profile Update Information",
                            body=message,
                            from_email=settings.EMAIL_HOST_USER,
                            to=[user_data.email],
                        )
                        mail.content_subtype = "html"
                        mail.send(fail_silently=False)
                        messages.success(request,'Your profile updated successfully and mail sended......')
                        return redirect('user-profile')
                else:
                    messages.info(request,'Some Fields Empty......')
                    return redirect('user-profile')
            else:
                messages.info(request,'User Not Found......')
                return redirect('user-profile')


class DeleteAllCandidate(View):
    def get(self,request):
        if request.user.is_authenticated:
            candidate=UserInfo.objects.all()
            if candidate:
                candidate.delete()
                return redirect('candidate-list')
            else:
                return redirect('candidate-list')
        else:
            return redirect("login")
        
class DeleteAllAnswersheet(View):
    def get(self,request):
        if request.user.is_authenticated:
            answer=UserAnswerSheet.objects.all()
            if answer:
                answer.delete()
                return redirect('candidate-answersheet-list')
            else:
                return redirect('candidate-answersheet-list')
        else:
            return redirect("login")
        
class DeleteAllStaff(View):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                staff=User.objects.filter(is_superuser=False)
                if staff:
                    staff.delete()
                    return redirect("staff-list")
                else:
                    return redirect("staff-list")
            else:
                return redirect("staff-list")
        else:
            return redirect("login")

class DeleteAllAdmin(View):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                admin=User.objects.filter(is_superuser=True)
                if admin:
                    admin.delete()
                    return redirect("admin-list")
                else:
                    return redirect("admin-list")
            else:
                return redirect("admin-list")
        else:
            return redirect("login")

class ForgottenPassword(View):
    def get(self,request):
        if request.user.is_authenticated:
            
            return render(request,'forgotten_password.html')
        else:
            return redirect('login')
        
    def post(self,request):
        
        if request.POST['currentpassword']:
            user=User.objects.get(id=request.user.id)
            if user:
                currentpassword=str(request.POST['currentpassword']).strip()
                if user.check_password(currentpassword):
                    user.set_password(request.POST['password'])
                    user.save()
                    message = get_template("forgotten_password_mail.html").render({
                                        "name":user.first_name.capitalize()+' '+ user.last_name.capitalize(),
                                        "password":request.POST['password'],
                                        "role":"Staff"

                                })
                    mail = EmailMessage(
                        subject="Password Update Information",
                        body=message,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[user.email],
                    )
                    mail.content_subtype = "html"
                    mail.send(fail_silently=False)

                    messages.success(request,'Password has been reset successfully and mail sended...')
                    
                    return redirect('logout')
                else:
                    messages.info(request,'Current Password incorrect')
                    return redirect('forgotten-password')
            else:
                messages.info(request,'USER NOT FOUND')
                return redirect('logout')
        else:
            messages.info(request,"Some field empty... ")
            return redirect('forgotten-password')
            
class TemporaryPasswordGenerator(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,'temporary_password_generator.html')
        else:
            return redirect('login')
        
    def post(self,request):
        email=request.POST['email']
        username=request.POST['username']
        if email and username:
            user = User.objects.get(username = username )
            if user:
                if user.email == email :
                        N = 7
                        res = str(''.join(random.choices(string.ascii_letters, k=N)))
                        user.set_password(res)
                        user.save()
                        message = get_template("tempory_forgottenpwd_mail.html").render({
                        "password":res

                        })
                        mail = EmailMessage(
                            subject="Temporary Password Information",
                            body=message,
                            from_email=settings.EMAIL_HOST_USER,
                            to=[user.email],
                        )
                        mail.content_subtype = "html"
                        mail.send(fail_silently=False)
                        messages.success(request,"Temporary password sending on your register mail")
                        return redirect('logout')
                else:
                    messages.info(request,"Register Email not valid")
                    return redirect('temporary-password')
            else:
                messages.info(request,"User Not Found")
                return redirect('temporary-password')
        else:
            messages.info(request,"Some Field Empty.....")
            return redirect('temporary-password')
        
