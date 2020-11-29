from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from guestbook.models import Guestbook
from .forms import GuestbookForm
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the guestbook index.")

def index(request):
    guestbook_index = Guestbook.objects.order_by('-created')
    paginator = Paginator((list(guestbook_index)), 10)
    
    page = request.GET.get('page')
    try:
        guestbook_index = paginator.page(page)
    except PageNotAnInteger:
        guestbook_index = paginator.page(1)
    except EmptyPage:
        guestbook_index = paginator.page(paginator.num_pages)
    
    # now return the rendered template
    template = loader.get_template('guestbook/index.html')
    context = RequestContext(request, {
        'guestbook_index': guestbook_index,
    })
    return HttpResponse(template.render(context.flatten()))
           
def detail(request, guestbook_id):
    guestbook = get_object_or_404(Guestbook, pk=guestbook_id)
    template = loader.get_template('guestbook/detail.html')
    context = RequestContext(request, {
        'guestbook': guestbook,
    })
    return HttpResponse(template.render(context.flatten()))


class GuestbookCreate(CreateView):
    model = Guestbook
    fields = ['nick', 'content']
    
    @csrf_exempt
    def form_valid(self, form):
        # @ToDo - enable csrf protection (fixed after upgrade to Django 3)
        return super(GuestbookCreate, self).form_valid(form)
