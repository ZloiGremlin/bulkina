from django.views.generic import TemplateView, DetailView
from gallery.models import Album


class FrontView(TemplateView):
    template_name = 'front.html'

    def get_context_data(self, **kwargs):
        ctx = super(FrontView, self).get_context_data(**kwargs)
        ctx['album'] = Album.objects.filter(main=True)[0]
        return ctx

class AlbumView(DetailView):
    model = Album
    slug_field = 'url'
    slug_url_kwarg = 'slug'
    template_name = 'front.html'

