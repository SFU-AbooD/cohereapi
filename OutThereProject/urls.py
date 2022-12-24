from django.urls import path,include
app_name = 'logic'
urlpatterns = [
    path('',include('logic.urls'))
]
