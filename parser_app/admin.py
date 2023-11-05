from django.contrib import admin

from parser_app.models import Parser


class ParserAdmin(admin.ModelAdmin):
    list_display = ('mpanCore', 'serialNo', 'unique_serial', 'ReadingDt', 'readingVal')
    search_fields = ('mpanCore', 'serialNo', 'unique_serial')
    list_filter = ('ReadingDt',)


admin.site.register(Parser, ParserAdmin)

