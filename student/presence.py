

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
def days_between(d1, d2):
    return ((d2 - d1).days)
    
    

def get_context(context):
	today = date.today()
	term=get_current_term()
	context.term=term
	context.year=get_current_year()
	user = frappe.session.user
	if not is_student(user):
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect
	context.name = get_student_name(user)
	context.name=name_student(context.name)
	context.attendance = get_myattendance(user)
	context.present = len([ i[0] for i in context.attendance if i[0] == "Present"] ) 
	context.absent = len([ i[0] for i in context.attendance if i[0] == "Absent"] ) 
	context.exclu = len([ i[0] for i in context.attendance if i[0] == "Exclu"] ) 
	context.presentt = len([ i[0] for i in context.attendance if i[0] == "Present" and i[2]==term]) 
	context.absentt = len([ i[0] for i in context.attendance if i[0] == "Absent" and i[2] == term]) 
	context.exclut = len([ i[0] for i in context.attendance if i[0] == "Exclu" and i[2] == term] ) 
	
	matieres = list(set([ i[1] for i in context.attendance ]))
	l=[]
	for m in matieres:
		p = len([ i[0] for i in context.attendance if i[0] == "Present" and i[1]==m] ) 
		a = len([ i[0] for i in context.attendance if i[0] == "Absent" and i[1]==m] ) 
		e = len([ i[0] for i in context.attendance if i[0] == "Exclu" and i[1]==m] ) 
		new=[m,p,a,e]
		l.append(new)
	context.att=l
	l=[]
	for m in matieres:
		p = len([ i[0] for i in context.attendance if i[0] == "Present" and i[1]==m and i[2]==term]) 
		a = len([ i[0] for i in context.attendance if i[0] == "Absent" and i[1]==m and i[2] == term]) 
		e = len([ i[0] for i in context.attendance if i[0] == "Exclu" and i[1]==m and i[2] == term]) 
		new=[m,p,a,e]
		l.append(new)
	context.attterm=l
	
	
