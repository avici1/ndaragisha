import json

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *


# Create your views here.

def handle_lost_request(request):
    lost = LostItems()
    if request.method == "POST":
        doc_name = request.POST.get("doc_name")
        doc_id = request.POST.get("item_id")
        lost.owner_name = request.POST.get("names")
        lost.owner_phone = request.POST.get("phone")
        lost.found_desc = request.POST.get("desc")
        lost.doc_name = doc_name
        lost.real_doc_id = doc_id
        lost.desc = request.POST.get("desc")

        lost.save()
        return redirect('/auth/users/')
    else:
        return redirect('/auth/error/')


def handle_found_items(request):
    lost = LostItems.objects.get(real_doc_id=request.POST.get('id'))
    if request.method == "POST" and request.FILES['image']:
        doc_id = request.POST.get("id")
        lost.found_person_name = request.POST.get('name')
        lost.found_person_phone = request.POST.get('phone')
        lost.found_desc = request.POST.get('desc')
        lost.fake_doc_id = doc_id
        lost.status = "Found"
        item_name = request.FILES['image']
        fs = FileSystemStorage()
        file_name = fs.save(item_name.name, item_name)
        image_url = fs.url(file_name)
        lost.img_path = image_url
        lost.save()

        return redirect('/auth/users/')

    else:
        return redirect('auth/error/')


def get_all_items_lost(request):
    lost = LostItems.objects.filter(status="Not Found")
    data = json.dumps([{
        'image_path': lost1.img_path,
        'doc_name': lost1.doc_name,
        'doc_id': lost1.real_doc_id
    } for lost1 in lost])
    return HttpResponse(data)


def get_all_items_found(request):
    lost = LostItems.objects.filter(status="Found")
    data = json.dumps([{
        'img_path': lost1.img_path,
        'doc_id': lost1.real_doc_id,
        'doc_name': lost1.doc_name,
        'found_person_name': lost1.found_person_name,
        'found_person_phone': lost1.found_person_phone,
        'owner_name': lost1.owner_name,
        'owner_phone': lost1.owner_phone
    } for lost1 in lost])
    return HttpResponse(data)

def get_all_items(request):
    lost = LostItems.objects.all()
    data = json.dumps([{
        'img_path': lost1.img_path,
        'doc_id': lost1.real_doc_id,
        'doc_name': lost1.doc_name,
        'found_person_name': lost1.found_person_name,
        'found_person_phone': lost1.found_person_phone,
        'owner_name': lost1.owner_name,
        'owner_phone': lost1.owner_phone
    } for lost1 in lost])
    return HttpResponse(data)



def handle_found_items_model_forms(request):
    form = FoundItemsForms(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/home/')
    else:
        form = FoundItemsForms(request.POST, request.FILES)
        # form.save()
        return render(request, 'ndaragisha.html', {'form': form})


def handle_sent_messages(request):
    if request.method == "POST":
        message = IncomingMessage()
        message.email = request.POST.get('email')
        message.message = request.POST.get('message')
        message.subject = request.POST.get('subject')
        message.names = request.POST.get('names')
        message.save()
        return redirect('/home/')
    else:
        return redirect('/auth/error/')
