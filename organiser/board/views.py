from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import urlresolvers

from .models import Duty,Patient,Volunteer,Ward

def index(request):

    
    return render(request, 'board/index.html', {

        'birthdays': 'Nobody but us chickens!',
        'dutys': 'Nobody but us chickens!',

        'duty_list_url': urlresolvers.reverse('admin:board_duty_changelist'),
        'patient_list_url': urlresolvers.reverse('admin:board_patient_changelist'),
        'volunteer_list_url': urlresolvers.reverse('admin:board_volunteer_changelist'),
        })
