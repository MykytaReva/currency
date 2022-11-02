from django.core.management.base import BaseCommand
from currency.parse_archive import parse_archive_privatbank


class Command(BaseCommand):

    def handle(self, *args, **options):
        parse_archive_privatbank()
