# -*- coding: cp936 -*-
from django.db import models

# Create your models here.
GENDER_CHOICE = (
                 ('Female','Female'),
                 ('Male','Male'),
)
DEGREE_CHOICE = (
                 ('PhD','PhD'),
                 ('Master','Master'),
                 ('Bachelor','Bachelor'),
)
CATEGORY_CHOICE = (
                ('Professor', 'Professor'),
                ('VisitingScholar', 'Visiting Scholar'),
                ('PostDoctorate', 'Post Doctorate'),
                ('PhDCandidate', 'PhD Candidate'),
                ('PhDGraduate', 'PhD(Graduate)'),
                ('MasterCandidate', 'Master Candidate'),
                ('MasterGraduate', 'Master(Graduate)'),
                ('ForeignStudent', 'Foreign Student'),               
)
'''
TITLE_CHOICE = (
                ('Professor', 'Professor'),
                ('PostPhD', 'PostPhD'),
                ('PhD', 'PhD'),
                ('Master', 'Master'),
)
'''

class Member(models.Model):
    name = models.CharField(max_length = '30')
    englishName = models.CharField(max_length = '30')
    gender = models.CharField(max_length = '10', choices = GENDER_CHOICE)
    birthday = models.DateField(auto_now = False, auto_now_add = False, blank = True, null=True)
    title = models.CharField(max_length = '300')
    degree = models.CharField(max_length = '20', choices = DEGREE_CHOICE)
    category = models.CharField(max_length = '30',choices = CATEGORY_CHOICE)
    enrollmentDate = models.DateField(auto_now = False, auto_now_add = False, blank = True, null=True)
    headshot = models.ImageField(upload_to = 'upload/headshot', blank = True, null=True, default='upload/headshot/0_0.jpg')    
    email = models.EmailField(blank = True, null=True)
    homepage = models.CharField(max_length = '60', blank = True, null=True) 
    
    def __unicode__(self):
        return self.name

class Project(models.Model):
    SOURCE_CHOICE = (
                 ('From NFSC', 'From NFSC'),
                 ('From Ministry Education', 'From Ministry Education'),
                 ('From Hu Nan Province', 'From Hu Nan Province'),
                 ('From CSU', 'From CSU'),
                 ('From 973', 'From 973'),
                 ('Cooperation Project', 'Cooperation Project'),
    )
    title = models.CharField(max_length = '200')
    name = models.CharField(max_length = '200')
    number = models.CharField(max_length = '30')
    fund = models.CharField(max_length = '10')
    time = models.CharField(max_length = '40')
    manager = models.CharField(max_length = '20')
    introduction = models.TextField(max_length = '6000')
    source = models.CharField(max_length = '50', choices = SOURCE_CHOICE)
    
    def __unicode__(self):
        return self.name

class Paper(models.Model):
    TYPE_CHOICE = (
                   ('JournalPaper','Journal Paper'),
                   ('ConferencePaper','Conference Paper'),
    )
    title = models.TextField(max_length = '300')
    authors = models.CharField(max_length = '200')
    publication = models.TextField(max_length = '200')
    publisher = models.CharField(max_length = '100',null = True, blank = True)
    volume = models.CharField(max_length = '20',null = True, blank = True)
    number = models.CharField(max_length = '20',null = True, blank = True)
    pages = models.CharField(max_length = '20',null = True, blank = True)
    publishDate = models.DateField(auto_now = False, auto_now_add = False) 
    link = models.CharField(max_length = '100', blank = True, null = True)
    type = models.CharField(max_length = '40', choices = TYPE_CHOICE)
    
    def __unicode__(self):
        return self.title

class Patent(models.Model):
    TYPE_CHOICE = (
                   ('Patent', 'Patent'),
                   ('Award', 'Award'),
                   ('SoftwareCopyright', 'Software Copyright'),
    )
    name = models.CharField(max_length = '200')
    year = models.CharField(max_length = '10')
    owner = models.CharField(max_length = '60')
    applicationNumber = models.CharField(max_length = '50',null = True, blank = True)
    type = models.CharField(max_length = '30', choices = TYPE_CHOICE)
    
    def __unicode__(self):
        return self.name
  
class Software(models.Model):
    SOFTWARE_CHOICE = (
            ('Protein_Complex_Mining', 'Protein_Complex_Mining'),
            ('Key_Protein_Predict','Key_Protein_Predict'),
    )
    name = models.CharField(max_length = '100')
    functionDescription = models.TextField(max_length = '6000')
    instruction = models.TextField(max_length = '600',null = True, blank = True)
    browseCount = models.IntegerField(editable = False, default = 0)
    downloadCount = models.IntegerField(editable =False, default = 0)
    image = models.ImageField(upload_to = 'upload/software/%Y%m',blank = True, null = True)
    #link = models.FileField(upload_to = 'upload/software/homepage/%Y%m')
    link = models.CharField(max_length = '100', default='software/')
    category = models.CharField(max_length = '80', choices = SOFTWARE_CHOICE)
    
      
class Contact(models.Model):
    name = models.CharField(max_length = '100', blank = False)
    email = models.EmailField(editable = True)
    messages = models.TextField(max_length = '6000',)
    time = models.DateTimeField(auto_now_add = True)
    isReply = models.BooleanField(default = False)
        
    def __unicode__(self):
       return self.name
   
class News(models.Model):
    title = models.CharField(max_length = '300')
    content = models.TextField(max_length = '60000')
    publishDate = models.DateField(auto_now_add = True)
    
    def __unicode__(self):
        return self.title

class FriendLink(models.Model):
    name = models.CharField(max_length = '200')
    english_name = models.CharField(max_length = '200')
    link = models.CharField(max_length = '200')

    def __unicode__(self):
        return self.name
    
