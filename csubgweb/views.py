# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail

from csubgweb.models import Member, Project, Paper, Patent, Contact, News

def index(request):
    news_list = News.objects.order_by('-publishDate')[:10]
    return render_to_response('index.html', {'header_menu_selected': 'index', 'news_list': news_list}, context_instance = RequestContext(request)) 

def forward(request,name,dir=''):
    template_name = ''
    news_list = None
    if(dir != ''):
        template_name = dir + '/'
    if(name == 'index.html'):
        news_list = News.objects.order_by('-publishDate')[:10]
    template_name = template_name + name
    return render_to_response(template_name, {'header_menu_selected': name.split('.')[0], 'news_list': news_list}, context_instance = RequestContext(request)) 

def member_list(request,name):
    members = Member.objects.filter(title = name.split('.')[0])
    return render_to_response('members/' + name, {'member_list': members, 'header_menu_selected': 'members', 'menu_selected': name.split('.')[0]}, context_instance = RequestContext(request))

def project_list(request,name):
    projects = Project.objects.filter(source__contains = name.split('.')[0])
    return render_to_response('project/NFSC.html', {'project_list': projects, 'header_menu_selected': 'project', 'menu_selected': name.split('.')[0]}, context_instance = RequestContext(request))
    
def achievement_list(request,name):    
    modelType = name.split('.')[0]
    if modelType.find('Paper') >= 0:
        achievements = Paper.objects.filter(type__contains = name.split('.')[0])
        name = 'Paper.html'            
    else:
        achievements = Patent.objects.filter(type__contains = modelType)
        name = 'Patent.html'       
    return render_to_response('achievements/' + name, {'achievement_list': achievements, 'header_menu_selected': 'achievements', 'menu_selected': modelType}, context_instance = RequestContext(request))

def download_list(request):
    return

def news_list(request,newsId):
    news_list = None
    template_name = 'newslist.html'
    if(newsId == '0'):
        news_list = News.objects.order_by('-publishDate')[:10]
    else:
        news_list = News.objects.get(id = int(newsId))
        template_name = 'news.html'
    return render_to_response(template_name, {'header_menu_selected': 'index', 'news_list': news_list}, context_instance = RequestContext(request))

def contact_save(request):
    name = request.POST.get('name', 'None')
    email = request.POST.get('email', 'liqi328@gmail.com')
    message = request.POST.get('message', 'None')
    contact = Contact(name = name,email=email,messages= message)
    contact.save()
    send_mail(
            'Feedback from my CSUBG website: %s=%s' % (name , email),
            message,'liqi328@163.com',
            ['liqi328@163.com']
        )  
    return render_to_response('contact_success.html', {'header_menu_selected': 'contact'}, context_instance = RequestContext(request))
