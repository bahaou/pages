

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
	
	user = frappe.session.user
	if not is_student(user):
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect
	term=get_current_term()
	context.term=term
	program=get_student_program(user)
	group=get_student_groupe(user)
	group=get_student_groupe()
	exams=get_exams(group)
	
	for i in range(len(exams)):
		start=get_exam_startdate(exams[i][0])
		end=get_exam_enddate(exams[i][0])
		left=days_between(today,start)
		left2=days_between(today,end)
		exams[i]=exams[i]+[left,left2]
	
	context.exams=exams
	exam = frappe.request.environ.get('QUERY_STRING')
	context.exam = exam
	exam=exam.replace('%20',' ')
	if exam:
		start=get_exam_startdate(exam)
		end=get_exam_enddate(exam)
		exams=get_exam(exam,group)
		left=days_between(today,start)
		context.left=left
		context.start=start
		context.end=end
		context.exams=exams
		context.today=today
