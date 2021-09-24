

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
	print(10*"*")
	bul = frappe.request.environ.get('QUERY_STRING')
	bul=bul.replace("%20"," ")
	print(bul)
	if '&&&' in bul:
		print('yes')
		students,terms = bul.split('&&&')
		students=students.split('?')
		if terms == 'tous':
			terms=['tous']
		else:
			terms=terms.split('&')
		bulletins=get_bulletins2(students,terms)
	else:
		terms,groups=bul.split('?')
		terms=terms.split('&')
		groups=groups.split('&')
		bulletins=get_bulletins(terms,groups)
	allbulletins =[]
	d2={"Semestre 1":"الثلاثي الأول","Semestre 2":"الثلاثي الثاني","Semestre 3":"الثلاثي الثالث","Trimestre 1":"الثلاثي الأول","Trimestre 2":"الثلاثي الثاني","Trimestre 3":"الثلاثي الثالث"}
	
	for b in bulletins:
		
		d={}
		email=bulletin_exist(b)
		namea=arabic_name(email)
		d['namea']=namea
		group= get_student_groupe_name(email)
		groupe=get_student_groupe(email)
		d['group']=group
		d['number']=number_students(groupe)
		d['birthday']= get_birthday(email)
		term=get_term(b)
		
		d['birthday']=d['birthday'].strftime("%Y/%m/%d")
		d['code']=get_student_name(email)
		d['results'] = get_student_fullbulletin(email,term,"a")
		d['term']=term
		s=d['term']
		d['t']=s[s.find("(")+1:s.find(")")]
		d['t']=d2[d['t']]
		d['p']=get_arabic_program(email)
		d['year']=term_year(d['term'])
		na=get_student_name(email)
		allterms=termsstudent(na)
		
		last=[]
		lastb=False
		s=0
		c=0
		for i in allterms:
			if last_term(i):
				lastb=True
			t=i[i.find("(")+1:i.find(")")]
			a=get_averages(email,i)
			last.append([d2[t]]+a)
			
			s+= float(a[0])*float(a[2])
			c+=float(i[2])
		
		last=last[::-1]
		if lastb:
			rank=annual_rank(email,d['year'])
			last.append(['المعدل السنوي',round(s/c,2),rank,1])
		d['last']=last
		d['location']=get_location(email)
		d['ordinal']=nombre_ordinal(email)
		allbulletins.append(d)
		
	context.allbulletins=allbulletins
	context.year=get_current_year()
	context.cre=get_cre()
	context.directeur = directeur()
	context.institut=get_institut()
	
