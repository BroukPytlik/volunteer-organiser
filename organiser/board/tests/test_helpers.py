from django.test import TestCase
from django.utils.timezone import now

import board.helpers as helpers
import datetime
from datetime import date
from . import generators as g
from board.models import *

class SimpleHelpersTests(TestCase):

    def test_years_ago(self):
        """
        helpers.years_ago should return a date object representing a day
        exactly X years ago.
        """
        self.assertEqual(
                helpers.years_ago(0, date(2015, 4, 28)),
                date(2015, 4, 28)
        )
        self.assertEqual(
                helpers.years_ago(2, date(2015, 4, 28)),
                date(2013, 4, 28)
        )
        self.assertEqual(
                helpers.years_ago(-1, date(2015, 4, 28)),
                date(2016, 4, 28)
        )
        self.assertEqual(
                helpers.years_ago(1, date(2004, 2, 29)),
                date(2003, 3, 1)
        )

    def test_num_years(self):
        """
        num_years should get number of years between two dates
        """
        self.assertEqual(
                helpers.num_years(
                    date(2015, 3, 11),
                    date(2015, 4, 28)
                ), 0 )
        self.assertEqual(
                helpers.num_years(
                    date(2014, 5, 11),
                    date(2015, 4, 28)
                ), 0 )
        self.assertEqual(
                helpers.num_years(
                    date(2014, 3, 11),
                    date(2015, 4, 28)
                ), 1 )
        self.assertEqual(
                helpers.num_years(
                    date(2015, 3, 11),
                    date(2014, 2, 28)
                ), 1 )

    def test_bday(self):
        """
        bday turns any date into a date in a specific year, 
        for comparison of month and day
        """
        self.assertEqual(
                helpers.bday( 4, 14),
                date(helpers.BIRTHDAY_YEAR, 4, 14))
        self.assertEqual(
                helpers.bday(now=True),
                date(helpers.BIRTHDAY_YEAR, now().month, now().day))


    def test_week(self):
        """
        week should return first and last day of the week the given day belongs to.
        """
        correct_mon = date(year=2015, month=6, day=29)
        correct_sun = date(year=2015, month=7, day=5)

        # check week boundary - monday
        test = date(year=2015, month=6, day = 29)
        (res_mon, res_sun) = helpers.week(test)
        self.assertTrue(res_mon == correct_mon and res_sun == correct_sun)

        # check week boundary - sunday
        test = date(year=2015, month=7, day = 5)
        (res_mon, res_sun) = helpers.week(test)
        self.assertTrue(res_mon == correct_mon and res_sun == correct_sun)

        # check middle of the week
        test = date(year=2015, month=7, day = 1)
        (res_mon, res_sun) = helpers.week(test)
        self.assertTrue(res_mon == correct_mon and res_sun == correct_sun)

class VacancyTests(TestCase):
    """
    Check if vacancy filter correctly gets people who are vacant
    during a period
    """

    def setUp(self):
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

        Holiday(volunteer = volunteers[4],
                since = date(year=2015, month=6, day=1),
                until = date(year=2015, month=7, day=5)
        ).save()


        # someone has two vacancies in a month
        Holiday(volunteer = volunteers[3],
                since = date(year=2015, month=6, day=1),
                until = date(year=2015, month=7, day=5)
        ).save()
        Holiday(volunteer = volunteers[3],
                since = date(year=2015, month=7, day=15),
                until = date(year=2015, month=7, day=30)
        ).save()

        # and someone has a vaccancy with uncertain end
        Holiday(volunteer = volunteers[5],
                since = date(year=2015, month=8, day=15),
        ).save()


    def test_vacancy_basic(self):

        self.assertEqual(
            len(helpers.filter_vacant(
                Holiday.objects,
                'since',
                'until',
                date(year=2015, month=7, day=1),
                date(year=2015, month=7, day=30),
            )), 6)

        self.assertEqual(
            len(helpers.filter_vacant(
                Holiday.objects,
                'since',
                'until',
                date(year=2015, month=7, day=1),
                date(year=2015, month=7, day=14),
            )), 5)
        self.assertEqual(
            len(helpers.filter_vacant(
                Holiday.objects,
                'since',
                'until',
                date(year=2015, month=7, day=5),
                date(year=2015, month=7, day=5),
            )), 4)
        self.assertEqual(
            len(helpers.filter_vacant(
                Holiday.objects,
                'since',
                'until',
                date(year=2015, month=7, day=26),
                date(year=2015, month=7, day=30),
            )), 1)

        self.assertEqual(
            len(helpers.filter_vacant(
                Holiday.objects,
                'since',
                'until',
                date(year=2015, month=3, day=1),
                date(year=2015, month=3, day=30),
            )), 0)


    def test_vacancy_uncertain_ending(self):
        # two for uncertain end
        # one which partly cover the starting day
        self.assertEqual(
            len(helpers.filter_vacant(
                Holiday.objects,
                'since',
                'until',
                date(year=2015, month=8, day=10),
                date(year=2015, month=8, day=20),
            )), 1)
        # one search inside of the uncertain vaccancy
        self.assertEqual(
            len(helpers.filter_vacant(
                Holiday.objects,
                'since',
                'until',
                date(year=2015, month=8, day=20),
                date(year=2015, month=8, day=30),
            )), 1)

        self.assertEqual(
            len(helpers.filter_vacant(
                Holiday.objects,
                'since',
                'until',
                date(year=2015, month=8, day=20),
                date(year=2015, month=8, day=20),
            )), 1)
    def test_volunteers(self):
        # and test it through volunteers as well
        self.assertEqual(
            len(helpers.filter_vacant(
                Volunteer.objects,
                'holiday__since',
                'holiday__until',
                date(year=2015, month=8, day=20),
                date(year=2015, month=8, day=30),
            )), 1)

        self.assertEqual(
            len(helpers.filter_vacant(
                Volunteer.objects,
                'holiday__since',
                'holiday__until',
                date(year=2015, month=3, day=1),
                date(year=2015, month=3, day=30),
            )), 0)


    def test_volunteers_inverted(self):
        # check for cases between two entries for a volunteer
        self.assertEqual(
            len(helpers.filter_vacant(
                Volunteer.objects,
                'holiday__since',
                'holiday__until',
                date(year=2015, month=7, day=10),
                date(year=2015, month=7, day=10),
                inverted=True,
            )), 8)
        # a volunteer with multiple entries, we are in middle of one
        self.assertEqual(
            len(helpers.filter_vacant(
                Volunteer.objects,
                'holiday__since',
                'holiday__until',
                date(year=2015, month=7, day=15),
                date(year=2015, month=7, day=15),
                inverted=True,
            )), 7)
        # check if we can filter out volunteers WITHOUT a vacancy at a moment
        self.assertEqual(
            len(helpers.filter_vacant(
                Volunteer.objects,
                'holiday__since',
                'holiday__until',
                date(year=2015, month=3, day=1),
                date(year=2015, month=3, day=30),
                inverted=True,
            )), 10)
        
        self.assertEqual(
            len(helpers.filter_vacant(
                Volunteer.objects,
                'holiday__since',
                'holiday__until',
                date(year=2015, month=3, day=1),
                date(year=2015, month=3, day=1),
                inverted=True,
            )), 10)

        # everyone except the uncertain end should be available
        self.assertEqual(
            len(helpers.filter_vacant(
                Volunteer.objects,
                'holiday__since',
                'holiday__until',
                date(year=2015, month=8, day=20),
                date(year=2015, month=8, day=20),
                inverted=True,
            )), 9)


