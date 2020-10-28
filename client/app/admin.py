from django.contrib import admin
from .models import Client
from .models import Media_File
from import_export.admin import ImportExportModelAdmin



@admin.register(Client)

class cinfo(ImportExportModelAdmin):

    pass


@admin.register(Media_File)

class cinfo1(ImportExportModelAdmin):

    pass



    #admin.site.register(Client)
    #admin.site.register(Media_File)




