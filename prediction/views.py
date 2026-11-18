
from pathlib import Path
import joblib
import pandas as pd

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from .forms import RegisterForm, HeartPredictionForm


# Load the trained machine learning model
MODEL_PATH = Path(__file__).resolve().parent / "heart_model.pkl"

model = None

if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)


def home(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True


@login_required
def dashboard(request):

    prediction_result = None
    probability = None

    if request.method == "POST":
        form = HeartPredictionForm(request.POST)

        if form.is_valid():

            if model is None:
                prediction_result = (
                    "Model file not found. Please train the model first."
                )
            else:
                try:
                    input_data = pd.DataFrame(
                        [form.cleaned_data],
                        columns=[
                            "age", "sex", "cp", "trestbps", "chol",
                            "fbs", "restecg", "thalach", "exang",
                            "oldpeak", "slope", "ca", "thal"
                        ]
                    )

                    # Convert form values to numeric
                    input_data = input_data.astype(float)

                    prediction = model.predict(input_data)[0]

                    if hasattr(model, "predict_proba"):
                        probability = round(
                            model.predict_proba(input_data)[0][1] * 100, 2
                        )

                    if prediction == 1:
                        prediction_result = "Higher estimated risk"
                    else:
                        prediction_result = "Lower estimated risk"

                except Exception as error:
                    prediction_result = f"Prediction error: {error}"

    else:
        form = HeartPredictionForm()

    return render(
        request,
        "dashboard.html",
        {
            "form": form,
            "prediction_result": prediction_result,
            "probability": probability,
        }
    )
