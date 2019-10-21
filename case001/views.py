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

def a1(request):
    
    list1 = Data1.objects.values('place').annotate(
        daycnt=Count('date1',distinct=True),headcnt=Count('worker',distinct=True),idcnt=Count('id'))
    
    print("DEBUG ... ")
    for x in list1:
        list2 = Data1.objects.filter(place=x['place'], date1__year=2019, date1__month=7).values('place').annotate(
            daycnt=Count('date1',distinct=True),headcnt=Count('worker',distinct=True),idcnt=Count('id'))
        
        #你會發現可能沒有，有的話也只有一筆
        # for x2 in list2:
        #     print('...',2019,7,x2)
        x['m1daycnt']=x['m1headcnt']=x['m1idcnt']=0
        if list2:
            x['m1daycnt']=list2[0]['daycnt']
            x['m1headcnt']=list2[0]['headcnt']
            x['m1idcnt']=list2[0]['idcnt']
            

        print(x)


    context = {'list': list1}
    return render(request, 'case001/a1.html', context)