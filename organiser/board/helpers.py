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

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import get_language
from django.template.defaulttags import register
import re
import datetime
from pprint import pformat


DAY_OF_THE_WEEK = [
    (1, _('Monday')),
    (2, _('Tuesday')),
    (3, _('Wednesday')),
    (4, _('Thursday')),
    (5, _('Friday')),
    (6, _('Saturday')),
    (7, _('Sunday')),
]

MORNING = 0
AFTERNOON = 1
DUTY_TIME = [
    (MORNING, _('Morning')),
    (AFTERNOON, _('Afternoon')),
]
DUTY_TIME_SHORT = [
    (MORNING, _('a.m.')),
    (AFTERNOON, _('p.m.')),
]

# used for Person.birthday, everyone has the same year in this value
# 2004 used as a leap year, to have 29th Feb.
BIRTHDAY_YEAR = 2004

def bday(month=None, day=None, now=False):
    """
    Return a date object set to a date in an arbitrary configured year,
    useful for comparing two dates on month/day basis (birthdays..)
    """
    if (month is None and day is None and now is False or
            month is None and day is not None or
            month is not None and day is None):
        raise ValueError("You have to call this function as bday(month, day),"
                         " or as bday(now=True).")
    if(now):
        month = timezone.now().month
        day = timezone.now().day
    return datetime.date(BIRTHDAY_YEAR, month, day)

def week(date):
    """
    Return (monday, sunday).
    Return date objects for first and last day of the week the given day belongs to.
    Get day of week, use it as a delta...
    """
    monday = date - datetime.timedelta(days = date.weekday())
    sunday = date + datetime.timedelta(days = 6-date.weekday())
    return (monday, sunday)


def years_ago(years, from_date=None):
    """
    Get a date object for a date X years ago (aka timedelta).
    Author: Rick Copeland - http://stackoverflow.com/a/765990/1023519
    """
    if from_date is None:
        from_date = timezone.now().date()
    try:
        return from_date.replace(year=from_date.year - years)
    except:
        # Must be 2/29!
        #assert from_date.month == 2 and from_date.day == 29 # can be removed
        return from_date.replace(month=3, day=1,
                             year=from_date.year-years)

def num_years(begin, end=None):
    """
    Return the number of years between two dates.
    Author: Rick Copeland - http://stackoverflow.com/a/765990/1023519
    """
    if end is None:
        end = timezone.now().date()
    if end < begin:
        tmp = end
        end = begin
        begin = tmp
    num_years = int((end - begin).days / 365.25)
    if begin > years_ago(num_years, end):
        return num_years - 1
    else:
        return num_years

def filter_date_range(queryset, column, start, end):
    """
    Filter a query to items which has value in column within
    a range stated by start and end arguments.
    """
    arg_start={ column+'__gte' : start}
    arg_end={column+'__lte' :end}
    arg_start_year={ column+'__gte' : datetime.date(end.year, 1, 1)}
    arg_end_year={column+'__lte' :datetime.date(start.year, 12, 31)}

    # if we are looking for next few days,
    # we have to bear in mind what happens on the eve
    # of a new year. So if the interval we are looking into
    # is going over the New Year, break the search into two.
    if (start.year == end.year):
        return queryset.filter(
                Q(**arg_start) &
                Q(**arg_end)
            )
    else:
        return queryset.filter(
                Q(**arg_start) &
                Q(**arg_end_year) |
                Q(**arg_start_year) &
                Q(**arg_end)
            )

