from datetime import date
from gallery.models import Album


def allAlbum(request):
    a = Album.objects.all()
    return {'albums': a}
