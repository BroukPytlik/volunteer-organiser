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

from django.utils.timezone import now

import datetime
from datetime import date

from board.models import *

def create_volunteers(count):
    for i in range(count):
        v = Volunteer(
            first_name  = "name %d"%i,
            surname     = "surname %d"%i,
            # don't get into future with birthdays
            birthdate   = datetime.date( 1900 + (i*10+i) % 110, 1 + i % 12, 1 + i % 28),
            active      = i % 4 != 0,
            insured     = i % 2 == 0,
            workingSince = now().date(),
        )
        v.save()

