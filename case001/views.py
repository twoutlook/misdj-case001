from django.shortcuts import render
from django.db.models import Count, Sum, Max, Min

from .models import Data1


def index(request):
    list1 = Data1.objects.values('date1__year','date1__month').annotate(daycnt=Count('date1',distinct=True),headcnt=Count('worker',distinct=True),idcnt=Count('id'))
    context = {'list1': list1}
    return render(request, 'case001/index.html', context)

def a8(request):
    
    list1 = Data1.objects.values('place','date1__year','date1__month').annotate(daycnt=Count('date1',distinct=True),headcnt=Count('worker',distinct=True),idcnt=Count('id')).order_by('place','date1__year','date1__month')
    
    context = {'list': list1}
    return render(request, 'case001/a8.html', context)