# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.template import RequestContext
from django.core.mail import send_mail
from django.db import connection

import os

from django.conf import settings
from csubgweb.models import Member, Project, Paper, Patent, Contact, News, Software, FriendLink

def index(request):
    news_list = News.objects.order_by('-publishDate')[:10]
    return render_to_response('index.html', {'header_menu_selected': 'index', 'news_list': news_list, 'link_list': get_friendLink()}, context_instance = RequestContext(request))

def get_friendLink():
    link_list = FriendLink.objects.all()
    return link_list

def forward(request,name,dir='', dir2=''):
    template_name = ''
    news_list = None
    query = ''
    cursor = connection.cursor()
    rows = None
    dicts = {}
    if(dir != ''):
        template_name = dir + '/'
    if(dir2 != ''):
        template_name = template_name + dir2 + '/'
    if((name == 'index.html' or name == 'index_cn.html') and dir2 == ''):
        news_list = News.objects.order_by('-publishDate')[:10]
    elif(name == 'members.html'):
        query = 'select category, count(*) as count from csubgweb_member group by category;'
    elif(name == 'project.html'):
        query = 'select source, count(*) as count from csubgweb_project group by source;'
    elif(name == 'achievements.html'):
        query = 'select type,count(*) as count from csubgweb_patent group by type;'
    elif(name == 'publications.html'):
        query = 'select type,count(*) as count from csubgweb_paper group by type;'
    if(query != ''):
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            dicts[row[0]] = row[1]
    template_name = template_name + name
    return render_to_response(template_name, {'header_menu_selected': name.split('.')[0], 'news_list': news_list,'dicts':dicts, 'link_list': get_friendLink()}, context_instance = RequestContext(request)) 

def member_list(request,name):
    members = Member.objects.filter(category = name.split('.')[0])
    return render_to_response('members/' + 'Master.html', {'member_list': members, 'header_menu_selected': 'members', 'menu_selected': name.split('.')[0], 'link_list': get_friendLink()}, context_instance = RequestContext(request))

def project_list(request,name):
    projects = Project.objects.filter(source__contains = name.split('.')[0])
    return render_to_response('project/NFSC.html', {'project_list': projects, 'header_menu_selected': 'project', 'menu_selected': name.split('.')[0], 'link_list': get_friendLink()}, context_instance = RequestContext(request))
    
def achievement_list(request,name):    
    modelType = name.split('.')[0]
    if modelType.find('Paper') >= 0:
        achievements = Paper.objects.filter(type__contains = name.split('.')[0])
        name = 'Paper.html'            
    else:
        achievements = Patent.objects.filter(type__contains = modelType)
        name = 'Patent.html'       
    return render_to_response('achievements/' + name, {'achievement_list': achievements, 'header_menu_selected': 'achievements', 'menu_selected': modelType, 'link_list': get_friendLink()}, context_instance = RequestContext(request))

def publication_list(request, name):
    publications = Paper.objects.filter(type__contains = name.split('.')[0])
    return render_to_response('achievements/Paper.html', {'publication_list': publications, 'header_menu_selected': 'publications', 'menu_selected': name.split('.')[0], 'link_list': get_friendLink()}, context_instance = RequestContext(request))

def download(request,dir, filename):
    path = 'software/'+ dir + '/' + filename
    path = os.path.join(settings.MEDIA_ROOT, path).replace('\\','/')
    f = open(path)
    data = f.read()
    f.close()
    response = HttpResponse(data, mimetype = 'application/octet-stream')
    response['Content-Disposition'] = 'attachment;filename=%s' % filename
    response['Content-Length'] = os.path.getsize(path)
    return response
'''
def download(request, dir, filename):
    path = 'software/'+ dir + '/' + filename
    path = os.path.join(settings.MEDIA_ROOT, path).replace('\\','/')
    wrapper = FileWrapper(file(path))
    response = HttpResponse(wrapper, content_type = 'text/plain')
    response['Content-Length'] = os.path.getsize(path)
    return response
'''
def download_list(request):
    s_category = ''
    if 'category' in request.GET and request.GET['category']:
        s_category = request.GET['category']
    template_name = 'download.html'
    software_list = Software.objects.filter(category__contains = s_category).order_by('-downloadCount')
    return render_to_response(template_name, {'header_menu_selected': 'download', 'menu_selected': s_category, 'software_list': software_list, 'link_list': get_friendLink()}, context_instance = RequestContext(request))

def news_list(request,newsId):
    news_list = None
    template_name = 'newslist.html'
    if(newsId == '0'):
        news_list = News.objects.order_by('-publishDate')[:10]
    else:
        news_list = News.objects.get(id = int(newsId))
        template_name = 'news.html'
    return render_to_response(template_name, {'header_menu_selected': 'index', 'news_list': news_list, 'link_list': get_friendLink()}, context_instance = RequestContext(request))

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

