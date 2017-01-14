from .models import RealTransaction, RawTransaction, Tag, TagLookup
import logging

logger = logging.getLogger(__name__)


def base_importer(raw_transaction):
    # Check that there's no real transaction

    if RealTransaction.objects.filter(raw_transaction=raw_transaction).exists():
        logger.info("Transaction exists for #%04d", raw_transaction.id)
        return

    d = RealTransaction(raw_transaction=raw_transaction,
                        date=raw_transaction.value_date,
                        value=raw_transaction.value)


    d = apply_payment_type(raw_transaction, d)
    d = apply_main_tag(raw_transaction, d)

    d.save()

    apply_tags(raw_transaction, d)

    return d


def apply_payment_type(raw_transaction, real_transaction):
    real_transaction.payment_type = 'unkown'
    return real_transaction

def apply_main_tag(raw_transaction, real_transaction):

    # first look for a main tag based on the payer name
    if TagLookup.objects.filter(name=raw_transaction.payer).exists():
        tag = TagLookup.objects.get(name=raw_transaction.payer).tag
    elif real_transaction.value < 0:
        tag, _ =  Tag.objects.get_or_create(name='other')
    else:
        tag, _ =  Tag.objects.get_or_create(name='other credit')

    real_transaction.main_tag = tag

    return real_transaction

def apply_tags(raw_transaction, real_transaction):
    pass
