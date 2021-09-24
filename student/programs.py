

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
	user = frappe.session.user
	if not is_student(user):
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect
		
	context.groupe= get_student_groupe(user)
	context.programme= get_student_program(user)
	context.program=get_program(context.programme)
	context.year = get_current_year()
