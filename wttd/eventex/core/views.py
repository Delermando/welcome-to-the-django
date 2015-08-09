# coding: utf-8
#from django.http import HttpResponse
#from django.template import loader, Context
from django.shortcuts import render_to_response
def homepage( request ):
	#t = loader.get_template( 'index.html' )
	#c = Context()
	#content = t.render( c )
	#return HttpResponse( content )
	return render_to_response('index.html')