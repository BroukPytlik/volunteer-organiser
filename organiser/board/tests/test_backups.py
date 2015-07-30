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

import os
import datetime
from datetime import date

from board.apps import BackupConfig

class BackupsTests(TestCase):

    def test_dir(self):
        """
        validate backup directory itself
        """
        self.assertTrue(BackupConfig.backupDir.endswith('/'),
                'BackupConfig.backupDir path has to ends with a slash (/).' )
        self.assertTrue(
                os.access(
                    os.path.dirname(BackupConfig.backupDir), os.W_OK),
                        'The backup directory is not writable (%s).' % BackupConfig.backupDir
            )
    
    def test_file_path(self):
        """
        verify the path for a backup file
        """
        path = BackupConfig.backupDir + BackupConfig.get_filename(now())
        self.assertTrue(
                os.access(
                    os.path.dirname(path), os.W_OK),
                        'The backup file path is not writable (%s).' % path
            )

    def test_check(self):
        """
        verify the correct detection whether to backup or not
        """
        self.assertTrue(
                BackupConfig.can_backup(['abc','guu'], now()))
        self.assertFalse(
                BackupConfig.can_backup([
                    'abc',
                    'guu',
                    BackupConfig.get_filename(now()),
                    ], now()))

    def test_backup_done(self):
        """
        And because the backups should be done even on test starts, verify it exists
        (in case the db file exists)
        """
        if os.path.isfile(BackupConfig.dbFile):
            dirlist = os.listdir(BackupConfig.backupDir)
            self.assertFalse(BackupConfig.can_backup(dirlist, now()))

    def test_for_delete(self):
        """
        Test the list marked for delete.
        'Create' 15 entries, and check only the oldest 5 is in the list.
        """
        dirlist = []
        for i in range(-15,0):
            dirlist.append(
                    BackupConfig.get_filename(
                        now()+datetime.timedelta(days = i)))

        res = BackupConfig.get_for_delete(dirlist)
        self.assertEqual(res, dirlist[0:5],
            'Bad for-delete list.')

    def test_for_delete_other_file(self):
        """
        Don't delete other files!
        """
        dirlist = []
        for i in range(-15,0):
            dirlist.append("db-guu-%d"%i)

        res = BackupConfig.get_for_delete(dirlist)
        self.assertEqual(res, [],
            'Bad for-delete list.')

