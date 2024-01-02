from django.http import HttpResponse
from django.shortcuts import render
from .forms import PredictionForm
import pandas as pd
import joblib


# Create your views here.
def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            age = request.POST.get('age')
            income = request.POST.get('income')
            gender = request.POST.get('gender')
            m_status = request.POST.get('m_status')

            print(age,income,gender,m_status)


            df = pd.DataFrame({'age': [age], 'income': [income], 'gender': [gender], 'm_status': [m_status]})
            print(df)
            model = joblib.load('model_prediction/dt_model.pkl')
            predicted_value = model.predict(df)
            print(predicted_value)

            if predicted_value[0]=='yes':
                return HttpResponse('Buy')
            else:
                return HttpResponse('Not Buy')
    else:
        form = PredictionForm()
    return render(request, "predict.html", {"form": form})
