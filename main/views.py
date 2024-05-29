from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SurveyResult, VoiceFile
from .forms import SurveyForm, VoiceFileForm
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        form = VoiceFileForm(request.POST, request.FILES)
        if form.is_valid():
            voice_file = VoiceFile(file=request.FILES['voiceFile'])
            voice_file.save()
            return redirect('index')
    else:
        form = VoiceFileForm()
    return render(request, 'main/index.html', {'form': form})

def checklist(request):
    return render(request, 'main/checklist.html')

def checklist_main(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            total_value = form.cleaned_data['total_value']
            result = SurveyResult.objects.create(total_value=total_value, recorded_at=timezone.now())
            return JsonResponse({'result': result.total_value, 'time': result.recorded_at.strftime('%Y-%m-%d %H:%M')})
    return render(request, 'main/checklist_main.html')