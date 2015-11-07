from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def portal_main_page(request):
	#if users authernticated, direct to main page, else to login

	return render_to_response('portal/index.html')