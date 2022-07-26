from currency.models import Rate, ContactUs, Source
from django.shortcuts import render
from currency.forms import RateForm, ContactUsForm, SourceForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'currency/index.html')


def rate_list(request):
    context = {
        'rate_list': Rate.objects.all(),
    }

    return render(request, 'currency/rate_list.html', context=context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()
    context = {
        'form': form,
    }
    return render(request, 'currency/rate_create.html', context=context)


def rate_update(request, rate_id):

    rate_instance = get_object_or_404(Rate, id=rate_id)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate_instance)
    context = {
        'form': form,
    }
    return render(request, 'currency/rate_update.html', context=context)


def rate_delete(request, rate_id):
    rate_instance = get_object_or_404(Rate, id=rate_id)

    context = {'instance': rate_instance}
    if request.method == 'POST':
        rate_instance.delete()
        return HttpResponseRedirect('/rate/list/')
    return render(request, 'currency/rate_delete.html', context=context)


def rate_details(request, rate_id):
    rate_instance = get_object_or_404(Rate, id=rate_id)

    context = {'instance': rate_instance}
    return render(request, 'currency/rate_details.html', context=context)


def contact_us(request):
    context = {
        'contactus_list': ContactUs.objects.all(),
    }

    return render(request, 'currency/contactus.html', context=context)


def contactus_create(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/us/')
    elif request.method == 'GET':
        form = ContactUsForm()
    context = {
        'form': form,
    }
    return render(request, 'currency/contactus_create.html', context=context)


def contactus_update(request, contactus_id):

    contactus_instance = get_object_or_404(ContactUs, id=contactus_id)

    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contactus_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/us/')
    elif request.method == 'GET':
        form = ContactUsForm(instance=contactus_instance)
    context = {
        'form': form,
    }
    return render(request, 'currency/contactus_update.html', context=context)


def contactus_delete(request, contactus_id):
    contactus_instance = get_object_or_404(ContactUs, id=contactus_id)

    context = {'instance': contactus_instance}
    if request.method == 'POST':
        contactus_instance.delete()
        return HttpResponseRedirect('/contact/us/')
    return render(request, 'currency/contactus_delete.html', context=context)


def contactus_details(request, contactus_id):
    contactus_instance = get_object_or_404(ContactUs, id=contactus_id)

    context = {'instance': contactus_instance}
    return render(request, 'currency/contactus_details.html', context=context)


def source_list(request):
    context = {
        'source_list': Source.objects.all(),
    }
    return render(request, 'currency/source_list.html', context=context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm()
    context = {
        'form': form,
    }
    return render(request, 'currency/source_create.html', context=context)


def source_update(request, source_id):

    source_instance = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm(instance=source_instance)
    context = {
        'form': form
    }
    return render(request, 'currency/source_update.html', context=context)


def source_delete(request, source_id):

    source_instance = get_object_or_404(Source, id=source_id)

    context = {'instance': source_instance}
    if request.method == 'POST':
        source_instance.delete()
        return HttpResponseRedirect('/source/list/')
    return render(request, 'currency/source_delete.html', context=context)


def source_details(request, source_id):
    source_instance = get_object_or_404(Source, id=source_id)

    context = {'instance': source_instance}
    return render(request, 'currency/source_details.html', context=context)
