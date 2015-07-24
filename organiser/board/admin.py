from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils import timezone
import datetime

from .models import Duty,Patient,Volunteer,Ward


admin.AdminSite.site_header ="Volunteer administration"
admin.AdminSite.site_title ="Volunteer administration"



class BirthdayFilter(admin.SimpleListFilter):
    title = 'birthday'
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'birthday_soon'
    def lookups(self, request, model_admin):
        return ( ('today', _('Today')), ('week', _('Next 7 days')))

    def queryset(self, request, queryset):
        # select by date... Patient.objects.filter(birthday__month=4, birthday__day=1)
        if self.value() == 'today':
            return queryset.filter(
                    birthday__month=timezone.now().month,
                    birthday__day=timezone.now().day
                )
        # FIXME
        if self.value() == 'week':
            future_date=timezone.now() +  datetime.timedelta(days=7);
            return queryset.filter(
                    birthday__month__gte = timezone.now().month,
                    birthday__day__gte = timezone.now().day,
                  #  birthday__month__lte = (timezone.now() \
                  #          + datetime.timedelta(days=7)).month,
                  #  birthday__day__lte = (timezone.now() \
                  #          + datetime.timedelta(days=7)).day,
                )


class DutyAdmin(admin.ModelAdmin):
    fieldsets = [
       (_('Who'), {'fields': ['volunteer', 'patient']}),
       (_('When'), {'fields': ['date', 'time']}),
       (_('Other'), {'fields': ['notes']}),
    ]
    list_display = ('volunteer', 'patient', 
            'date', 'time', 'notes')


class VolunteerAdmin(admin.ModelAdmin):
    fieldsets = [
       (_('Person'), {'fields': ['first_name', 'surname', 'birthday']}),
       (_('Contact'), {'fields': ['email','phone']}),
       (_('Other'), {'fields': ['notes']}),
    ]
    list_display = ('first_name', 'surname',
                    'birthday', 'email', 'notes')
    list_filter = [BirthdayFilter]


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
       (_('Person'), {'fields': ['first_name', 'surname', 'birthday']}),
       (_('Contact'), {'fields': ['email','phone']}),
       (_('Other'), {'fields': ['ward','notes']}),
    ]
    list_display = ('first_name', 'surname', 'ward',
                    'birthday', 'email', 'notes')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Ward)
