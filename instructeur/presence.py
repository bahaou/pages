

from __future__ import unicode_literals

import frappe, json
from frappe import _dict
import frappe.share
from frappe import _
from frappe.utils import cint
from frappe.boot import get_allowed_reports
from frappe.permissions import get_roles, get_valid_perms 
from frappe.instructor import *
from frappe.student import *
from frappe.core.doctype.domain_settings.domain_settings import get_active_modules
from datetime import date, timedelta,datetime
import locale

no_cache = 1

	

def get_attendance(group):
	l = [r[:8] for r in  frappe.db.sql("""select student,student_name,sc.course,sc.instructor,att.status,att.date,emp.from_time,emp.to_time  from `tabStudent Attendance` as att, `tabCourse Schedule` as sc, `tabEmploi` as emp where att.course_schedule=sc.name and att.emploi=emp.name  and att.student_group=%s """,(group,) )]
	return l


def get_context(context):
	days=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
	user = frappe.session.user
	context.user=user
	context.classes=get_classes(user)
	group = frappe.request.environ.get('QUERY_STRING')
	group=group.replace("%20"," ")
	page=""
	if "?" in group:
		group,page=group.split("?")
		if page.isdigit():
			page=int(page)
		else:
			frappe.local.flags.redirect_location = "/instructeur/presence"
			raise frappe.Redirect
	else:
		page=1
	
	context.page=page
	if group !="" and group not in context.classes:
		frappe.local.flags.redirect_location = "/instructeur/presence"
		raise frappe.Redirect
	context.group=group
	context.students=get_students(group)
	for i in range(len(context.students)) :
		context.students[i] = name_student(context.students[i])
	today = datetime.now()
	context.jour=days[today.weekday()]
	context.today= today.strftime("%d-%m-%Y")
	context.calendar= getschedule('A' ,day=context.jour,groupe=group)
	allc=[]
	di=[]
	for i in range(6):
		sc=getschedule('A' ,day=days[i],groupe=group)
		di.append([days[i],len(sc)])
		allc.append([days[i],sc])
	context.allc=allc
	context.di=di
	start = today - timedelta(days=today.weekday())
	end = start + timedelta(days=6)
	start = start.strftime("%d-%m-%y")
	end= end.strftime("%d-%m-%y")
	context.semaine=[start,end]
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
