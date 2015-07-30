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

from django.apps import AppConfig
from organiser.settings import BASE_DIR
from django.utils.timezone import now
import os
import shutil

class BackupConfig(AppConfig):
    name = 'board.apps'
    backupDir = BASE_DIR + "/backups/"
    dbFile = BASE_DIR + "/db.sqlite3"


    def ready(self):
        dirlist = os.listdir(self.backupDir)
        for item in self.get_for_delete(dirlist):
            print ('Removing old backup: %s' % item )
            os.remove(self.backupDir + item)

        if self.can_backup(dirlist, now()):
            shutil.copyfile(self.dbFile, self.backupDir + self.get_filename(now()))


    @classmethod
    def get_for_delete(self, dirlist):
        newlist=[]
        for item in dirlist:
            if item[:3] == 'db-' and item[-8:] == '.sqlite3':
                newlist.append(item)
        return newlist[:-10]


    @classmethod
    def can_backup(cls, dirlist, date):
        return False if cls.get_filename(date) in dirlist else True

    @classmethod
    def get_filename(cls, date):
        return "db-%s.sqlite3" % (date.strftime('%Y-%m-%d'))

