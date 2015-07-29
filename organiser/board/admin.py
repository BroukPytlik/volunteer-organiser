from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.core import urlresolvers
from django import forms
from django.utils.html import format_html
from django.db.models import Q

import datetime
from .models import Duty,Person,Patient,Volunteer,Category1,Category2,Ward,CssClass,WorkedHours,Holiday
import board.helpers as h
import board.validators as validators

from pprint import pprint


admin.site.site_header = _("Volunteer administration")
admin.site.site_title = _("Volunteer administration")

#
# patient filters
#
class PatientWardsFilter(admin.SimpleListFilter):
    title = _('wards')
    parameter_name = 'wards'

    def lookups(self, request, model_admin):
        return [(x.name, _(x.name)) for x in Ward.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(ward__name = self.value())
        

#
# volunteer filters
#
class VolunteerCategoriesFilter(admin.SimpleListFilter):
    title = _('categories')
    parameter_name = 'categories'

    def lookups(self, request, model_admin):
        return [(x.name, _(x.name)) for x in Category1.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(availableCategories__name = self.value())

class VolunteerSubcategoriesFilter(admin.SimpleListFilter):
    title = _('subcategories')
    parameter_name = 'subcategories'

    def lookups(self, request, model_admin):
        return [(x.name, _(x.name)) for x in Category2.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(availableSubcategories__name = self.value())

class VolunteerHolidayFilter(admin.SimpleListFilter):
    title = _('vacancy')
    parameter_name = 'vacancy'

    def lookups(self, request, model_admin):
        return (('true', _('Is vacant')), 
                ('false', _('Is not vacant'))
            )
    def queryset(self, request, queryset):
        if self.value() == 'true':
            return queryset.filter(
                    holiday__since__lte = now().date(),
                    holiday__until__gte = now().date()
                )
        elif self.value() == 'false':
            return queryset.exclude(
                    holiday__since__lte = now().date(),
                    holiday__until__gte = now().date()
                )

class VolunteerActiveFilter(admin.SimpleListFilter):
    title = _('active')
    parameter_name = 'active'

    def lookups(self, request, model_admin):
        return (('active', _('Active')), 
                ('inactive', _('Inactive'))
            )

    def queryset(self, request, queryset):
        if self.value() == 'active':
            return queryset.filter(active = True)
        elif self.value() == 'inactive':
            return queryset.filter(active = False)

#
# Duty filters
#
class DutyFilter(admin.SimpleListFilter):
    title = _('duty')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'duty_soon'
    def lookups(self, request, model_admin):
        return ( ('today', _('Today')), ('week', _('Next 7 days')))

    def queryset(self, request, queryset):
        if self.value() == 'today':
            # for 'today' it is simple...
            return queryset.filter(date = now().date())

        if self.value() == 'week':
            future_date = (now() + datetime.timedelta(days=7)).date()
            return h.filter_date_range(
                    queryset,
                    'date',
                    now().date(),
                    future_date
                )

#
# Generic person filters
#
class BirthdayFilter(admin.SimpleListFilter):
    title = _('birthday')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'birthday_soon'
    def lookups(self, request, model_admin):
        return ( ('today', _('Today')), ('week', _('Next 7 days')))

    def queryset(self, request, queryset):
        # select by date... Patient.objects.filter(birthday__month=4, birthday__day=1)
        if self.value() == 'today':
            return queryset.filter(
                    birthday = h.bday(now=True)
                )
        if self.value() == 'week':
            future_date = (now() + datetime.timedelta(days=7)).date()
            return h.filter_date_range(
                    queryset,
                    'birthday',
                    h.bday(now=True),
                    h.bday(future_date.month, future_date.day)
                )


# to ensure the volunteer wasn't assigned bad category1
class DutyAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(DutyAdminForm, self).clean()
        volunteer = cleaned_data.get('volunteer')
        category1 = cleaned_data.get('category1')
        validators.validate_duty_category1(volunteer, category1)
        return self.cleaned_data



class DutyAdmin(admin.ModelAdmin):
    # disabled, not needed
    # form = DutyAdminForm
    fieldsets = [
       (_('Where'), {'fields': ['category1','category2']}),
       (_('Who'), {'fields': ['volunteer', 'patient']}),
       (_('When'), {'fields': ['date', 'time']}),
       (_('Other'), {'fields': ['notes']}),
    ]
    list_display = ('date', 'time', 'volunteer', 'patient',
            'category1', 'category2', 'notes')
    list_filter = [DutyFilter]
        


class VolunteerAdmin(admin.ModelAdmin):
    readonly_fields = [
            'getWorkedHours',
            'getWorkedHoursMonthly',
            'notOnHoliday',
            'link_add_worked_hours',
            'link_add_duty',
            'links',
        ]
    fieldsets = [
       (_('Worked hours'), {'fields': [
           'notOnHoliday',
           ('getWorkedHoursMonthly','getWorkedHours'),
           'links',
        ]}),
       (_('Person'), {'fields': [
           'pid',
           ('first_name', 'surname'),
           'birthdate',
        ]}),
       (_('Contact'), {'fields': [
           'email',
           ('phone1','phone2'),
           'address',
        ]}),
       (_('Other'), {'fields': [
           'cssClass',
           'professions',
           'preferredDays',
           ('availableCategories', 'availableSubcategories'),
           ('workingSince', 'workedUntil'),
           'active',
           'insured',
           'notes',
        ]}),
    ]
    list_display = (
            'surname',
            'first_name',
            'birthdate',
            'links',
            'professions',
            'getCategoriesStr',
            'getSubcategoriesStr',
            'preferredDays',
            'notOnHoliday',
            'active',
            'insured',
            'notes',
        )
    list_filter = [
            BirthdayFilter,
            VolunteerActiveFilter,
            VolunteerCategoriesFilter,
            VolunteerSubcategoriesFilter,
            VolunteerHolidayFilter,
        ]

    def link_add_worked_hours(self, instance):
        url = urlresolvers.reverse('admin:%s_%s_add' % (
            WorkedHours._meta.app_label,
            WorkedHours._meta.model_name),
            args=()
        )
        return format_html(
            '<a href="{}?added={}&volunteer={}">{}</a>',
                url,
                str(now().date()),
                instance.id,
                _('hours'),
            )
    link_add_worked_hours.short_description = _('Worked hours')

    def link_add_duty(self, instance):
        url = urlresolvers.reverse('admin:%s_%s_add' % (
            Duty._meta.app_label,
            Duty._meta.model_name),
            args=()
        )
        return format_html(
            '<a href="{}?volunteer={}">{}</a>',
                url,
                instance.id,
                _('duty'),
            )
    link_add_worked_hours.short_description = _('New duty')


    def links(self, instance):
        return format_html("<ul><li>{}<li>{}</ul>", 
                self.link_add_worked_hours(instance),
                self.link_add_duty(instance),
            )
    links.short_description = _('Add')
    


    def admin_link(self, instance):

        url = urlresolvers.reverse('admin:%s_%s_change' % (instance._meta.app_label,  
                                              instance._meta.model_name),
                      args=(instance.id,))
        return format_html(u'<a href="{}">Edit</a>', url)
        # … or if you want to include other fields:
        return format_html(u'<a href="{}">Edit: {}</a>', url, instance.title)


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
       (_('Person'), {'fields': ['first_name', 'surname', 'birthdate']}),
       (_('Other'), {'fields': ['ward','diagnosis','notes','cssClass']}),
    ]
    list_display = ('surname', 'first_name',
                    'birthdate', 'ward', 'diagnosis', 'notes')
    list_filter = [BirthdayFilter, PatientWardsFilter]

class WorkedHoursAdmin(admin.ModelAdmin):
    list_display = ('volunteer','added','hours', 'category1', 'category2')

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('volunteer','since','until','reason')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Category1)
admin.site.register(Category2)
admin.site.register(Ward)
admin.site.register(CssClass)
admin.site.register(WorkedHours,WorkedHoursAdmin)
admin.site.register(Holiday, HolidayAdmin)
