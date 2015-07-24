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

DAY_OF_THE_WEEK = {
    '0' : _(u'None'),
    '1' : _(u'Monday'),
    '2' : _(u'Tuesday'),
    '3' : _(u'Wednesday'),
    '4' : _(u'Thursday'),
    '5' : _(u'Friday'),
    '6' : _(u'Saturday'),
    '7' : _(u'Sunday'),
}

class Ward(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Person(models.Model):
	first_name = models.CharField(max_length=20)
	surname    = models.CharField(max_length=20)
	birthday   = models.DateField()
	notes      = models.TextField(blank=True)
	phone      = models.TextField(blank=True)
	email      = models.EmailField(blank=True)

	# select by date... Patient.objects.filter(birthday__month=4, birthday__day=1)
	def birthday_today(self):
		return self.birthday.month == timezone.now().month \
				and self.birthday.day == timezone.now().day
	birthday_today.admin_order_field = _('birthday')
	birthday_today.boolean = True
	birthday_today.short_description = _("Birthday today?")

	def __str__(self):
		return "First name: %s, Surname: %s, Birthday: %s" % (
				self.first_name, self.surname, self.birthday
			)

class Patient(Person):
	ward = models.ForeignKey(Ward)

class Volunteer(Person):
	pass

class Duty(models.Model):
	volunteer   = models.ForeignKey(Volunteer)
	patient     = models.ForeignKey(Patient)
	time        = models.TimeField()
	day         = models.CharField(max_length=1, default='0')
	created     = models.DateTimeField(auto_now_add=True, blank=True)
	recurent    = models.BooleanField(blank=True)

	def __str__(self):
		return "Patient: <%s>\nVolunteer: <%s>\nTime: %s\n" % (
				self.patient, self.volunteer, self.time
			)
	

