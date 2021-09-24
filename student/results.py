

from __future__ import unicode_literals

import frappe, json
from frappe import _dict
import frappe.share
from frappe.utils import cint
from frappe.boot import get_allowed_reports
from frappe.permissions import get_roles, get_valid_perms 
from frappe.student import *
from frappe.core.doctype.domain_settings.domain_settings import get_active_modules


no_cache = 1

def get_context(context):
	
	context.currentyear= get_current_year()
	context.bulletins = get_student_bulletin()
	
	
