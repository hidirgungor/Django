from django.shortcuts import render
from .models import Kazananlar
from .forms import TcAramaForm

def kazananlar(request):
    if request.method == 'POST':
        form = TcAramaForm(request.POST)
        if form.is_valid():
            tc_num = form.cleaned_data['tc_num']
            try:
                kazanan = Kazananlar.objects.get(tc_num=tc_num)
                kazandi = kazanan.kazandi
                return render(request, 'kazananlar.html', {'kazandi': kazandi})
            except Kazananlar.DoesNotExist
