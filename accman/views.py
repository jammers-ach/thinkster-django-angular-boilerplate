from django.shortcuts import render
from django.http import HttpResponse

from bankimporter.models import RealTransaction


# TODO login required
def view_all(request):
    transactions = RealTransaction.objects.all().order_by('-date')

    context = {
        'transactions': transactions
    }

    return render(request, 'accman/index.html', context)
