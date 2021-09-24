

from __future__ import unicode_literals

import frappe, json
from frappe import _dict
import frappe.share
from frappe.utils import cint
from frappe.boot import get_allowed_reports
from frappe.permissions import get_roles, get_valid_perms 
from frappe.student import *
from frappe.core.doctype.domain_settings.domain_settings import get_active_modules
from frappe.instructor import *
from frappe.general import *

no_cache = 1

def get_context(context):
	user = frappe.session.user
	if user=="Guest":
		context.guest='true'
		frappe.local.flags.redirect_location = "/E-learning"
		raise frappe.Redirect
	context.guest='false'
	context.term=get_current_term()
	
	
	
	
	if  is_student(user):
		context.heis="student"
		context.classes=get_student_courses()
		context.classes.sort()
		group=get_student_groupe()
		context.group=group[:-8]
		context.currentclass=context.classes[0]
		
		context.chat=chat(group,context.currentclass,context.term,'first')
		context.max=maxx(group,context.currentclass,context.term)
		
	elif is_instructor(user):
		context.heis="instructor"
		context.classes=get_classescourses()
		
		context.classes.sort()
		context.currentclass=context.classes[0]
		getmeetings()
		context.name=get_instructorname()
		user = frappe.session.user
		group,course=context.currentclass.split('_')
		group=group+'-'+context.term[:8]
			
		context.chat=chat(group,course,context.term,'first')
		context.max=maxx(group,course,context.term)
	else:	
		frappe.local.flags.redirect_location = "/E-learning"
		raise frappe.Redirect
	
