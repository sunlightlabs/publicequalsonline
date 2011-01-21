from django.contrib import admin
from publicequalsonline.cosign.models import Letter, Signer

class LetterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Letter, LetterAdmin)

class SignerAdmin(admin.ModelAdmin):
    list_display = ('letter','name','organization','date_signed','is_important')
    list_display_links = ('name',)
    list_filter = ('letter','is_important',)
    search_fields = ('name','organization','email')
admin.site.register(Signer, SignerAdmin)