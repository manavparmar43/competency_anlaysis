from django.contrib import admin

from .models import *
@admin.register(UserInfo)
class user_Info(admin.ModelAdmin):
        list_display=['id','name','email','position','experience']


      
@admin.register(UserAnswerSheet)
class user_answer_sheet(admin.ModelAdmin):
        list_display=['id','user','answer_key','style']