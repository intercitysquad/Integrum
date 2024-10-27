from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PythonProjectCifra import settings
from django.contrib.auth import authenticate, login
import psycopg2


# Create your views here.
def index(request):
    db = settings.DATABASES['test_database']
    conn = psycopg2.connect(dbname=db['NAME'], host=db['HOST'], user=db['USER'], password=db['PASSWORD'], port=db['PORT'])
    cursor = conn.cursor()

    # cursor.execute("SELECT * FROM public.""table""")
    # print(cursor.fetchall())

    cursor.close()
    conn.close()
    return HttpResponseRedirect("login/")
    # return HttpResponse("Hello ME!")

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

def login(request):
    return render(request=request,template_name="page5.html")