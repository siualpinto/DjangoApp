from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from djangoApp.forms import UserForm
from django.views import View
from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.models import User
from django.utils import timezone


class IndexView(View):

    template = "index.html"

    def get(self, request):

        return render(request, self.template)


class UserListView(ListView):
    model = User
    template_name = 'list.html'
    context_object_name = 'users'
    paginate_by = 5
    queryset = User.objects.all()


class UserCreateView(CreateView):
    template_name = "create.html"
    form_class = UserForm
    model = User

    def get(self, request, *args, **kwargs):
        super(UserCreateView, self).get(request, *args, **kwargs)
        form = self.form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.first_name + ' ' + user.last_name
            user.save()
            return HttpResponseRedirect('/')
        else:
            return self.render_to_response(self.get_context_data(form=form))


