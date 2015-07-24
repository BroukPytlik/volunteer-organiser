# vim: set noexpandtab cindent sw=4 ts=4:
#
# (C)2015 Jan Tulak <jan@tulak.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
import datetime

DAY_OF_THE_WEEK = [
    (1, _(u'Monday')),
    (2, _(u'Tuesday')),
    (3, _(u'Wednesday')),
    (4, _(u'Thursday')),
    (5, _(u'Friday')),
    (6, _(u'Saturday')),
    (7, _(u'Sunday')),
]

MORNING = 0
AFTERNOON = 1
DUTY_TIME = [
    (MORNING, _('Morning')),
    (AFTERNOON, _('Afternoon')),
]

#
# Just a simple class to hold wards list
#
class Ward(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


#
# Generic person details, common for both patient and volunteer.
#
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    surname    = models.CharField(max_length=20)
    birthday   = models.DateField()
    notes      = models.TextField(blank=True, null=True)
    phone      = models.CharField(max_length=20,blank=True, null=True)
    email      = models.EmailField(blank=True, null=True)

    # show whether the person has birthday today
    def birthday_today(self):
        return self.birthday.month == timezone.now().month \
                and self.birthday.day == timezone.now().day
    birthday_today.admin_order_field = _('birthday')
    birthday_today.boolean = True
    birthday_today.short_description = _("Birthday today?")

    def __str__(self):
        return "%s, %s (%s)" % (
                self.surname, self.first_name, self.birthday
            )


class Patient(Person):
    ward = models.ForeignKey(Ward)


class Volunteer(Person):
    pass



#
# Pair volunteers and patients.
#
# In most views, show only future dutys.
# 
class Duty(models.Model):
    volunteer   = models.ForeignKey(Volunteer)
    patient     = models.ForeignKey(Patient)
    created     = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time        = models.IntegerField(choices=DUTY_TIME, default=MORNING)
    date        = models.DateField()
    #day         = models.IntegerField(default=1, choices=DAY_OF_THE_WEEK)
 #   ended       = models.DateField(blank=True, null=True)
    notes       = models.TextField(blank=True, null=True)

    def __str__(self):
        day = "%s %s" % (
                DAY_OF_THE_WEEK[self.date.weekday()][1],
                DUTY_TIME[self.time][1],
            )
        if (self.date < timezone.now().date()):
            day = "%s %s" % (_('was on'), day)
        else:
            day = "%s: %s" % (_('day'), day)


        return "%s: <%s>\n%s: <%s>\n%s\n" % (
                _('patient'), self.patient, 
                _('volunteer'), self.volunteer, 
                #_('day'), DAY_OF_THE_WEEK[self.day][1]
                day,
            )

    
    def duty_today(self):
        return timezone.now().date() == self.date
            
    duty_today.admin_order_field = _('duty')
    duty_today.boolean = True
    duty_today.short_description = _("Duty today?")
    

