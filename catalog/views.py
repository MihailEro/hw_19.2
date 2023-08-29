from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse

from catalog.models import Product, Blog


class IndexView(TemplateView):
    template_name = 'catalog/index.html'


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def get_contact(self, request):
        if self.request.method == 'POST':
            self.name = request.Post.get('name')
            self.phone = request.POST.get('phone')
            self.message = request.POST.get('message')
            print(f'{self.name} ({self.phone}) {self.message}')
        return render(request, 'catalog/contacts.html, context')


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products.html'


class ProductsCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'price')
    success_url = reverse_lazy('catalog:products')


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductsUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'price')
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body')
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'catalog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body')
    success_url = reverse_lazy('catalog:blog')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')


