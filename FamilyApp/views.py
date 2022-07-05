from django.http import HttpResponse
from django.shortcuts import render
from FamilyApp.models import Familia
from django.template import loader
from datetime import date
# Create your views here.
marisa= Familia(p='Madre', nombre = 'Maria Isabel', apellido = 'Pereyra', birth_date= '1969-07-25',edad=53, ocupacion='Empleada')
marisa.save()
sofia= Familia(p= 'Hermana', nombre = 'Sofia', apellido = 'Medinilla', birth_date= '2002-04-04',edad=20, ocupacion='Estudiante')
sofia.save()
alejo= Familia(p='Hermano', nombre= "Alejo", apellido= 'Medinilla',edad=8, birth_date='2013-09-10')
alejo.save()
ernesto = Familia(p='Padre', nombre= "Ernesto", apellido= 'Medinilla', birth_date='1966-10-06', edad = 56)
ernesto.save()
tadeo = Familia( nombre= "Tadeo", apellido= 'Medinilla', birth_date='1999-01-07', edad = 23, ocupacion='Estudiante')
tadeo.save()
parientes = [sofia,ernesto,alejo,marisa,tadeo]
dic={'parientes': parientes}

def t_principal(self):
    
    t= loader.get_template('Ppal.html/') #Hago la carga del template
    r= t.render(dic) #En el argumento va lo que quiero renderizar
    
    return HttpResponse(r)

def t_sofia(self):
    
    t=loader.get_template('Sofia.html/')
    r=t.render(dic)
    
    return HttpResponse(r)

def t_ernesto(self):
    
    t=loader.get_template('Ernesto.html/')
    r=t.render(dic)
    
    return HttpResponse(r)

def t_marisa(self):
    
    t=loader.get_template('Marisa.html/')
    r=t.render(dic)
    
    return HttpResponse(r)

def t_alejo(self):
    
    t=loader.get_template('Alejo.html/')
    r=t.render(dic)
    
    return HttpResponse(r)

def t_tadeo(self):
    
    t=loader.get_template('Tadeo.html/')
    r=t.render(dic)
    
    return HttpResponse(r)