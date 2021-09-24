

from __future__ import unicode_literals

import frappe, json
from frappe import _dict
import frappe.share
from frappe.utils import cint
from frappe.boot import get_allowed_reports
from frappe.permissions import get_roles, get_valid_perms 
from frappe.student import *
from frappe.core.doctype.domain_settings.domain_settings import get_active_modules



def get_context(context):
	email = frappe.session.user
	if not is_student(email):
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect
	context.user = email
	bulletin = frappe.request.environ.get('QUERY_STRING')
	context.bulletin = bulletin
	name = get_student_name()
	context.student = bulletin_exist(bulletin)
	
	
	if context.student == "None":
		frappe.local.flags.redirect_location = "/student/results"
		raise frappe.Redirect
	else :
		if context.student != email:
			frappe.local.flags.redirect_location = "/"
			raise frappe.Redirect
	term=get_term(bulletin)
	context.term=term
	context.line=get_line(term)
	context.result = get_result(bulletin)
	context.results = get_student_fullbulletin(email,term)
	context.year=term_year(term)
	context.allterms=termsstudent(name)
	
	
	context.last=[]
	
	last=False
	s=0
	c=0
	for i in context.allterms:
		if last_term(i):
			last=True
		t=i[i.find("(")+1:i.find(")")]
		a=get_averages(email,i)
		context.last.append([t]+a)
		
		s+= float(a[0])*float(a[2])
		c+=float(i[2])
	
	context.last=context.last[::-1]
	if last:
		rank=annual_rank(email,context.year)
		context.last.append(['annuelle',round(s/c,2),rank,1])
	
	
	
