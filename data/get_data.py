#!/usr/bin/env python
# encoding: utf-8
from lxml import html
import requests
from bs4 import BeautifulSoup
from pprint import pprint; 

#== File to get the subjects information from UMA directory of subjects using scraping
#= Links to download webs
data_links = { '403': { 'title_ES': u'Escuela Politécnica Superior', 'title': 'politechnical_school', 'degrees': [
    { '5044': { 'title_ES': u'Graduado/a en Ingeniería Eléctrica', 'title': 'electrical_engineering_degree' }}, 
    { '5208': { 'title_ES': u'Graduado/a en Ingeniería Eléctrica + Graduado/a en Ingeniería Mecánica', 'title': 'electrical_and_mechanical_engineering_degree' }}, 
    { '5045': { 'title_ES': u'Graduado/a en Ingeniería Electrónica Industrial', 'title': 'industiral_electronic_engineering_degree' }}, 
    { '5209': { 'title_ES': u'Graduado/a en Ingeniería Electrónica Industrial + Graduado/a en Ingeniería Eléctrica', 'title': 'industiral_electronic_and_electrical_engineering_degree' }},
    { '5046': { 'title_ES': u'Graduado/a en Ingeniería en Diseño Industrial y Desarrollo del Producto', 'title': 'design_engineering_degree' }}, 
    { '5043': { 'title_ES': u'Graduado/a en Ingeniería Mecánica', 'title': 'mecanical_engineering_degree' }}, 
    { '5207': { 'title_ES': u'Graduado/a en Ingeniería Mecánica + Graduado/a en Ingeniería en Diseño Industrial y Desarrollo del Producto', 'title': 'mecanical_and_design_engineering_degree' }}
    ]},
'306': {'title_ES': 'Escuela Técnica Superior de Ingeniería Informática', 'title': 'computer_science_school', 'degrees': [
    { '5104': {'title_ES': u'Graduado/a en Ingeniería de Computadores', 'title': 'hardware_engineering_degree' }}, 
    { '5157': {'title_ES': u'Graduado/a en Ingeniería de la Salud', 'title': 'health_engineering_degree' }}, 
    { '5103': {'title_ES': u'Graduado/a en Ingeniería del Software', 'title': 'software_engineering_degree' }}, 
    { '5102': {'title_ES': u'Graduado/a en Ingeniería Informática', 'title': 'computer_engineering_degree' }}
    ]},
 '305': {'title_ES': 'Facultad de Derecho', 'title': 'law_school', 'degrees': [
    { '5112': {'title_ES': 'Graduado/a en Criminología', 'title': 'criminology_degree' }}, 
    { '5113': {'title_ES': 'Graduado/a en Derecho', 'title': 'law_degree' }},
    ]},}
#TODO: follow with the next degrees and schools following the pattern above
#{ 314 : Escuela Técnica Superior de Arquitectura', 'title': '', 'degrees': 
    #{ 5016 : Graduado/a en Arquitectura', 'title': '' }, 
#{ 307 : Escuela Técnica Superior de Ingeniería de Telecomunicación', 'title': '' }, 
    #{ 5107 : Graduado/a en Ingeniería de Sistemas de Telecomunicación', 'title': '' }, 
    #{ 5108 : Graduado/a en Ingeniería de Sistemas Electrónicos', 'title': '' }, 
    #{ 5109 : Graduado/a en Ingeniería de Sonido e Imagen', 'title': '' }, 
    #{ 5111 : Graduado/a en Ingeniería de Tecnologías de Telecomunicación', 'title': '' }, 
    #{ 5110 : Graduado/a en Ingeniería Telemática', 'title': '' }, 
#{ 308 : Escuela Técnica Superior de Ingeniería Industrial', 'title': '' }, 
    #{ 5158 : Graduado/a en Ingeniería de la Energía', 'title': '' }, 
    #{ 5155 : Graduado/a en Ingeniería de Organización Industrial', 'title': '' }, 
    #{ 5156 : Graduado/a en Ingeniería Electrónica, Robótica y Mecatrónica', 'title': '' }, 
    #{ 5061 : Graduado/a en Ingeniería en Tecnologías Industriales', 'title': '' }, 
#{ 313 : Facultad de Bellas Artes', 'title': '' }, 
    #{ 5101 : Graduado/a en Bellas Artes', 'title': '' }, 
#{ 303 : Facultad de Ciencias', 'title': '' }, 
    #{ 5002 : Graduado/a en Biología', 'title': '' }, 
    #{ 5164 : Graduado/a en Bioquímica', 'title': '' }, 
    #{ 5005 : Graduado/a en Ciencias Ambientales', 'title': '' }, 
    #{ 5106 : Graduado/a en Ingeniería Química', 'title': '' }, 
    #{ 5003 : Graduado/a en Matemáticas', 'title': '' }, 
    #{ 5004 : Graduado/a en Química', 'title': '' }, 
#{ 309 : Facultad de Ciencias de la Comunicación', 'title': '' }, 
    #{ 5024 : Graduado/a en Comunicación Audiovisual', 'title': '' }, 
    #{ 5023 : Graduado/a en Periodismo', 'title': '' }, 
    #{ 5022 : Graduado/a en Publicidad y Relaciones Públicas', 'title': '' }, 
