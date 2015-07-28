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
from django.utils.translation import ugettext_lazy as _,pgettext
from django.utils.timezone import now
import datetime
import board.helpers as h
import board.validators
#
# Just a simple class to hold categories list
#
class Category1(models.Model):
    class Meta:
            verbose_name_plural = _("categories")
            verbose_name = _("category")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Category2(models.Model):
    class Meta:
            verbose_name_plural = _("subcategories")
            verbose_name = _("subcategory")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CssClass(models.Model):
    class Meta:
            verbose_name_plural = _("styles")
            verbose_name = _("style")
    name = models.CharField(max_length=50, verbose_name=_('name'))
    cls  = models.CharField(max_length=250, verbose_name=_('CSS class'))

    def dummy_styles(self):
        """
        This is here to provide translation strings somwhere.
        """
        pgettext('css','Red')
        pgettext('css','Blue')
        pgettext('css','Green')

    def __str__(self):
        return pgettext('css',self.name)

#
# Generic person details, common for both patient and volunteer.
#
class Person(models.Model):
    first_name = models.CharField(max_length=20, verbose_name=_('first name'))
    surname    = models.CharField(max_length=20, verbose_name=_('surname'))
    # birthdate - real date of birth
    birthdate  = models.DateField(verbose_name=_('birth date'))
    # birthday - only month and day, year is the same for all persons
    # BIRTHDAY_YEAR
    birthday   = models.DateField()
    notes      = models.TextField(blank=True, null=True, verbose_name=_('notes'))
    phone1     = models.CharField(max_length=20,blank=True, null=True, verbose_name=_('phone'))
    phone2     = models.CharField(max_length=20,blank=True, null=True, verbose_name=_('phone'))
    email      = models.EmailField(blank=True, null=True, verbose_name=_('e-mail'))
    address    = models.TextField(blank=True, null=True, verbose_name=_('address'))
    cssClass  = models.ForeignKey(CssClass, blank=True, null=True, verbose_name=_('style'))

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

class Ward(models.Model):
    class Meta:
            verbose_name_plural = _("wards")
            verbose_name = _("ward")
    name = models.TextField(verbose_name = _('name'))
    def __str__(self):
        return self.name

class Patient(Person):
    class Meta:
            verbose_name_plural = _("patients")
            verbose_name = _("patient")
    diagnosis = models.TextField(blank = True, null=True,verbose_name = _('diagnosis'))
    ward = models.ForeignKey(Ward, verbose_name = _('ward'))


class Volunteer(Person):
    class Meta:
            verbose_name_plural = _("volunteers")
            verbose_name = _("volunteer")
    active = models.BooleanField(blank=True, default=True, verbose_name=_('active'))
    availableCategories = models.ManyToManyField(Category1, verbose_name = _('available categories'))
    availableSubcategories = models.ManyToManyField(Category2, blank=True, verbose_name = _('available subcategories'))
    pid = models.IntegerField(unique = True, blank = True, verbose_name = _('PID'))
    workingSince = models.DateField(blank=True, verbose_name = _('working since'))
    workedUntil = models.DateField(blank=True,null=True, verbose_name = _('worked until'))
    professions = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('professions'))
    preferredDays = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('preferred days'))

    def save(self, *args, **kwargs):
        if not self.pid:
            last_pid = Volunteer.objects.all().aggregate(models.Max('pid'))['pid__max']
            self.pid = int(last_pid) + 1
        if not self.workingSince:
            self.workingSince = now().date()
        super(Volunteer, self).save(*args, **kwargs)


    def getSubcategoriesStr(self):
        l = []
        for i in self.availableSubcategories.all():
            l.append(str(i))
        return ', '.join(l)
    getSubcategoriesStr.short_description = _('subcategories')

    def getCategoriesStr(self):
        l = []
        for i in self.availableCategories.all():
            l.append(str(i))
        return ', '.join(l)
    getCategoriesStr.short_description = _('categories')



#
# Pair volunteers and patients.
#
# In most views, show only future dutys.
# 
class Duty(models.Model):
    class Meta:
            verbose_name_plural = _("duties")
            verbose_name = _("duty")
    volunteer   = models.ForeignKey(Volunteer, verbose_name=_('volunteer'))
    patient     = models.ForeignKey(Patient, blank=True, null=True, verbose_name=_('patient'))
    created     = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_('created'))
    time        = models.IntegerField(choices=h.DUTY_TIME, default=h.MORNING, verbose_name=_('time'))
    date        = models.DateField(verbose_name=_('date'))
    notes       = models.TextField(blank=True, null=True, verbose_name=_('notes'))
    category1        = models.ForeignKey(Category1, verbose_name=_('category'))
    category2        = models.ForeignKey(Category2, blank=True, null=True, verbose_name=_('subcategory'))


    def __str__(self):

        return "%s: <%s>, %s: <%s>, %s %s\n" % (
                _('patient'), self.patient, 
                _('volunteer'), self.volunteer, 
                self.date, h.DUTY_TIME[self.time][1]
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
    

