

from __future__ import unicode_literals

import frappe, json
from frappe import _dict
import frappe.share
from frappe.utils import cint
from frappe.boot import get_allowed_reports
from frappe.permissions import get_roles, get_valid_perms 
from frappe.student import *
from frappe.core.doctype.domain_settings.domain_settings import get_active_modules
from datetime import date, timedelta,datetime
import locale



no_cache = 1

def get_context(context):
	user = frappe.session.user
	if not is_student(user):
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect
	context.calendarA = getschedule()
	
	today = datetime.now()
	context.now= [ int(today.strftime("%H")),int(today.strftime("%M")) ]
	start = today - timedelta(days=today.weekday())
	end = start + timedelta(days=6)
	today = today.strftime("%d-%m-%y")
	start = start.strftime("%d-%m-%y")
	end= end.strftime("%d-%m-%y")
	context.date=[start,end,today]
	
	context.tod = date.today().strftime('%A %d/%m/%Y')
	context.groupe = get_student_groupe()
	context.semaine=semaine()
	context.events=events(context.groupe)
	print(context.date)
	context.color=group_color(context.groupe)
	context.groupe = get_student_groupe_name()
	context.program = get_student_program()
