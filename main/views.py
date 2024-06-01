from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SurveyResult, VoiceFile, HealthRecord
from .forms import SurveyForm, VoiceFileForm
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt

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
        total_value = request.POST.get('total_value')
        result = SurveyResult.objects.create(total_value=total_value, recorded_at=timezone.now())
        return JsonResponse({'result': result.total_value, 'time': result.recorded_at.strftime('%Y-%m-%d %H:%M')})
    return render(request, 'main/checklist_main.html')

def get_records(request):
    records = SurveyResult.objects.all().order_by('-recorded_at')
    data = [{'date': record.recorded_at.strftime('%Y.%m.%d'), 'total_value': record.total_value} for record in records]
    return JsonResponse({'records': data})

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sex = data.get('sex')
            age = data.get('age')
            weight = data.get('weight')
            height = data.get('height')

            record = HealthRecord(sex=sex, age=age, weight=weight, height=height)
            record.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
