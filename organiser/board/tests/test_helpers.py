from django.test import TestCase
from django.utils.timezone import now

import board.helpers as helpers
import datetime
from datetime import date

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
