from django.urls import path, include
from rest_framework import routers

from Myapp.views import EmployeeViewSet

router=routers.DefaultRouter()
router.register(r'employee',EmployeeViewSet)
#router.register(r'post',PostViewSet)

urlpatterns=[
    path('',include(router.urls))
]