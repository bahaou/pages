

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
	email = frappe.session.user
	context.year=get_current_year()
	context.user = email
	bulletin = frappe.request.environ.get('QUERY_STRING')
	context.bulletin = bulletin
	context.namea=arabic_name(email)
	context.student = bulletin_exist(bulletin)
	context.group= get_student_groupe(email)
	context.number=number_students(context.group)
	context.birthday= get_birthday(email)
	context.birthday=context.birthday.strftime("%Y/%m/%d")
	context.code=get_student_name(email)
	term=get_current_term()
	context.term=term
	context.line=get_line(term)
	
	
	context.journal = journal(email,context.year)
	context.cre=get_cre()
	s=context.term
	context.t=s[s.find("(")+1:s.find(")")]
	d={"Semestre 1":"الثلاثي الأول","Semestre 2":"الثلاثي الثاني","Semestre 3":"الثلاثي الثالث"}
	context.t=d[context.t]
	context.p=get_arabic_program(email)
	context.year=term_year(term)
	context.allterms=get_terms(context.year)
	context.last=[]
	
	last=False
	s=0
	c=0
	for i in context.allterms:
		if last_term(i):
			last=True
		t=i[i.find("(")+1:i.find(")")]
		a=get_averages(email,i)
		context.last.append([d[t]]+a)
		
		s+= float(a[0])*float(a[2])
		c+=float(i[2])
	
	context.last=context.last[::-1]
	if last:
		rank=annual_rank(email,context.year)
		context.last.append(['المعدل السنوي',round(s/c,2),rank,1])
	
	
	context.location=get_location(email)
	context.directeur = directeur()
	context.ordinal=nombre_ordinal(email)
