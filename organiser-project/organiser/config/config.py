# -*- coding: utf-8 -*-
# vim: set noexpandtab cindent sw=4 ts=4:
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
from organiser.config.routes import routes


debug = {
	'enabled': True
}
routes = {
	'index': {
		'path': '/',
		'options': {'controller': 'organiser.controllers.Index'}
	},
	'volunteers': {
		'path': '/volunteers',
		'options': {'controller': 'organiser.controllers.Volunteers'}
	},
	'patients': {
		'path': '/patients',
		'options': {'controller': 'organiser.controllers.Patients'}
	},
	'board': {
		'path': '/board',
		'options': {'controller': 'organiser.controllers.Board'}
	},
}
dependencies = {
	'definitions': {
		'db': {
			'item': 'organiser.db.create_session',
			'init': {
				'connection_string': 'sqlite://sqlite.db'
			}
		},
		'organiser.controllers.board.Board': {
			'property': {
				'db': 'db'
			}
		}
	}
}

