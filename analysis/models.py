from django.db import models
# import jsonfield

class UserInfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    position=models.CharField(max_length=200)
    experience=models.CharField(max_length=5)
    
    def __str__(self) :
        return self.name
    




    
class UserAnswerSheet(models.Model):
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    answer_key= models.TextField(max_length=200)
    style=models.CharField(max_length=100)

    def __str__(self) :
        return self.user.name
    