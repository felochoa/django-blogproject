from django.urls import path


from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
#Its path is just signup/ so the overall URL path will be accounts/signup/.