#{ 310 : Facultad de Ciencias de la Educación', 'title': '' }, 
    #{ 5009 : Graduado/a en Educación Infantil', 'title': '' }, 
    #{ 5010 : Graduado/a en Educación Primaria', 'title': '' }, 
    #{ 5060 : Graduado/a en Educación Social', 'title': '' }, 
    #{ 5008 : Graduado/a en Pedagogía', 'title': '' }, 
#{ 405 : Facultad de Ciencias de la Salud', 'title': '' }, 
    #{ 5050 : Graduado/a en Enfermería', 'title': '' }, 
    #{ 5049 : Graduado/a en Fisioterapia', 'title': '' }, 
    #{ 5048 : Graduado/a en Podología', 'title': '' }, 
    #{ 5051 : Graduado/a en Terapia Ocupacional', 'title': '' }, 
#{ 301 : Facultad de Ciencias Económicas y Empresariales', 'title': '' }, 
    #{ 5006 : Graduado/a en Administración y Dirección de Empresas', 'title': '' }, 
    #{ 5165 : Graduado/a en Administración y Dirección de Empresas + Graduado/a en Derecho', 'title': '' }, 
    #{ 5007 : Graduado/a en Economía', 'title': '' }, 
    #{ 5206 : Graduado/a en Economía + Graduado/a en Administración y Dirección de Empresas', 'title': '' }, 
    #{ 5017 : Graduado/a en Finanzas y Contabilidad', 'title': '' }, 
#{ 401 : Facultad de Comercio y Gestión', 'title': '' }, 
    #{ 5105 : Graduado/a en Gestión y Administración Pública', 'title': '' }, 
    #{ 5018 : Graduado/a en Marketing e Investigación de Mercados', 'title': '' }, 
#{ 312 : Facultad de Estudios Sociales y del Trabajo', 'title': '' }, 
    #{ 5159 : Graduado/a en Estudios de Asia Oriental', 'title': '' }, 
    #{ 5026 : Graduado/a en Relaciones Laborales y Recursos Humanos', 'title': '' }, 
    #{ 5114 : Graduado/a en Trabajo Social', 'title': '' }, 
#{ 304 : Facultad de Filosofía y Letras', 'title': '' }, 
    #{ 5019 : Graduado/a en Estudios Ingleses', 'title': '' }, 
    #{ 5020 : Graduado/a en Filología Clásica', 'title': '' }, 
    #{ 5066 : Graduado/a en Filología Hispánica', 'title': '' }, 
    #{ 5013 : Graduado/a en Filosofía', 'title': '' }, 
    #{ 5012 : Graduado/a en Geografía y Gestión del Territorio', 'title': '' }, 
    #{ 5011 : Graduado/a en Historia', 'title': '' }, 
    #{ 5065 : Graduado/a en Historia del Arte', 'title': '' }, 
    #{ 5032 : Graduado/a en Traducción e Interpretación', 'title': '' }, 
#{ 302 : Facultad de Medicina', 'title': '' }, 
    #{ 5014 : Graduado/a en Medicina', 'title': '' }, 
#{ 311 : Facultad de Psicología', 'title': '' }, 
    #{ 5086 : Graduado/a en Logopedia', 'title': '' }, 
    #{ 5015 : Graduado/a en Psicología', 'title': '' }, 
#{ 406 : Facultad de Turismo', 'title': '' }, 
    #{ 5001 : Graduado/a en Turismo', 'title': '' }, 

def link(school_code, degree_code, year):
    """
    Returns the link to get school degree information
    """
    return 'https://oas.sci.uma.es:8443/pls/apex/f?p=101:1:117193384589344::NO::INICIO_LOV_TIPO_ESTUDIO,INICIO_LOV_CURSO_ACAD,INICIO_LOV_CENTROS,INICIO_LOV_TITULACIONES,INICIO_LOV_CICLOS,INICIO_LOV_CURSOS,INICIO_BUSCAR:3%2C{0}%2C{1}%2C{2}%2C1%2C-1%2C'.format(year, school_code, degree_code)

schools_data = {}
nschools = len(data_links)
print nschools,'Schools to get information'
for school_code, school_data in data_links.iteritems():
    degree_data = {}
    ndegrees = len(school_data['degrees'])
    print 'Fetching data for:', school_data['title_ES'], ndegrees, 'degrees'
    for idegree, degree in enumerate(school_data['degrees']):
        # fetching data for degrees
        degree_code, deg_data = degree.items()[0]
        page = requests.get(link(school_code, degree_code, '2013'))
        tree = BeautifulSoup(page.text)
        code_title = {}
        for trs in tree.find('table', {'class':
        't15standardalternatingrowcolors'}).findAll('tr')[1:-3]:
            code_title[trs.find('td').getText()] = {'title': trs.find('a').getText()}
        degree_data[deg_data['title']] = code_title
        print 'Data for:', deg_data['title_ES'], idegree + 1, 'of', ndegrees
    schools_data[school_data['title']] = degree_data
with open('./school_degrees_data.py', 'wt') as out:
    out.write('schools_data = ')
    pprint(schools_data, stream=out)
