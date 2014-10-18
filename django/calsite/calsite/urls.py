from caluny import views 
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin

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


urlpatterns = patterns('',
        url(r'^', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'admin/', include(admin.site.urls)),
        )
