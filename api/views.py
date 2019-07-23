import json

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from .forms import *
from .models import *


# Create your views here.

def send_email(rec):
    email = EmailMessage("Ndarangisha","Murakoze gukoresha gahunda yacu yitwa Ndarangisha. La Fraternite Tech Ltd irabamenyesha ko ibyo mwarangishije byabonetse 0788902758",to=[rec])
    return email.send()

def handle_lost_request(request):
    lost = LostItems()
    try:
        qs = FoundButNotAssigned.objects.get(found_doc_id=request.POST.get("item_id"))
        qs.status = "Found"
        qs.owner_name = request.POST.get("names")
        qs.owner_phone = request.POST.get("phone")
        qs.owner_id = request.POST.get("natId")
        qs.owner_email = request.POST.get("email")
        qs.save()
        send_email(request.POST.get("email"))
        return redirect('/auth/users/')
    except ObjectDoesNotExist:
     if request.method == "POST":
        doc_name = request.POST.get("doc_name")
        doc_id = request.POST.get("item_id")
        lost.owner_name = request.POST.get("names")
        lost.owner_email = request.POST.get("email")
        lost.owner_id = request.POST.get("natId")
        lost.owner_phone = request.POST.get("phone")
        lost.found_desc = request.POST.get("desc")
        lost.owner_cell = request.POST.get("cell")
        lost.owner_umudugudu = request.POST.get("umudugudu")
        lost.owner_district = request.POST.get("district")
        lost.owner_sector = request.POST.get("sector")
        lost.doc_name = doc_name
        lost.real_doc_id = doc_id
        lost.desc = request.POST.get("desc")

        lost.save()
        return redirect('/auth/users/')
    else:
        return redirect('/auth/error/')


def handle_found_items(request):
    lost_1 = LostItems.objects.filter(fake_doc_id=request.POST.get('id'))
    if lost_1.exists():
        return render(request, '500.html', {"message": "Post exists already", "url": "http://127.0.0.1:8000"})
    else:

        if request.method == "POST" and request.FILES['image']:
            try:
                lost = LostItems.objects.get(
                    real_doc_id=request.POST.get("id"))
            except ObjectDoesNotExist:
                fd = FoundButNotAssigned()
                fd.found_person = request.POST.get('name')
                # fd.found_person_id = request.POST.get('natId')
                fd.found_doc_id = request.POST.get('id')
                fd.owner_id = request.POST.get('natId')
                fd.found_doc_type = request.POST.get('doc_name')
                fd.found_person_phone = request.POST.get("phone")
                doc_img = request.FILES['image']
                fs =FileSystemStorage()
                file_name = fs.save(doc_img.name,doc_img)
                doc_img_url = fs.url(file_name)
                fd.found_doc_img = doc_img_url 
                fd.save()
                return redirect('http://127.0.0.1:8000/auth/users/')

            doc_id = request.POST.get("id")
            send_email(lost.owner_email)
            lost.found_person_name = request.POST.get('name')
            lost.found_person_phone = request.POST.get('phone')
            lost.found_desc = request.POST.get('desc')
            lost.found_cell = request.POST.get("cell")
            lost.found_umudugudu = request.POST.get("umudugudu")
            lost.found_district = request.POST.get("district")
            lost.found_sector = request.POST.get("sector")
            lost.found_person_id = request.POST.get("natId")
            lost.fake_doc_id = doc_id
            lost.status = "Found"
            item_name = request.FILES['image']
            fs = FileSystemStorage()
            file_name = fs.save(item_name.name, item_name)
            image_url = fs.url(file_name)
            lost.img_path = image_url
            lost.save()
            return redirect ('/auth/users/')
        else:
            return render(request, '500.html', {'message': 'Post request forgery', 'url': 'http://127.0.0.1:8000'})


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
def load_found_not_assined(request):
    fd = FoundButNotAssigned.objects.filter(status='Not Found')
    data = json.dumps([{
        'found_person': fd_data.found_person,
        'found_person_id':fd_data.found_person_id,
        'found_doc_id':fd_data.found_doc_id,
        'found_doc_type':fd_data.found_doc_type,
      
        'found_person_phone':fd_data.found_person_phone,
        'found_doc_img':fd_data.found_doc_img
    } for fd_data in fd])
    return HttpResponse(data)

    # def handle_found_but_ass(request):
