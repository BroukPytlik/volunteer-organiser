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


    def test_vacancy(self):
        """
        Check if vacancy filter correctly gets people who are vacant
        during a period
        """
        volunteers = g.create_volunteers(10)

        Holiday(volunteer = volunteers[0],
                since = date(year=2015, month=7, day=1),
                until = date(year=2015, month=7, day=25)
        ).save()

        Holiday(volunteer = volunteers[1],
                since = date(year=2015, month=7, day=4),
                until = date(year=2015, month=7, day=4)
        ).save()

        Holiday(volunteer = volunteers[2],
                since = date(year=2015, month=7, day=1),
                until = date(year=2015, month=7, day=15)
        ).save()

        Holiday(volunteer = volunteers[3],
                since = date(year=2015, month=7, day=15),
                until = date(year=2015, month=7, day=30)
        ).save()

        # someone has two vacancies in a month
        Holiday(volunteer = volunteers[3],
                since = date(year=2015, month=6, day=1),
                until = date(year=2015, month=7, day=5)
        ).save()

        Holiday(volunteer = volunteers[4],
                since = date(year=2015, month=6, day=1),
                until = date(year=2015, month=7, day=5)
        ).save()

        # now do the test - both volunteer and Holiday version
        self.assertEqual(
            len(Holiday.filter_vacant_only(
                date(year=2015, month=7, day=1),
                date(year=2015, month=7, day=30),
            )), 6)

        self.assertEqual(
            len(Holiday.filter_vacant_only(
                date(year=2015, month=7, day=1),
                date(year=2015, month=7, day=14),
            )), 5)
        self.assertEqual(
            len(Holiday.filter_vacant_only(
                date(year=2015, month=7, day=5),
                date(year=2015, month=7, day=5),
            )), 4)
        self.assertEqual(
            len(Holiday.filter_vacant_only(
                date(year=2015, month=7, day=26),
                date(year=2015, month=7, day=30),
            )), 1)

        self.assertEqual(
            len(Holiday.filter_vacant_only(
                date(year=2015, month=3, day=1),
                date(year=2015, month=3, day=30),
            )), 0)

        # volunteers
        self.assertEqual(
            len(Volunteer.filter_vacant_only(
                date(year=2015, month=7, day=1),
                date(year=2015, month=7, day=30),
            )), 6)

        self.assertEqual(
            len(Volunteer.filter_vacant_only(
                date(year=2015, month=7, day=1),
                date(year=2015, month=7, day=14),
            )), 5)
        self.assertEqual(
            len(Volunteer.filter_vacant_only(
                date(year=2015, month=7, day=5),
                date(year=2015, month=7, day=5),
            )), 4)
        self.assertEqual(
            len(Volunteer.filter_vacant_only(
                date(year=2015, month=7, day=26),
                date(year=2015, month=7, day=30),
            )), 1)

        self.assertEqual(
            len(Volunteer.filter_vacant_only(
                date(year=2015, month=3, day=1),
                date(year=2015, month=3, day=30),
            )), 0)


    def test_age(self):
        """
        Check if the age of a person is correctly computed.
        """
        bd = datetime.date( 1950, 1, 25 )
        v = Volunteer(birthdate   = bd)
        self.assertEqual(v.age(), helpers.num_years(bd))

        

