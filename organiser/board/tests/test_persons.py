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

class PersonTests(TestCase):
    def setUp(self):
        pass

    def test_create_volunteer(self):
        v = Volunteer(
            first_name  = "name",
            surname     = "surname",
            birthdate   = datetime.date( 1950, 1, 25 ),
            active      = True,
            insured     = True,
            workingSince = now().date(),
        )
        v.save()

    def test_birthday_setting(self):
        """
        Every person should have created birthday entry from birthdate
        automaticaly.
        """
        g.create_volunteers(1)
        v = Volunteer.objects.get(id=1)
        self.assertEqual(
                v.birthday,
                helpers.bday(v.birthdate.month, v.birthdate.day))


    def test_birthday_today(self):
        bd = datetime.date( 1950, now().month, now().day )
        v = Volunteer(birthdate   = bd)
        v.save()
        self.assertTrue(v.birthday_today())

    def test_birthday_filter(self):
        """
        Verify if we correctly gets list of people with birthdays in next X days.
        """
        today = now().date()
        normalized = helpers.bday(today.month, today.day)
        tomorrow = normalized + datetime.timedelta(days=1)
        next_week = normalized + datetime.timedelta(days=8)
        for i in range (-5,10):
            v = Volunteer(
                    surname="bd-filter-%d" % i,
                    birthdate = today + datetime.timedelta(days=i))
            v.save()

        # today
        for v in Volunteer.filter_birthday_in(days=0, skip=0):
            self.assertTrue(v.birthday_today())
        # next 7 days
        for v in Volunteer.filter_birthday_in(7):
            self.assertTrue( tomorrow <= v.birthday <= next_week )


    def test_age(self):
        """
        Check if the age of a person is correctly computed.
        """
        bd = datetime.date( 1950, 1, 25 )
        v = Volunteer(birthdate   = bd)
        self.assertEqual(v.age(), helpers.num_years(bd))


    def test_on_holiday(self):
        """
        Check on-holiday reporting.
        """
        v = Volunteer(birthdate = datetime.date(1950, 1, 1))
        v.save()
        h = Holiday(
                volunteer = v,
                since = datetime.date(2015, 7, 5),
                until = datetime.date(2015, 7, 15)
        )
        h.save()

        self.assertTrue(
                v.notOnHoliday(datetime.date(2015,7,1)))

        self.assertFalse(
                v.notOnHoliday(datetime.date(2015,7,5)))
        self.assertFalse(
                v.notOnHoliday(datetime.date(2015,7,10)))
        self.assertFalse(
                v.notOnHoliday(datetime.date(2015,7,15)))
        h.delete()
        v.delete()

    def test_on_holiday_multiple_terms(self):
        """
        Check on-holiday reporting if we are between two holidays 
        for a volunteer.
        """
        v = Volunteer(birthdate = datetime.date(1950, 1, 1))
        v.save()
        h1 = Holiday(
                volunteer = v,
                since = datetime.date(2015, 7, 5),
                until = datetime.date(2015, 7, 10)
        )
        h1.save()
        h2 = Holiday(
                volunteer = v,
                since = datetime.date(2015, 7, 20),
                until = datetime.date(2015, 7, 25)
        )
        h2.save()

        self.assertTrue(
                v.notOnHoliday(datetime.date(2015,7,1)))
        self.assertTrue(
                v.notOnHoliday(datetime.date(2015,7,15)))

        self.assertFalse(
                v.notOnHoliday(datetime.date(2015,7,5)))
        self.assertFalse(
                v.notOnHoliday(datetime.date(2015,7,10)))
        self.assertFalse(
                v.notOnHoliday(datetime.date(2015,7,22)))

        h1.delete()
        h2.delete()
        v.delete()

    def test_on_holiday_uncertain(self):
        """
        Check on-holiday reporting for uncertain endings.
        """
        v = Volunteer(birthdate = datetime.date(1950, 1, 1))
        v.save()
        h = Holiday(
                volunteer = v,
                since = datetime.date(2015, 7, 5),
        )
        h.save()

        self.assertTrue(
                v.notOnHoliday(datetime.date(2015,7,1)))

        self.assertFalse(
                v.notOnHoliday(datetime.date(2015,7,5)))
        self.assertFalse(
                v.notOnHoliday(datetime.date(2015,7,15)))

        h.delete()
        v.delete()


