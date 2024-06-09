from django.core.management.base import BaseCommand
from django.utils import timezone
from ._populate_books_utils import populate_db_with_books

class Command(BaseCommand):
    help = 'Populate dummy books data in database'

    def handle(self, *args, **kwargs):
        populate_db_with_books()
        time = timezone.now().strftime('%X')
        self.stdout.write("Populated books in database at %s" % time)