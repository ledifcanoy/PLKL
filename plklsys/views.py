from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from .models import *
from .forms import cusinfo


def mainpage(request):
	if request.method == "POST":
		cphile_name=request.POST['name']
		cphile_email=request.POST['email']
		cphile_title=request.POST['film']
		cphile_director=request.POST['director']
		cphile_genre=request.POST['genre']
		FilmRequest.objects.create(cphile_name = cphile_name, 
		cphile_email=cphile_email, 
		cphile_title = cphile_title,
		cphile_director = cphile_director,
		cphile_genre = cphile_genre)
	return render(request, 'mainpage.html')

def branch(request):
	return render(request, 'model1_branch.html',)

def show(request):
	if request.method == "POST":
		country=request.POST['country']
		city=request.POST['city']
		cinema=request.POST['cinema']
		gate=request.POST['gate']
		Branch.objects.create(itemcountry = country, itemcity = city, itemcinema = cinema, itemgate = gate)
	return render(request, 'model3_show.html',)

def information(request):
	if request.method == "POST":
		movie=request.POST['movie']
		date=request.POST['date']
		time=request.POST['time']
		tickets=request.POST['tickets']
		dateres=request.POST['dateres']
		timeres=request.POST['timeres']
		Show.objects.create(itemmovie=movie, itemdate= date, itemtime = time, itemtickets = tickets, itemdateres = dateres, itemtimeres=timeres)
	return render(request, 'model5_ci.html',)


def table(request):
	if request.method == "POST":
		name=request.POST['name']
		email=request.POST['email']
		mobile=request.POST['mobile']
		payment=request.POST['payment']
		wallet=request.POST['wallet']
		CustomerInformation.objects.create(itemname = name, itememail = email, itemmobile = mobile, itempayment=payment, itemwallet=wallet)
	b = Branch.objects.all()
	s = Show.objects.all()
	c = CustomerInformation.objects.all()
	return render(request, 'table.html', {'Branch':b,'Show':s,'CustomerInformation':c})

def update(request, id):
	info = CustomerInformation.objects.get(id=id)
	form = cusinfo(instance=info)
	if request.method == 'POST':
		form = cusinfo(request.POST, instance = info)
		if form.is_valid():
			form.save()
			return redirect('/table')
	return render(request, 'update.html', {'form':form})
		
def cancel(request, id):
    ifn = CustomerInformation.objects.get(id=id)
    for x in CustomerInformation.objects.only('id'):
        if ifn == x:
            x = CustomerInformation.objects.get(id=id).delete()
            break
    return redirect('/table')

def cancel1(request, id):
    ifn = Branch.objects.get(id=id)
    for x in Branch.objects.only('id'):
        if ifn == x:
            x = Branch.objects.get(id=id).delete()
            break
    return redirect('/table')
def cancel2(request, id):
    ifn = Show.objects.get(id=id)
    for x in Show.objects.only('id'):
        if ifn == x:
            x = Show.objects.get(id=id).delete()
            break
    return redirect('/table')