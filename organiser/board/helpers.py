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

# used for Person.birthday, everyone has the same year in this value
BIRTHDAY_YEAR = 2000

def bday(month=None, day=None, now=False):
    if (month is None and day is None and now is False or
            month is None and day is not None or
            month is not None and day is None):
        raise ValueError("You have to call this function as bday(month, day),"
                         " or as bday(now=True).")
    if(now):
        month = timezone.now().month
        day = timezone.now().day
    return datetime.date(BIRTHDAY_YEAR, month, day)

