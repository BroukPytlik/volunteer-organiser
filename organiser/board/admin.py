from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils import timezone
import datetime

from .models import Duty,Patient,Volunteer,Ward



class BirthdayFilter(admin.SimpleListFilter):
    title = 'birthday'
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'birthday_soon'
    def lookups(self, request, model_admin):
        return ( ('today', _('Today')), ('week', _('Next 7 days')))

    def queryset(self, request, queryset):
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


# Change the order of fields...
class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
       (_('Person'), {'fields': ['first_name', 'surname', 'birthday']}),
       (_('Contact'), {'fields': ['email']}),
       (_('Other'), {'fields': ['notes']}),
    ]
    list_display = ('birthday_today','first_name', 'surname',
                    'birthday', 'email', 'notes')
    list_filter = [BirthdayFilter]


class PatientAdmin(PersonAdmin):
    fieldsets = [
       (_('Person'), {'fields': ['first_name', 'surname', 'birthday']}),
       (_('Contact'), {'fields': ['email']}),
       (_('Other'), {'fields': ['ward','notes']}),
    ]
    list_display = ('birthday_today','first_name', 'surname', 'ward',
                    'birthday', 'email', 'notes')
    list_filter = [BirthdayFilter]

admin.site.register(Patient,PatientAdmin)
admin.site.register(Volunteer,PersonAdmin)
admin.site.register(Duty)
admin.site.register(Ward)
