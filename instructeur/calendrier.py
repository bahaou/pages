

from __future__ import unicode_literals

import frappe, json
from frappe import _dict
import frappe.share
from frappe.utils import cint
from frappe.boot import get_allowed_reports
from frappe.permissions import get_roles, get_valid_perms 
from frappe.instructor import *
from frappe.student import semaine
from frappe.core.doctype.domain_settings.domain_settings import get_active_modules
from datetime import date, timedelta,datetime
import locale

    

no_cache = 1

def get_context(context):
	user = frappe.session.user
	context.user=user
	n= get_instructorname(user)
	if n=="no":
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect
	
	context.n = n 
	context.calendarA = getschedule('A',user)
	today = datetime.now()
	context.now= [ int(today.strftime("%H")),int(today.strftime("%M")) ]
	start = today - timedelta(days=today.weekday())
	end = start + timedelta(days=6)
	today = today.strftime("%d-%m-%y")
	start = start.strftime("%d-%m-%y")
	end= end.strftime("%d-%m-%y")
	context.date=[start,end,today]
	context.tod = date.today().strftime('%A %d/%m/%Y')
	
	context.semaine=semaine()
