"""competency_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from analysis.views import *
from analysis.admin_view import *
urlpatterns = [
    path('login/', ForgottenPasswordAndLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path("question-list/", QuestionList.as_view(), name="question-list"),
    path("", Register.as_view(), name="register"),
    path("user-register/", UserRegister.as_view(), name="user-register"),
    path("admin-list/", AdminListView.as_view(), name="admin-list"),
    path("edit-user/<int:id>/",EditUserView.as_view(),name='edit-user'),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("user-profile/", UserProfile.as_view(), name="user-profile"),
    path("staff-list/", StaffListView.as_view(), name="staff-list"),
    path("delete-admin/<int:id>/", DeleteAdminView.as_view(), name="delete-admin"),
    path("delete-staff/<int:id>/", DeleteStaffView.as_view(), name="delete-staff"),
    path("candidate-list/", RegisterCandidateList.as_view(), name="candidate-list"),
    path("delete-candidate/<int:id>/", DeleteCandidate.as_view(), name="delete-candidate"),
    path("candidate-answersheet-list/", CandidateAnswerSheetList.as_view(), name="candidate-answersheet-list"),
    path("candidate-answersheet-delete/<int:id>/", CandidateAnswerSheetDelete.as_view(), name="candidate-answersheet-delete"),
    path("delete-candidate-all-data/",DeleteAllCandidate.as_view(),name="delete-candidate-all-data"),
    path("delete-answersheet-all-data/",DeleteAllAnswersheet.as_view(),name="delete-answersheet-all-data"),
    path("delete-all-staff/",DeleteAllStaff.as_view(),name="delete-all-staff"),
    path("delete-all-admin/",DeleteAllAdmin.as_view(),name="delete-all-admin"),
    path("forgotten-password/",ForgottenPassword.as_view(),name="forgotten-password"),
    path("temporary-password/",TemporaryPasswordGenerator.as_view(),name="temporary-password"),
]
