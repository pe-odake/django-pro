from django.shortcuts import render
from .forms import AddForm, EditForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect


def show(request):
    
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html',{'contacts': contact_list})

def detail(request, contato_id):
    
    contact_list = Contact.objects.filter(id=contato_id)
    return render(request, 'mycontacts/detail.html',{'details': contact_list})

def delete(request, contato_id):
    contato_delete = Contact.objects.filter(id=contato_id)
    contato_delete.delete()
    return redirect(show)
    
def edit(request, contato_id):
    contact = get_object_or_404(Contact, id=contato_id)

    if request.method == "POST":
        contact.name = request.POST.get("name")
        contact.relation = request.POST.get("relation")
        contact.phone = request.POST.get("phone")
        contact.email = request.POST.get("email")
        contact.save()
        return redirect(show) 

    return render(request, "mycontacts/edit.html", {"contact": contact})

        
def add(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_relation = django_form.data.get("relation")
            new_member_phone = django_form.data.get('phone')
            new_member_email = django_form.data.get('email')
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.create(
                name =  new_member_name, 
                relation = new_member_relation,
                phone = new_member_phone,
                email = new_member_email, 
                )
                 
            contact_list = Contact.objects.all()
            return render(request, 'mycontacts/show.html',{'contacts': contact_list})    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return redirect(show) 
    else:
        return render(request, 'mycontacts/add.html')

    