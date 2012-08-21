from django.contrib import admin
from csubgweb.models import Member, Project, Paper, Patent, Contact, News, Software

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'degree', 'email') 
    search_fields = ('name',)
    ording = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'fund', 'time', 'manager', 'source')
    search_fields = ('name',)
    ording = ('name',)

class PaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publishPlace', 'publishDate')
    search_fields = ('name',)
    ording = ('-publishDate',)

class PatentAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'owner', 'applicationNumber')
    search_fields = ('name',)
    ording = ('-year')
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time', 'messages',)
    search_fields = ('messages',)
    ording = ('-time',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publishDate')
    search_fields = ('title',)
    ording = ('-publishDate',)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'browseCount', 'downloadCount', 'link')
    search_fields = ('name',)
    ording = ('-downloadCount')
    
admin.site.register(Member, MemberAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Patent, PatentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Software, SoftwareAdmin)