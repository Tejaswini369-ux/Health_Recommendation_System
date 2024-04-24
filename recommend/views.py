from django.shortcuts import render

import json
import pandas as pd
import pickle

from .models import Doctor
from .data import spls
from .train import loaded_model, x_columns
# Create your views here.




def mainview(request):
    return render(request,'main.html')

def doctorview(request):
    if request.method == 'POST':
        doc = Doctor.objects.create(name = request.POST['Name'], specialisation = request.POST['specialisation'])
        doc.save()
    return render(request, 'doctor.html')

def patientview(request):
    if request.method == 'POST':
        symps = json.loads(request.POST['json_details'])
        # spl = pd.read_csv('recommend/files/Symptom_Weights.csv')
        symps = [item['label'] for item in symps]
        cols = list(spls.columns)
        x = {}
        for col in list(x_columns):
            if col in symps:
                x[col] = [1]
            else:
                x[col] = [0]
        x = pd.DataFrame(x)
        # loaded_model = pickle.load(open('Specalist.pkl', 'rb'))

        predictions = loaded_model.predict(x)
        print(predictions)
        print(Doctor.objects.all())
        doctors = Doctor.objects.filter(specialisation=predictions[0])

        return render(request, 'display.html', {'specialisation': predictions[0], 'doctors':doctors})
        
    return render(request, 'patient.html')

    