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


def years_ago(years, from_date=None):
    """
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
    Author: Rick Copeland - http://stackoverflow.com/a/765990/1023519
    """
    if end is None:
        end = timezone.now().date()
    num_years = int((end - begin).days / 365.25)
    if begin > years_ago(num_years, end):
        return num_years - 1
    else:
        return num_years

def filter_date_range(queryset, column, start, end):
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

@register.filter
def day_of_week(day):
    return DAY_OF_THE_WEEK[day][1]

@register.filter
def duty_time(time):
    return DUTY_TIME[time][1]

# strip language from URL when changing language
@register.filter
def strip_lang(path):
    pattern = '^(/%s)/' % get_language()
    match = re.search(pattern, path)
    if match is None:
        return path
    return path[match.end(1):]



# Custom tag for diagnostics
@register.simple_tag()
def dump(var):
    dumped = str(vars(var))
    out = ''
    indent = 0
    prev_char_br = False
    for i in range(len(dumped)):
        formatting="%s"
        c = dumped[i]
        if i < len(dumped)-1:
            n = dumped[i+1]
        else:
            n = None

        if prev_char_br == True:
            prev_char_br = False
            for x in range(indent*4):
                out += '-'

        else:
            if c == ',':
                if n != ',':
                    formatting = '%s\n'
                    prev_char_br = True

            if c == '{' or c == '(' or c == '[':
                indent += 1
                if n != '}' and n != ')' and n != ']':
                    formatting = '%s\n'
                    prev_char_br = True
            if c == '}' or c == ')' or c == ']':
                indent -= 1
                formatting = "\n%s"
                prev_char_br = True
        out += formatting%c
    return "<pre class='dump'>%s</pre>" % (out)
