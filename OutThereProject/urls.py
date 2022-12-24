from django.urls import path,include
app_name = 'logic'
urlpatterns = [
     path('forest', include('django_forest.urls')),
    path('',include('logic.urls'))
]
