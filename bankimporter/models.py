from django.db import models

# Create your models here.
class RawTransaction(models.Model):
    entry_date = models.DateField()
    value_date = models.DateField()
    value = models.DecimalField(max_digits=6, decimal_places=2)
    kind = models.IntegerField()
    explanation = models.CharField(max_length=20)
    payer = models.CharField(max_length=20, blank=True, null=True)
    acc_no = models.CharField(max_length=20, blank=True, null=True)
    reference = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    filling_code = models.CharField(max_length=30)

    def __str__(self):
        if self.id:
            return '#{:04d}: {:%Y-%m-%d}  , {}  , {}'.format(self.id, self.value_date, self.value, self.payer)
        else:
            return '#    : {:%Y-%m-%d}  , {}  , {}'.format(self.id, self.value_date, self.value, self.payer)


class Tag(models.Model):
    name = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.name


class RealTransaction(models.Model):
    raw_transaction = models.ForeignKey('RawTransaction', blank=True, null=True)
    date = models.DateField(default='2016-01-01')
    value = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    payment_type = models.CharField(max_length=20, default='card')
    tags = models.ManyToManyField(Tag)
    main_tag = models.ForeignKey(Tag, related_name='main_tag', blank=True, null=True)


    def __str__(self):
        if self.id:
            return '#{:04d}: {:%Y-%m-%d} , {} , {}'.format(self.id, self.date, self.value, self.main_tag)
        else:
            return '#    : {:%Y-%m-%d}  , {} , {}'.format(self.date, self.value, self.main_tag)


class TagLookup(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    tag = models.ForeignKey(Tag)

    def __str__(self):
        return "{} , {}".format(self.name, self.tag)
