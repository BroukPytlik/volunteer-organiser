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
from django.utils.translation import ugettext
from django.utils.timezone import now
from django.utils.html import format_html
import datetime
import calendar
import board.helpers as h
import board.validators
from django.db.models import Q


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

#
# Second category class, currently used as a subcategory
#
class Category2(models.Model):
    class Meta:
            verbose_name_plural = _("subcategories")
            verbose_name = _("subcategory")
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=100, blank=True, null=True, verbose_name = _('contact person'))

    def __str__(self):
        return self.name

#
# Class used to keep legal values for row highlighting.
# Note: All entries has to be in English, and then translate them
# with gettext!
#
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
        pgettext('css','Silver')
        pgettext('css','Purple')
        pgettext('css','Orange')
        pgettext('css','Teal')
        pgettext('css','Aqua')
        pgettext('css','Olive')
        pgettext('css','Red')
        pgettext('css','Blue')
        pgettext('css','Green')

    def __str__(self):
        return pgettext('css',self.name)

#
# Ward for patients
#
class Ward(models.Model):
    class Meta:
            verbose_name_plural = _("wards")
            verbose_name = _("ward")
    name = models.CharField(max_length=200,verbose_name = _('name'))
    def __str__(self):
        return self.name

#
# Generic person details, common for both patient and volunteer.
#
class Person(models.Model):
    first_name = models.CharField(max_length=20, verbose_name=_('first name'))
    surname    = models.CharField(max_length=20, verbose_name=_('surname'))
    # birthdate - real date of birth
    birthdate  = models.DateField(verbose_name=_('birth date'))
    # birthday - only month and day, year is the same for all persons
    # NORMALIZED_YEAR
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

    def full_name(self, surname_first=True):
        if surname_first:
            return "%s, %s" % (self.surname, self.first_name)
        return "%s %s" % (self.first_name, self.surname_first)

    def age(self):
        return h.num_years(self.birthdate)

    # show whether the person has birthday today
    # Class method
    def birthday_today(self):
        return self.birthday == h.bday(now=True)

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
    insured = models.BooleanField(blank=True, default=False, verbose_name=_('insured'))
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
            if last_pid is None:
                last_pid = 0
            self.pid = int(last_pid) + 1
        if not self.workingSince:
            self.workingSince = now().date()
        super(Volunteer, self).save(*args, **kwargs)

    def notOnHoliday(self, when = now()):
        query = h.filter_vacant(
                Holiday.objects.filter(volunteer = self),
                'since',
                'until',
                when,
                when,
        )
        if query.count() > 0:
            return False
        return True
    notOnHoliday.short_description = _('not vacant')
    notOnHoliday.boolean = True

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
    
    def getWorkedHours(self, since=None,until=None):
        """
        Get hours the volunteer worked. If since and until is None, get
        total sum. Otherwise, filter it by the month.
        """
        if since is None and until is None:
            total = 0
            for x in WorkedHours.objects.filter(volunteer = self):
                total += x.hours
            return total
        else:
            total = 0
            for x in WorkedHours.objects.filter(volunteer = self, added__gte=since, added__lte=until):
                total += x.hours
            return total
    getWorkedHours.short_description =_('total')

    def getWorkedHoursMonthly(self):
        today = now()
        (weekday,end) = calendar.monthrange(today.year, today.month)
        return self.getWorkedHours(
                since=datetime.date(year=today.year, month=today.month, day=1),
                until=datetime.date(year=today.year, month=today.month, day=end)
            )
    getWorkedHoursMonthly.short_description = _('this month')

    # get volunteers who are vacant in the given range since start to end
    # even if it is for a part of the range
    @classmethod
    def filter_vacant_only(cls, start, end):
        return h.filter_vacant(
                cls.objects,
                'holiday__since',
                'holiday__until',
                start,
                end
        )



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
    date        = models.DateField(verbose_name=_('date'),help_text=_('If the duty is recurrent, then this will be its first day, and the duty will repeat weekly.'))
    recurrent    = models.BooleanField(default=False, verbose_name=_('recurrent'))
    normalized_date = models.DateField(blank=True, null=True) # NORMALIZED_*
    notes       = models.TextField(blank=True, null=True, verbose_name=_('notes'))
    category1        = models.ForeignKey(Category1, verbose_name=_('category'))
    category2        = models.ForeignKey(Category2, blank=True, null=True, verbose_name=_('subcategory'))


    def __str__(self):

        return "%s: <%s>, %s: <%s>, %s %s\n" % (
                _('patient'), self.patient, 
                _('volunteer'), self.volunteer, 
                self.date, h.DUTY_TIME[self.time][1]
            )

    def save(self, *args, **kwargs):
        """
        Override save, to add normalized_date for recurrent events.
        """

        if self.recurrent:
            # get the day into the normalized week
            self.normalized_date = h.normalized_week(self.date)
        else:
            self.normalized_date = None

        super(Duty, self).save(*args, **kwargs)

    
    def duty_today(self):
        if self.recurrent:
            return now().date() >= self.date and \
                h.normalized_week(now()) == self.normalized_date
        return now().date() == self.date

    def day_or_date(self):
        """
        Return day of week if the duty is recurrent,
        or date if it is a one-time.
        """
        if self.recurrent and self.date <= now().date():
            return self.day_of_week()
        return "%s (%s)" % (str(self.date), h.day_of_week(self.date, use_short=True))
    day_or_date.short_description = _('day or date')

    def day_of_week(self):
        """"
        Get week name of the duty day.
        """
        if self.date:
            return h.day_of_week(self.date)
        return ""
    day_of_week.short_description = _('day of week')

    # get duties in next X days
    @classmethod
    def filter_date_in(cls, days, skip=1):
        """
        Get list of all duties in the next X days. By default it skips
        1 day to start search tomorrow. Can be altered with skip=N.
        """
        since = now().date() + datetime.timedelta(days=skip)
        to = now().date() + datetime.timedelta(days=days)

        # Just filter out future duties.
        or_query = \
            Q(recurrent = True) \
            & Q(date__lte = to)
        if (to - since).days >= 7:
            # Entire week, nothing complicated, we already have it.
            pass
        elif to.weekday() > since.weekday():
            # we are not crossing a week boundary, so just a simple gt/lt
            or_query = or_query \
                & Q(normalized_date__gte = h.normalized_week(since)) \
                & Q(normalized_date__lte = h.normalized_week(to))
        else:
            # We crossed the week boundary, so make it a bit complicated:
            # rather than inclusion, make it exclusion and search outside.
            or_query = or_query \
                & Q(normalized_date__lte = h.normalized_week(since)) \
                & Q(normalized_date__gte = h.normalized_week(to))

        return h.filter_date_range(
                cls.objects,
                'date',
                since,
                to,
                or_query = or_query
            )

    @classmethod
    def get_date_range(cls, start, end):
        # Just filter out future duties.
        or_query = \
            Q(recurrent = True) \
            & Q(date__lte = end)
        if (end - start).days >= 7:
            # Entire week, nothing complicated, we already have it.
            pass
        elif end.weekday() > start.weekday():
            # we are not crossing a week boundary, so just a simple gt/lt
            or_query = or_query \
                & Q(normalized_date__gte = h.normalized_week(start)) \
                & Q(normalized_date__lte = h.normalized_week(end))
        else:
            # We crossed the week boundary, so make it a bit complicated:
            # rather than inclusion, make it exclusion and search outside.
            or_query = or_query \
                & Q(normalized_date__lte = h.normalized_week(start)) \
                & Q(normalized_date__gte = h.normalized_week(end))

        return h.filter_date_range(
            cls.objects,
            'date',
            start,
            end,
            or_query = or_query
        )
            
    duty_today.admin_order_field = _('duty')
    duty_today.boolean = True
    duty_today.short_description = _("Duty today?")

