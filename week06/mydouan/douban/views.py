from django.shortcuts import render
from .models import MovieBabai,T1
from django.db.models import Avg

def movie_short(request):
    # 三星级以上
    search_key = request.GET.get('search_input')
    condtions = {'stars__gt': 3}
    if search_key:
        condtions = {"shorts__contains": search_key}
    queryset = MovieBabai.objects.all()
    good_comment = queryset.filter(**condtions)
    return render(request, 'result01.html', locals())

def books_short(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = round(T1.objects.aggregate(Avg('n_star'))['n_star__avg'],1)
    # 情感倾向
    sent_avg = round(T1.objects.aggregate(Avg('sentiment'))['sentiment__avg'],2)

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result02.html', locals())

# Create your views here.
