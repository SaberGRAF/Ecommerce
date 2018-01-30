from django.http import Http404
from django.views.generic import ListView, DetailView

from products.models import Product


class ProductFeaturedListView(ListView):
    def get_queryset(self):
        return Product.objects.featured()


class ProductListView(ListView):
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Product does not exits')
        return instance


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        instance = Product.objects.get_by_slug(slug)
        if instance is None:
            raise Http404('Product does not exits')
        return instance
