# vim: set expandtab cindent sw=4 ts=4:
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
from django.utils.timezone import now
import datetime
import board.helpers as h
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
    # birthdate - real date of birth
    birthdate  = models.DateField()
    # birthday - only month and day, year is the same for all persons
    # BIRTHDAY_YEAR
    birthday  = models.DateField()
    notes      = models.TextField(blank=True, null=True)
    phone      = models.CharField(max_length=20,blank=True, null=True)
    email      = models.EmailField(blank=True, null=True)

    @classmethod
    def filter_birthday_in(cls, days, skip=1):
        """
        Get list of all people with birthday in the next X days.
        By default it skips 1 day to start search tomorrow.
        Can be altered with skip=N.
        """
        future_date = (now() + datetime.timedelta(days=days)).date()
        start = (now() + datetime.timedelta(days=skip)).date()
        return h.filter_date_range(
                cls.objects,
                'birthday',
                h.bday(start.month, start.day),
                h.bday(future_date.month, future_date.day)
            )

    def age(self):
        return h.num_years(self.birthdate)

    # show whether the person has birthday today
    # Class method
    def birthday_today(self):
        return self.birthday == helper.bday(now=True)

    birthday_today.admin_order_field = _('birthday')
    birthday_today.boolean = True
    birthday_today.short_description = _("Birthday today?")

    def save(self, *args, **kwargs):
        self.birthday = h.bday(self.birthdate.month, self.birthdate.day)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return "%s, %s (%s)" % (
                self.surname, self.first_name, self.birthdate
            )


class Patient(Person):
    ward = models.ForeignKey(Ward)


class Volunteer(Person):
    active = models.BooleanField(blank=True, default=True)
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
    time        = models.IntegerField(choices=h.DUTY_TIME, default=h.MORNING)
    date        = models.DateField()
    notes       = models.TextField(blank=True, null=True)

    def __str__(self):
        day = "%s %s" % (
                h.DAY_OF_THE_WEEK[self.date.weekday()][1],
                h.DUTY_TIME[self.time][1],
            )
        if (self.date < now().date()):
            day = "%s %s" % (_('was on'), day)
        else:
            day = "%s: %s" % (_('day'), day)


        return "%s: <%s>\n%s: <%s>\n%s\n" % (
                _('patient'), self.patient, 
                _('volunteer'), self.volunteer, 
                day,
            )

    
    def duty_today(self):
        return now().date() == self.date


    # get duties in next X days
    @classmethod
    def filter_date_in(cls, days, skip=1):
        """
        Get list of all duties in the next X days. By default it skips
        1 day to start search tomorrow. Can be altered with skip=N.
        """
        future_date = (now() + datetime.timedelta(days=days)).date()
        return h.filter_date_range(
                cls.objects,
                'date',
                now().date() + datetime.timedelta(days=skip),
                future_date
            )
            
    duty_today.admin_order_field = _('duty')
    duty_today.boolean = True
    duty_today.short_description = _("Duty today?")
    
