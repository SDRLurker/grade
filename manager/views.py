from django.shortcuts import render
#회원가입
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from manager.forms import RegisterForm
from django.views.generic import View

# Create your views here.
def signup(request):
    """signsup
    to register users
    """
    if request.method == "POST":
        userform = RegisterForm(request.POST)
        print(userform.is_valid())
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(
                reverse("signup_ok")
            )
    elif request.method =="GET":
        userform = RegisterForm()
    return render(request, "registration/signup.html", {"userform": userform,})

class DuplicationCheck(View):
    def post(self, request):
        # user = get_object_or_404(User, username=username)
        username = request.POST.get('username', None)
        data = {
            'is_taken': User.objects.filter(username__iexact=username).exists()
            }
        return JsonResponse(data)
