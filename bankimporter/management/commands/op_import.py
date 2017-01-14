from django.core.management.base import BaseCommand, CommandError
from bankimporter.importer import import_op_csv
import logging

class Command(BaseCommand):
    help = 'imports transactions from OP banks data'

    def add_arguments(self, parser):
        parser.add_argument('opfile', nargs='+')

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO)
        for fname in options['opfile']:
            import_op_csv(fname)
