import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import Administrator, Design, Designer
from models import Proyecto


# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def createProject(request):

    if request.method == 'POST':

     jsonProject = json.loads(request.body)
     proyecto = Proyecto()
     print str("Entro ")

     print str("pasooooo ")

     proyecto.name = jsonProject['name']
     proyecto.description = jsonProject['description']
     proyecto.image = jsonProject['image']
     proyecto.estimated_price= jsonProject['estimatedPrice']
     proyecto.administrador = request.user
     proyecto.save()
     return HttpResponse(serializers.serialize("json",{proyecto}))

    if request.method == 'GET':
        #proyecto = Proyecto.objects.all()


        page = request.GET.get('page')
        user = request.user
        proyecto = Proyecto.objects.filter(administrador=user)
        paginator = Paginator(proyecto, 10) # Show 25 contacts per page
        try:
            proyectos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            proyectos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            proyectos = paginator.page(paginator.num_pages)
        data =serializers.serialize("json",proyectos.object_list)
        return HttpResponse(serializers.serialize("json",proyecto))

        ##return JsonResponse({"proyectos":data,"numeroPaginas":paginator.num_pages})

    if request.method == 'PUT':
        jsonProject = json.loads(request.body.decode('utf-8'))

        proyecto = Proyecto.objects.get(pk=jsonProject.get('pk'))
        proyecto.name = jsonProject.get('name')
        proyecto.description = jsonProject.get('description')
        proyecto.estimated_price= jsonProject.get('estimatedPrice')
        proyecto.image = jsonProject.get('image')
        proyecto.save()

        return HttpResponse(serializers.serialize("json",{proyecto}))

    if request.method == 'DELETE':
            jsonProject = json.loads(request.body.decode('utf-8'))

            proyecto = Proyecto.objects.get(pk=jsonProject.get('pk'))
            proyecto.delete()

            return HttpResponse(serializers.serialize("json",""))

@csrf_exempt
def registerManager(request):
    if request.method == 'POST':
        objs = json.loads(request.body)

        company = objs['company'].lower()
        password = objs['password']
        email = objs['email']


        userQS = User.objects.filter(username=company)
        userList = list(userQS[:1])
        if userList:
            print 'Paila ya existe el man'
            return HttpResponse(status=400)


        userModel = User.objects.create_user(username=company, password=password)
        userModel.first_name=company
        userModel.last_name=company
        userModel.email=email
        userModel.save()
        print 'Se crea el usuario'

        '''
        userQS = User.objects.filter(username=company)
        userList = list(userQS[:1])
        userObject = userList[0]
        '''
        manager = Administrator()
        manager.email=email
        manager.company=company
        manager.user=userModel
        manager.save()

        manager.url = request.get_raw_uri().replace('register',manager.company+'/'+str(manager.id))
        manager.save()
        print 'Se crea el manager'


    return HttpResponse(status=200)

@csrf_exempt
def loginUser(request):
    message = ''

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        username = jsonUser.get('username')
        password = jsonUser.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            message = 'OK'
            print 'El man se logeo'
        else:
            message = 'Usuario y/o clave invalida'
            print 'Paila el man no se logeo'

    return JsonResponse({'message':message})

@csrf_exempt
def loginUser(request):
    message = ''

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        username = jsonUser.get('username')
        password = jsonUser.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            message = 'OK'
        else:
            message = 'Usuario y/o clave invalida'

    return JsonResponse({'message':message})

@csrf_exempt
def isLoggedUser(request):
    if request.user.is_authenticated():
        logged = True
    else:
        logged = False
    return JsonResponse({'logged':logged})

@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({'logout':True})

