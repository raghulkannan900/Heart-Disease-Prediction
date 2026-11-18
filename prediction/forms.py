
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# USER REGISTRATION FORM
class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-input",
            "placeholder": "Enter your email"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Choose a username"
            })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


# HEART DISEASE PREDICTION FORM
# Category codes below are for the standard Cleveland dataset.

class HeartPredictionForm(forms.Form):

    age = forms.IntegerField(
        label="Age",
        min_value=1,
        max_value=120
    )

    sex = forms.ChoiceField(
        label="Sex",
        choices=[
            ("1", "Male"),
            ("0", "Female"),
        ]
    )

    cp = forms.ChoiceField(
        label="Chest Pain Type",
        choices=[
            ("1", "Typical Angina"),
            ("2", "Atypical Angina"),
            ("3", "Non-Anginal Pain"),
            ("4", "Asymptomatic"),
        ]
    )

    trestbps = forms.IntegerField(
        label="Resting Blood Pressure",
        min_value=50,
        max_value=250
    )

    chol = forms.IntegerField(
        label="Serum Cholesterol",
        min_value=50,
        max_value=700
    )

    fbs = forms.ChoiceField(
        label="Fasting Blood Sugar",
        choices=[
            ("1", "Greater than 120 mg/dl"),
            ("0", "120 mg/dl or less"),
        ]
    )

    restecg = forms.ChoiceField(
        label="Resting ECG",
        choices=[
            ("0", "Normal"),
            ("1", "ST-T Wave Abnormality"),
            ("2", "Left Ventricular Hypertrophy"),
        ]
    )

    thalach = forms.IntegerField(
        label="Maximum Heart Rate Achieved",
        min_value=50,
        max_value=250
    )

    exang = forms.ChoiceField(
        label="Exercise Induced Angina",
        choices=[
            ("1", "Yes"),
            ("0", "No"),
        ]
    )

    oldpeak = forms.FloatField(
        label="ST Depression",
        min_value=0,
        max_value=10
    )

    slope = forms.ChoiceField(
        label="Slope of Peak Exercise ST Segment",
        choices=[
            ("1", "Upsloping"),
            ("2", "Flat"),
            ("3", "Downsloping"),
        ]
    )

    ca = forms.IntegerField(
        label="Number of Major Vessels",
        min_value=0,
        max_value=3
    )

    thal = forms.ChoiceField(
        label="Thalassemia",
        choices=[
            ("3", "Normal"),
            ("6", "Fixed Defect"),
            ("7", "Reversible Defect"),
        ]
    )
