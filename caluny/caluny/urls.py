from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin

from caluny_api import views


router = DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'university', views.UniversityViewSet)
router.register(r'subject', views.SubjectViewSetSimple)
router.register(r'degrees', views.DegreeViewSet)
router.register(r'degree', views.DegreeViewDetailSet)
router.register(r'teachingsubject', views.TeachingSubjectViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'timetable', views.TimetableViewSet)
router.register(r'exam', views.ExamViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^caluny/', include('caluny_api.urls', namespace='caluny', app_name='core')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'admin/', include(admin.site.urls)),
]