'''
@csrf_exempt
def getIndependents(request):
    independents = Independent.objects.all().order_by('-user__date_joined')
    return HttpResponse(serializers.serialize("json",independents,use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def getJobs(request):
    jobs = Job.objects.all()
    return HttpResponse(serializers.serialize("json",jobs))

@csrf_exempt
def loginUser(request):
    message = ''

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        username = jsonUser.get('username')
        password = jsonUser.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            message = 'OK'
        else:
            message = 'Usuario y/o clave invalida'

    return JsonResponse({'message':message})

@csrf_exempt
def isLoggedUser(request):
    if request.user.is_authenticated():
        logged = True
    else:
        logged = False
    return JsonResponse({'logged':logged})

@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({'logout':True})

@csrf_exempt
def profile(request):
    user = request.user
    independent = Independent.objects.get(user=user)

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))

        independent.name = jsonUser.get('name')
        independent.lastName = jsonUser.get('last_name')
        independent.yearsOfExperience = jsonUser.get('experience')
        independent.phoneNumber = jsonUser.get('phone_number')
        independent.email = jsonUser.get('email')
        independent.imageFileUrl = jsonUser.get('image')

        jobQS = Job.objects.filter(jobName=str(jsonUser.get('job')).lstrip().rstrip())
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]

        independent.job = jobObject
        independent.job.save()
        independent.save()

    return HttpResponse(serializers.serialize("json",{independent},use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def registerIndependent(request):
    if request.method == 'POST':
        objs = json.loads(request.body)

        jobString = str(objs['job']).lstrip().rstrip()
        jobQS = Job.objects.filter(jobName=jobString)
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]
        username = objs['username']
        password = objs['password']
        email = objs['email']
        name = objs['name']
        lastName = objs['lastName']
        imageFileUrl = objs['imageFileUrl']
        phoneNumber = objs['phoneNumber']
        yearsOfExperience = objs['yearsOfExperience']

        userModel = User.objects.create_user(username=username, password=password)
        userModel.first_name=name
        userModel.last_name=lastName
        userModel.email=email
        userModel.save()
        print 'Se crea el usuario'

        userQS = User.objects.filter(username=username)
        userList = list(userQS[:1])
        userObject = userList[0]
        independent = Independent()
        independent.email=email
        independent.lastName=lastName
        independent.imageFileUrl=imageFileUrl
        independent.job=jobObject
        independent.name=name
        independent.phoneNumber=phoneNumber
        independent.yearsOfExperience = yearsOfExperience
        independent.user=userObject
        independent.save()
        print 'Se crea el independiente'


    return HttpResponse(status=200)

@csrf_exempt
def registerComment(request):

    if request.method == 'POST':
        objs = json.loads(request.body)
        idIndependent = objs['idIndependent']
        comment = objs['comment']
        userEmail = objs['userEmail']

        comentario = "<strong>Comentario:</strong> %s <br><br><strong>Enviado por:</strong> %s" % (comment, userEmail)

        independent = Independent.objects.get(id=idIndependent)

        emailIndependent = independent.email

        commentModel = Comment()
        commentModel.independent=independent
        commentModel.comment=comentario
        commentModel.userEmail=userEmail
        commentModel.save()

        print 'Se crea comentario para el idIndependent: '+ idIndependent

        #send_mail('Busco Ayuda - Comentario', comentario, userEmail, [emailIndependent], fail_silently=False)

        asunto = 'Busco Ayuda - Comentario'
        text_content = ''
        html_content = comentario
        from_email = userEmail
        to = emailIndependent

        mensaje = EmailMultiAlternatives(asunto, text_content, from_email, [to])
        mensaje.attach_alternative(html_content, "text/html")
        mensaje.send()

        print 'Se envia el correo electronico a: '+ emailIndependent

    return HttpResponse(status=200)


@csrf_exempt
def detail(request):
    user = request.user
    independent = Independent.objects.get(user=user)

    if request.method == 'POST':
        independentJson = json.loads(request.body)
        idIndependent = independentJson['idIndependent']

        independent = Independent.objects.filter(id=idIndependent)

        jobQS = Job.objects.filter(jobName=str(independentJson.get('job')).lstrip().rstrip())
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]

        independent.job = jobObject
        independent.job.save()
        independent.save()

    return HttpResponse(serializers.serialize("json",{independent},use_natural_foreign_keys=True, use_natural_primary_keys=True))
'''