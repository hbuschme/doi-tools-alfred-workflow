#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2015 Hendrik Buschmeier
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import json
import sys
import urllib2

try:
	query = sys.argv[1]
	resource = urllib2.urlopen('http://shortdoi.org/%s?format=json' % query).read()
	print(json.loads(resource)['ShortDOI'], end='')
except:
	print('Error getting short DOI of %s' % query)
