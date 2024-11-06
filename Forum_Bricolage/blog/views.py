from django.shortcuts import render
from auths.models import User
from .models import Article

def index(request):
    is_connected = False 
    articles= Article.objects.filter(status=True)
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        user = User.objects.get(idUser=user_id)
        is_connected = True
        context = {"user":user, "articles":articles[:6],"is_connected":is_connected}
    else:
        is_connected = False
        context={"articles":articles[:6],"is_connected":is_connected}
    return render(request,"index.html",context)
