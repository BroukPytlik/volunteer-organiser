from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import urlresolvers
from django.template.defaulttags import register

import board.helpers as h
from .models import Duty,Patient,Volunteer,Ward

# how many days should we look in front for birthdays and duties?
OVERVIEW_DAYS=7


@register.filter
def day_of_week(day):
    return h.DAY_OF_THE_WEEK[day][1]

@register.filter
def duty_time(time):
    return h.DUTY_TIME[time][1]

def index(request):

    
    return render(request, 'board/index.html', {
        'overview_days': OVERVIEW_DAYS,

        'birthdays_patients_today': Patient.filter_birthday_in(0, skip=0),
        'birthdays_volunteers_today': Volunteer.filter_birthday_in(0, skip=0),
        'duties_today': Duty.filter_date_in(0, skip=0),
        'birthdays_patients_soon': Patient.filter_birthday_in(OVERVIEW_DAYS),
        'birthdays_volunteers_soon': Volunteer.filter_birthday_in(OVERVIEW_DAYS),
        'duties_soon': Duty.filter_date_in(OVERVIEW_DAYS),

        'duty_list_url': urlresolvers.reverse('admin:board_duty_changelist'),
        'patient_list_url': urlresolvers.reverse('admin:board_patient_changelist'),
        'volunteer_list_url': urlresolvers.reverse('admin:board_volunteer_changelist'),
        })