#
# Keep a record of what volunteer really did
#
class WorkedHours(models.Model):
    class Meta:
            verbose_name_plural = _("worked hours")
            verbose_name = _("worked hours")
    volunteer = models.ForeignKey(Volunteer, verbose_name=_('volunteer'))
    added = models.DateField(verbose_name=_('added'))
    hours = models.IntegerField(verbose_name=_('worked hours'))
    category1 = models.ForeignKey(Category1, verbose_name=_('category'))
    category2 = models.ForeignKey(Category2, blank=True, null=True, verbose_name=_('subcategory'))

    def __str__(self):
        return "%s: %d"%(self.volunteer, self.hours)

#
# Keep a record of volunteers temporarily out of work
#
class Holiday(models.Model):
    class Meta:
        verbose_name_plural = _('Vacancies')
        verbose_name = _('Vacancy')
    volunteer = models.ForeignKey(Volunteer, verbose_name=_('volunteer'))
    since = models.DateField(verbose_name=_('since'))
    until = models.DateField(null=True, blank=True, verbose_name=_('until'))
    reason = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('reason'))
    def __str__(self):
        return "%s: %s - %s" % (str(self.volunteer), self.since, self.until)

    # get volunteers who are vacant in the given range since start to end
    # even if it is for a part of the range
    @classmethod
    def filter_vacant_only(cls, start, end):
        return h.filter_vacant(
                cls.objects,
                'since',
                'until',
                start,
                end
        )

#
# allow file uploads with documents about a volunteer
#
class Attachment(models.Model):
    class Meta:
        verbose_name_plural = _('Attachments')
        verbose_name = _('Attachment')
    volunteer = models.ForeignKey(Volunteer, verbose_name=_('volunteer'))
    name = models.CharField(max_length=250, verbose_name = _('name'))
    attachment = models.FileField(verbose_name=_('attachment'), upload_to='./')
    description = models.TextField(blank=True,null=True, verbose_name = _('description'))
    created     = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def download_link(self):
        if self.attachment:
            return format_html(
                    '<a href="{}">{}</a>',
                    self.attachment.url,
                    #_('download'))
                    self.name)
        return ''
    download_link.short_description = _('download')
    
    def __str__(self):
        return ugettext('attachment')

# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
@receiver(post_delete, sender=Attachment)
def attachment_delete(sender, instance, **kwargs):
    if instance.attachment:
        # Pass false so FileField doesn't save the model.
        instance.attachment.delete(False)

