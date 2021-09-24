# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.password import *
from frappe.general import *
from frappe.student import *
from frappe.instructor import *
no_cache = 1

def get_context(context):
	context.terms=bulletin_terms()
	context.terms.insert(0,["Tous les termes","tous"])
	context.groups=bulletin_groups()
	context.groups.insert(0,"Tous les groupes")
	context.term=get_current_term()
	
