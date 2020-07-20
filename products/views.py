from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import featuredproducts,ringsdatabase,necklessdatabase,braceletsdatabase,earingsdatabase,jewellarydatabase,message,reviewdatabase
from itertools import chain
from operator import attrgetter
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

#ringcnt=ringsdatabase.objects.all().count()
neckcnt=int(necklessdatabase.objects.all().count())
braccnt=int(braceletsdatabase.objects.all().count())
earcnt=int(earingsdatabase.objects.all().count())
#jwecnt=jewellarydatabase.objects.all().count()
start99cnt = neckcnt+braccnt
start99cnt= start99cnt + earcnt
zip_list={
    'neckcnt':neckcnt,
    'braccnt':braccnt,
    'earcnt':earcnt,
    'start99cnt':start99cnt
        }



# Create your views here.

def rings(request):
    ringsobj=ringsdatabase.objects.all()
    page_obj=pagechanger(request,ringsobj,9)
    zip_list.update({'page_obj':page_obj,'function_name':'rings'})
    return render(request,'products/shop.html',zip_list)

def necklace(request):
    necklessobj=necklessdatabase.objects.all()
    page_obj=pagechanger(request,necklessobj,9)
    zip_list.update({'page_obj':page_obj,'function_name':'necklace'})
    return render(request,'products/shop.html',zip_list)

def bracelets(request):
    braceletsobj=braceletsdatabase.objects.all()
    page_obj=pagechanger(request,braceletsobj,9)
    zip_list.update({'page_obj':page_obj,'function_name':'bracelets'})
    return render(request,'products/shop.html',zip_list)

def earings(request):
    earingsobj=earingsdatabase.objects.all()
    page_obj=pagechanger(request,earingsobj,9)
    zip_list.update({'page_obj':page_obj,'function_name':'earings'})
    return render(request,'products/shop.html',zip_list)

def jewellary(request):
    jewellaryobj=jewellarydatabase.objects.all()
    page_obj=pagechanger(request,jewellaryobj,9)
    zip_list.update({'page_obj':page_obj,'function_name':'jewellery'})
    return render(request,'products/shop.html',zip_list)

def start99(request):
    obj=braceletsdatabase.objects.all()
    #obj=chain(obj,braceletsdatabase.objects.all())
    obj=chain(obj,earingsdatabase.objects.all())
    #obj=chain(obj,jewellarydatabase.objects.all())
    obj=chain(obj,necklessdatabase.objects.all())
    result_list=sorted(obj,key=attrgetter('price'))
    result=pagechanger(request,result_list,9)
    zip_list.update({'page_obj':result,'function_name':'start99'})
    return render(request,'products/shop.html',zip_list)

def newcollection(request):
    obj=(braceletsdatabase.objects.all().order_by('-time'))[:9]
    #obj=chain(obj,braceletsdatabase.objects.all())
    obj=chain(obj,(earingsdatabase.objects.all().order_by('time'))[:9])
    #obj=chain(obj,jewellarydatabase.objects.all())
    obj=list(chain(obj,(necklessdatabase.objects.all().order_by('time'))[:9]))
    #result_list=sorted(obj,key=attrgetter('time'))[::-1]
    #result_list=result_list[:27]
    random.shuffle(obj)
    result=pagechanger(request,obj,9)
    zip_list.update({'page_obj':result,'function_name':'newcollection'})
    return render(request,'products/shop.html',zip_list)

