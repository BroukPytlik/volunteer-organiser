from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import urlresolvers
from django.views import generic
from django.utils import timezone
from django import forms
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _,pgettext

from django.contrib.admin import widgets
import sys
import datetime
from . import models
import board.helpers as h

# how many days should we look in front for birthdays and duties?
# 7 + 1, because we are skipping today
OVERVIEW_DAYS=8



def index(request):
    site_header ="models.Volunteer administration"
    site_title ="models.Volunteer administration"

    
    return render(request, 'board/index.html', {
        'overview_days': OVERVIEW_DAYS,
        'has_permission': request.user.is_authenticated(),

        'birthdays_patients_today': models.Patient.filter_birthday_in(0, skip=0),
        'birthdays_volunteers_today': models.Volunteer.filter_birthday_in(0, skip=0),
        'duties_today': models.Duty.filter_date_in(0, skip=0),
        'birthdays_patients_soon': models.Patient.filter_birthday_in(OVERVIEW_DAYS),
        'birthdays_volunteers_soon': models.Volunteer.filter_birthday_in(OVERVIEW_DAYS),
        'duties_soon': models.Duty.filter_date_in(OVERVIEW_DAYS),

        'duty_list_url': urlresolvers.reverse('admin:board_duty_changelist'),
        'patient_list_url': urlresolvers.reverse('admin:board_patient_changelist'),
        'volunteer_list_url': urlresolvers.reverse('admin:board_volunteer_changelist'),
        })

class WeekListSelectForm(forms.Form):
    day = forms.DateField(
                label = _('Choose a week'),
                widget = widgets.AdminDateWidget(),
                required=False,
            )

class WeekListView(generic.edit.FormView):
    site_header ="Week list"
    site_title ="Week list"
    form_class = WeekListSelectForm
    success_url = ''
    template_name='board/week_list.html'

    #week_form = WeekListSelectForm() supplied in self.get() method
    chosen_week = h.week(timezone.now().date())

    def get_initial(self):
        #initial = super(WeekListView, self).get_initial()
        #initial['day'] = timezone.now()
        #return initial
        return {'day': 'guu'}

    def get(self, request, **kwargs):
        self.week_form = self.form_class(self.request.GET)
        # get the day and compute the week - if there is a valid non-empty input
        if self.week_form.is_valid() \
            and 'day' in request.GET \
            and request.GET['day'] != '':
            self.chosen_week = h.week(
                datetime.datetime.strptime(
                    request.GET['day'],
                    '%d.%m.%Y').date()
            )
        return super(WeekListView, self).get(self, request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(WeekListView, self).get_context_data(**kwargs)
        context.update({
            'has_permission': self.request.user.is_authenticated(),
            'wards' : models.Ward.objects.all(),
            'week_form': self.week_form,
            'monday' : self.chosen_week[0],
            'sunday' : self.chosen_week[1],
            'duties_patients' : models.Duty.get_date_range(
                            self.chosen_week[0],
                            self.chosen_week[1]).filter(~Q(patient=None)).order_by('patient__surname'),
            'duties_other' : models.Duty.get_date_range(
                            self.chosen_week[0],
                            self.chosen_week[1]).filter(Q(patient=None)).order_by('volunteer__surname'),
            'categories' : models.Category1.objects.all(),
            'subcategories': models.Category2.objects.all(),

            'vacancies' : models.Holiday.filter_vacant_only(
                            self.chosen_week[0],
                            self.chosen_week[1]).order_by('volunteer__surname'),
        })
        return context

