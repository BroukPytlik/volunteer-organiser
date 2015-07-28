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
from django.utils.translation import get_language
from django.contrib.admin.templatetags import admin_list
from django import template
import re
import datetime
from pprint import pformat
import json

register = template.Library()

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
    out = json.dumps(var, indent=4, sort_keys=True)
    return "<pre class='dump'>%s</pre>" % (out)

# copy from django.contrib.admin.templatetags.admin_list
# to get an extra options
@register.inclusion_tag("admin/change_list_results.html")
def board_result_list(cl, extra):
    """
    Displays the headers and data list together
    """
    headers = list(admin_list.result_headers(cl))
    num_sorted_fields = 0
    for h in headers:
        if h['sortable'] and h['sorted']:
            num_sorted_fields += 1
    return {'cl': cl,
            'extra': extra,
            'result_hidden_fields': list(admin_list.result_hidden_fields(cl)),
            'result_headers': headers,
            'num_sorted_fields': num_sorted_fields,
            'results': list(admin_list.results(cl))}
