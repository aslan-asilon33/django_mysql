# from django.conf.urls import url 
from django.urls import path
from tutorials import views 

 
# urlpatterns = [ 
#     path(r'^api/tutorials$', views.tutorial_list),
#     path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
#     path(r'^api/tutorials/published$', views.tutorial_list_published)
# ]

urlpatterns = [ 
    path('api/tutorials', views.tutorial_list),
    # path('api/tutorials/<int:pk>', views.tutorial_detail),
    path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published)
    # path(r'^api/tutorials/published$', views.tutorial_list_published)
]