def pagechanger(request,obj,size):
    paginator = Paginator(obj,size)
    current_page = request.GET.get('page')

    try:
        result = paginator.page(current_page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        print(paginator.num_pages)
        result = paginator.page(paginator.num_pages)

    return result

def home(request):
    obj=(braceletsdatabase.objects.all().order_by('-time'))[:5]
    obj=chain(obj,(earingsdatabase.objects.all().order_by('-time'))[:5])
    obj=list(chain(obj,(necklessdatabase.objects.all().order_by('-time'))[:5]))
    #result_list=sorted(obj,key=attrgetter('time'),reverse=True)
    #newobj=result_list[:10]
    random.shuffle(obj)
    featuredobj=featuredproducts.objects.all()
    params ={
        'newobj':obj,
        'featuredobj':featuredobj,
        }
    return render(request,'products/index.html',params)

def about(request):
    return render(request,'products/about.html')

def contact(request):
    if request.method=='POST':
        msg=message()
        msg.name=request.POST['name']
        msg.email=request.POST['email']
        msg.phone=request.POST['phone']
        msg.message=request.POST['message']
        msg.save()
        messages.add_message(request, messages.INFO, 'Thank You ')
        return redirect('contact')
    return render(request,'products/contact-us.html')

def singleproduct(request,type,id):
    if type=='ring':
        obj=ringsdatabase.objects.get(id=int(id))
        related_obj=related_prod(ringsdatabase)
    elif type=='necklace':
        obj=necklessdatabase.objects.get(id=int(id))
        related_obj=related_prod(necklessdatabase)
    elif type=='bracelet':
        obj=braceletsdatabase.objects.get(id=int(id))
        related_obj=related_prod(braceletsdatabase)
    elif type=='earing':
        obj=earingsdatabase.objects.get(id=int(id))
        related_obj=related_prod(earingsdatabase)
    else:
        obj=jewellarydatabase.objects.get(id=int(id))
        related_obj=related_prod(jewellarydatabase)
    reviewobj=reviewdatabase.objects.filter(code=id).order_by('-star')
    #review_page=pagechanger(request,reviewobj,3)
    imgae_url="https://aashirwadjewellarycollection.pythonanywhere.com" + obj.image.url
    return render(request,'products/single-product.html',{'obj':obj,'related':related_obj,'reviewobj':reviewobj,'image_url':imgae_url})


def related_prod(database_type):
    related=set()
    for i in range(0,10):
        related.add(database_type.objects.order_by('?')[0])
    return related

def review(request):
    if request.method=='POST':
        obj=reviewdatabase()
        obj.name=request.POST['name']
        obj.review=request.POST['review']
        obj.star=request.POST['star']
        obj.code=request.POST['code']
        obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def sortby(request,type,option):
    if type=="rings":
        if option=='low-to-high':
            obj=ringsdatabase.objects.all().order_by('price')
        elif option=='high-to-low':
            obj=ringsdatabase.objects.all().order_by('price')[::-1]
        else:
            obj=ringsdatabase.objects.all().order_by('time')[::-1]
        page_obj=pagechanger(request,obj,9)
        zip_list.update({'page_obj':page_obj,'function_name':'rings'})
        return render(request,'products/shop.html',zip_list)

    elif type=="necklace":
        if option=='low-to-high':
            obj=necklessdatabase.objects.all().order_by('price')
        elif option=='high-to-low':
            obj=necklessdatabase.objects.all().order_by('price')[::-1]
        else:
            obj=necklessdatabase.objects.all().order_by('time')[::-1]
        page_obj=pagechanger(request,obj,9)
        zip_list.update({'page_obj':page_obj,'function_name':'necklace'})
        return render(request,'products/shop.html',zip_list)

    elif type=="bracelets":
        if option=='low-to-high':
            obj=braceletsdatabase.objects.all().order_by('price')
        elif option=='high-to-low':
            obj=braceletsdatabase.objects.all().order_by('price')[::-1]
        else:
            obj=braceletsdatabase.objects.all().order_by('time')[::-1]
        page_obj=pagechanger(request,obj,9)
        zip_list.update({'page_obj':page_obj,'function_name':'bracelets'})
        return render(request,'products/shop.html',zip_list)

    elif type=="earings":
        if option=='low-to-high':
            obj=earingsdatabase.objects.all().order_by('price')
        elif option=='high-to-low':
            obj=earingsdatabase.objects.all().order_by('price')[::-1]
        else:
            obj=earingsdatabase.objects.all().order_by('time')[::-1]
        page_obj=pagechanger(request,obj,9)
        zip_list.update({'page_obj':page_obj,'function_name':'earings'})
        return render(request,'products/shop.html',zip_list)

    elif type=="jewellary":
        if option=='low-to-high':
            obj=jewellarydatabase.objects.all().order_by('price')
        elif option=='high-to-low':
            obj=jewellarydatabase.objects.all().order_by('price')[::-1]
        else:
            obj=jewellarydatabase.objects.all().order_by('time')[::-1]
        page_obj=pagechanger(request,obj,9)
        zip_list.update({'page_obj':page_obj,'function_name':'jewellery'})
        return render(request,'products/shop.html',zip_list)

    elif type=="start99":
        res=braceletsdatabase.objects.all()
        #res=chain(res,braceletsdatabase.objects.all())
        res=chain(res,earingsdatabase.objects.all())
        #res=chain(res,jewellarydatabase.objects.all())
        res=chain(res,necklessdatabase.objects.all())
        if option=="low-to-high":
            obj=sorted(res,key=attrgetter('price'))
        elif option=="high-to-low":
            obj=sorted(res,key=attrgetter('price'))[::-1]
        else:
            obj=sorted(res,key=attrgetter('time'))[::-1]
        page_obj=pagechanger(request,obj,9)
        zip_list.update({'page_obj':page_obj,'function_name':'start99'})
        return render(request,'products/shop.html',zip_list)

    elif type=="newcollection":
        res=braceletsdatabase.objects.all()
        #res=chain(res,braceletsdatabase.objects.all())
        res=chain(res,earingsdatabase.objects.all())
        #res=chain(res,jewellarydatabase.objects.all())
        res=chain(res,necklessdatabase.objects.all())
        result_list=sorted(res,key=attrgetter('time'))[::-1]
        result_list=result_list[:27]
        if option=='low-to-high':
            obj=sorted(result_list,key=attrgetter('price'))
        elif option=='high-to-low':
            obj=sorted(result_list,key=attrgetter('price'))[::-1]
        else:
            obj=sorted(result_list,key=attrgetter('time'))[::-1]
        obj=obj[:27]
        page_obj=pagechanger(request,obj,9)
        zip_list.update({'page_obj':page_obj,'function_name':'newcollection'})
        return render(request,'products/shop.html',zip_list)

def not_found(request):
    return render(request,'products/404.html',status=404)



