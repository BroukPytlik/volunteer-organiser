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
from django.core.urlresolvers import reverse, NoReverseMatch
import re
import datetime
from pprint import pformat
import json
import board.helpers as h
from organiser import settings

register = template.Library()

@register.filter
def none_only(v, text):
    """
    Return text if variable is none, otherwise return variable.
    A custom variant of 'yesno' filter, for None only.
    """
    if v is None:
        return text
    return v


@register.filter
def day_of_week(day):
    return h.day_of_week(day)

@register.filter
def duty_time(time):
    return h.DUTY_TIME[time][1]

@register.filter
def duty_time_short(time):
    return h.DUTY_TIME_SHORT[time][1]

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
    try:
        out = json.dumps(var, indent=4, sort_keys=True)
    except TypeError:
        #out = pformat(var, indent=4)
        out = var
    return "<pre class='dump'>%s</pre>" % (out)


def result_css(cl):
    for x in cl.result_list:
        if hasattr(x, 'cssClass'):
            yield '' if x.cssClass is None else x.cssClass.cls
        else:
            yield ''

# copy from django.contrib.admin.templatetags.admin_list
# to get an extra options
@register.inclusion_tag("admin/change_list_results.html")
def board_result_list(cl):
    """
    Displays the headers and data list together
    """
    css = list(result_css(cl))
    headers = list(admin_list.result_headers(cl))
    num_sorted_fields = 0
    results = list(admin_list.results(cl))
    for h in headers:
        if h['sortable'] and h['sorted']:
            num_sorted_fields += 1
    return {'cl': cl,
            'css': css,
            'result_hidden_fields': list(admin_list.result_hidden_fields(cl)),
            'result_headers': headers,
            'num_sorted_fields': num_sorted_fields,
            'results': results}

@register.simple_tag()
def get_index_minus_one(var, i):
    return var[i-1]

# This tag returns 'active' string if current URL matches given argument.
# source: http://stackoverflow.com/a/18772289/1023519 in comments
@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    path = context['request'].path
    try:
        pattern = '^' + reverse(pattern_or_urlname)
        if re.search(pattern, path):
            return 'active-page-link'
    except NoReverseMatch:
        pattern = pattern_or_urlname
        if getattr(settings, 'USE_I18N', False):
            print (pattern)
            if pattern[0] == '^':
                pattern = '^/' + get_language() + pattern.replace("^",'')
            print (pattern)
        if re.search(pattern, path):
            return 'active-page-link'
    return ''
