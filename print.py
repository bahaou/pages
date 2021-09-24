

from __future__ import unicode_literals

import frappe, json
from frappe import _dict
import frappe.share
from frappe.utils import cint
from frappe.boot import get_allowed_reports
from frappe.permissions import get_roles, get_valid_perms 
from frappe.student import *
from frappe.core.doctype.domain_settings.domain_settings import get_active_modules
from googletrans import Translator



def get_context(context):
	context.years=result_years()
	context.terms=result_terms()
	context.groups=result_groups()
	context.programs=result_programs()
	doc=frappe.get_doc("Education Settings")
	print(doc.current_academic_term)
