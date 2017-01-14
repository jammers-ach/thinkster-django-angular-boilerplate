from .models import RawTransaction
from .tagger import base_importer
import datetime as dt
import csv

import logging
logger = logging.getLogger(__name__)

def parse_decimal(fake_decimal):
    """turns '-15,61' to '-15.61'"""
    return fake_decimal.replace(',', '.').replace('-','-')

def import_op_csv(fpath):
    fmt = '%d.%m.%Y'
    with open(fpath, encoding='ISO-8859-1') as f:
        reader = csv.reader(f, delimiter=';')
        logger.info("Loading %s", fpath)

        next(reader) # Skip first line, it has headers

        for line in reader:
            if len(line) == 10:
                t, created = RawTransaction.objects.get_or_create(
                    entry_date=dt.datetime.strptime(line[0], fmt),
                    value_date=dt.datetime.strptime(line[1], fmt),
                    value=parse_decimal(line[2]),
                    kind=line[3],
                    explanation=line[4],
                    payer=line[5],
                    acc_no=line[6],
                    reference=line[7],
                    message=line[8],
                    filling_code=line[9],
                )


                if created:
                    logger.info("Created: %s ", t)
                else:
                    logger.info(" Exists: %s", t)

                base_importer(t)
            else:
                logger.info("Ignoring: '%s'",';'.join(line))


