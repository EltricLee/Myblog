from django.urls import path
from . import views

#http://localhost:8000/blog/1
#http://localhost:8000

# start with blog
urlpatterns = [
	path('update_comment',views.update_comment,name='update_comment'),

]