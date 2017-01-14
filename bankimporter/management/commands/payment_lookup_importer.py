from django.core.management.base import BaseCommand, CommandError
from bankimporter.models import Tag, TagLookup
import logging
import csv


class Command(BaseCommand):
    help = 'imports payment lookups'

    def add_arguments(self, parser):
        parser.add_argument('lookupfile')

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO)
        with open(options['lookupfile']) as f:
            reader = csv.reader(f, delimiter='\t')
            for who, tag_name in reader:
                tag, _ = Tag.objects.get_or_create(name=tag_name)

                if not(TagLookup.objects.filter(name=who)):
                    t = TagLookup(name=who, tag=tag)
                    t.save()
                    logger.info("Make lookup between %s and %s", who, tag_name)
