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

from django.test import TestCase
from django.utils.timezone import now

import datetime
from datetime import date

from board.models import *
import board.helpers as helpers

from . import generators as g

class DutyTests(TestCase):
    def setUp(self):
        g.init_db()
        pass

    def test_get_date_range(self):
        """
        Create duties through few weeks and try to get entries
        filtered by date range.
        """
        volunteers = g.create_volunteers(6)
        patients = g.create_patients(6)
        duties = []
        for counter in range(6):
            # create duties in three following weeks
            if counter < 2:
                # Monday
                day = date(year=2015, month=7, day=3)
            elif counter < 4:
                # Wednesday
                day = date(year=2015, month=7, day=12)
            else:
                # Sunday
                day = date(year=2015, month=7, day=23)

            d = Duty(
                volunteer = volunteers[counter],
                patient = patients[counter],
                created = now(),
                date = day,
                category1 = g.CAT
            )
            d.save()
            duties.append(d)

        # now when duties are created, do the test
        self.assertEqual(
            len(Duty.get_date_range(
                date(year=2015, month=7, day=4),
                date(year=2015, month=7, day=22)
            )),
            2)
    
    def test_recurrent_saving(self):
        """
        Test if recurrent duties are correctly mapped to normalized date.
        """

        volunteers = g.create_volunteers(1)
        patients = g.create_patients(1)

        # none
        day = date(year=2015, month=7, day=13)
        d = Duty(
            volunteer = volunteers[0],
            patient = patients[0],
            created = now(),
            date = day,
            category1 = g.CAT
        )
        d.save()
        self.assertEqual(d.normalized_date, None)

        # monday
        day = date(year=2015, month=7, day=13)
        d = Duty(
            volunteer = volunteers[0],
            patient = patients[0],
            created = now(),
            recurrent = True,
            date = day,
            category1 = g.CAT
        )
        d.save()
        self.assertEqual(d.normalized_date.weekday(), 0)

        # friday
        day = date(year=2015, month=7, day=10)
        d = Duty(
            volunteer = volunteers[0],
            patient = patients[0],
            created = now(),
            recurrent = True,
            date = day,
            category1 = g.CAT
        )
        d.save()
        self.assertEqual(d.normalized_date.weekday(), 4)


