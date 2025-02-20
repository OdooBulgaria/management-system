# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2012 Daniel Reis
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Management System - Claims and Nonconformities',
    'version': '1.0',
    'author': "Daniel Reis,Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'category': 'Management System',
    'depends': [
        'mgmtsystem_nonconformity'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mgmtsystem_nonconformity.xml',
        'data/mgmtsystem_nonconformity_type.xml',
    ],
    'installable': True,
    'application': False,
}
