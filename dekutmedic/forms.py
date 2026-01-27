from django import forms
from .models import ReferralAppointment

class PatientReferralForm(forms.ModelForm):
    class Meta:
        model = ReferralAppointment
        fields = ["hospital_id", "doctor_id", "date_of_referral", "time_of_referral", "additional_msg"]

        labels = {
            "hospital_id": "Hospital name",
            "doctor_id": "Doctor",
            "date_of_referral": "Date of Referral",
            "time_of_referral": "Time of Referral",
            "additional_msg": "Additional Message",
        }


        widgets = {
            "hospital_id": forms.Select(attrs={"class": "form-control", "id":"hospital_id","placeholder":"Select Hospital"}),
            "doctor_id": forms.Select(attrs={"class": "form-control", "id":"doctor_id"}),
            "date_of_referral": forms.DateInput(attrs={"class": "form-control", "type":"date"}),
            "time_of_referral": forms.TimeInput(attrs={"class": "form-control","type":"time"}),
            "additional_msg": forms.Textarea(attrs={"class": "form-control","rows":3}),

        }