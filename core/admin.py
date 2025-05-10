from django.contrib import admin
from unfold.admin import ModelAdmin
from newsletter.models import NewsletterSubscriber
from .models import Sector, Startup, Investor
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


class SectorAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    
    
class StartupAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ('name', 'sector', 'location')
    search_fields = ('name',)
    list_filter = ['sector']
    
class InvestorAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display =('name', 'investment_type', 'country')
    search_fields = ('name',)
    
    
class NewsletterSubscriberAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display = ('email', 'subscribed_at')


admin.site.register(Sector, SectorAdmin)
admin.site.register(Startup, StartupAdmin)
admin.site.register(Investor, InvestorAdmin)
admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)

