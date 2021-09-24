

from __future__ import unicode_literals

import frappe, json
from frappe import _dict
import frappe.share
from frappe import _
from frappe.utils import cint
from frappe.boot import get_allowed_reports
from frappe.permissions import get_roles, get_valid_perms 
from frappe.instructor import *
from frappe.student import semaine,name_student
from frappe.core.doctype.domain_settings.domain_settings import get_active_modules
from datetime import date, timedelta,datetime
import locale

no_cache = 1

def get_context(context):
	
	user = frappe.session.user
	context.user=user
	context.username= get_instructorname(user)
	context.classes=get_classes(user)
	group = frappe.request.environ.get('QUERY_STRING')
	print(99999,group)
	group=group.replace("%20"," ")
	subject=""
	if "?" in group:
		group,subject=group.split("?")
	context.subject=subject
	
	if group !="" and group not in context.classes:
		frappe.local.flags.redirect_location = "/instructeur/notes"
		raise frappe.Redirect
	context.group=group
	context.subjects=[ i for i in get_subjects(group,user) ]
	if subject !="" and subject not in context.subjects:
		frappe.local.flags.redirect_location = "/instructeur/notes?"+group
		raise frappe.Redirect
	
	notes=get_notes(group,subject,user)
	i = context.classes.index(group)
	
	#if len(context.classes) >2:
	#	context.previous=context.classes[i-1]
	#	context.next=context.classes[i+1]
	#elif len(context.classes) ==2:
		#context.previous=context.classes[i-1]
		#context.next=context.classes[i-1]


	context.notes=notes
	


	
