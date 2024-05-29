from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def checklist(request):
    return render(request, 'main/checklist.html')

def checklist_main(request):
    return render(request, 'main/checklist_main.html')