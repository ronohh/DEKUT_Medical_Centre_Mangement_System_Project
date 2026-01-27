from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # admin panel
    path('adminhome/', views.adminhome, name='admindashboard'),
    path('base/', views.base, name='base'),
    path('Admin/doctorlist/', views.doctorList, name='viewdoctorlist'),
    path('Admin/pharmacistlist/', views.pharmacistList, name='viewpharmacistlist'),
    path('ViewDoctorDetails/<str:id>', views.ViewDoctorDetails, name='viewdoctordetails'),
    path('Admin/ViewDoctorPatient/<str:id>', views.ViewDoctorPatient, name='viewdoctorpatient'),
    path('Admin/registeredusers/', views.Registeredusers, name='registeredusers'),
    path('Admin/staffmembers/', views.StaffMembersList, name='staffmemberslist'),
    path('Admin/studentslist/', views.StudentsList, name='studentslist'),
    path('Admin/DoctorAppointmentList/<str:id>',views.ViewDoctorAppointmentList, name='ViewDoctorAppointmentList'),
    path('AdminAppointmentPatientDetails/<str:id>', views.ViewAppointmentPatientsDetails, name='viewappointmentpatientsdetails'),
    path('RegisteredUserAppointment/<str:id>', views.Registered_User_Appointments, name='registeredusersappointments'),
    path('DeleteRegusers/<str:id>', views.DeleteRegUsers, name='deleteuser'),
    path('Admin/insuranceList/', views.InsuranceList, name="insurancelist"),
    path('Admin/insurance/add', views.InsuranceAdd, name="insuranceadd"),
    path('Admin/insurance/Edit/<str:id>', views.InsuranceEdit, name='editinsurance'),
    path('Admin/insurance/delete/<str:id>', views.InsuranceDelete, name='insurancedelete'),
    path('Admin/dependants/<str:id>/', views.admindependants, name='admindependants'),
    path('Admin/review_claims/', views.review_claims, name='review_claims'),
    path('Admin/claim/<str:id>/<str:decision>/', views.update_claim_status, name='update_claim_status'),
    path('Admin/referral_requests/', views.referral_requests, name='referral_requests'),
    path('Admin/referral/forward/<str:id>/', views.forward_referral, name='forward_referral'),
    


    path('login/', views.login_view, name='login'),
    path('logout', views.dologout, name='dologout'),
    path('dologin/', views.dologin, name='dologin'),
    path('profile', views.Profile, name='profile'),
    path('profile/update', views.ProfileUpdate, name='profileupdate'),

    # user panel
    path('userbase/', views.Userbase, name='userbase'),
    path('', views.index, name='index'),
    path('patientregistration/', views.patientregistration, name="patientregistration"),
    path('patienthome/', views.patienthome, name='patienthome'),
    path( 'patientappointment/', views.create_appointment, name='patientappointment'),
    path('get_doctor/', views.get_doctor, name='get_doctor'),
    path('payment_status/', views.payment_status, name='payment_status'),
    path('viewAppointmentHistory/', views.view_appointment_history, name='viewappointmenthistory'),
    path('cancelappointment/<str:id>', views.cancel_appointment, name='cancelappointment'),
    path('AppointmentHistoryDetails/', views.appointment_history_details, name='viewappointmenthistorydetails'),
    path('records/<str:id>/', views.records, name='records'),
    path('fetch_regnumber/', views.get_regno, name='fetch_regnumber'),
    path("patient/change-type/", views.patient_change_type, name="patient_change_type"),

    # staff panel
    path('staffregistration/', views.staffregistration, name='staffregistration'),
    path('staffhome/', views.staffhome, name='staffdashboard'),
    path('staff/dependantslist/', views.dependantslist, name='dependantslist'),
    path('adddependants/', views.AddDependants, name='adddependants'),
    path('staff/Referrals/', views.Requestreferral, name='referrals'),
    path('staff/referral_history/', views.referral_history, name='referral_history'),
    path('staff/referralrecord/', views.staff_referral_record, name='staff_referral_record'),
    path('staff/medicalclaim/', views.medical_claim , name='medicalclaim'),
    path('staff/medicalclaimhistory', views.medicalclaim_history, name='medicalclaimhistory'),
    path('fetch-staff/', views.get_staff_id, name='fetch_staff'),

    # pharmacist panel
    path('pharmacistsignup/', views.pharmacistsignup, name='pharmacistsignup'),
    path('pharmacistdashboard/', views.pharmacistdashboard, name='pharmacistdashboard'),
    path('pharmacist/newappointments/', views.newappointments, name='newpharmacistappointments'),
    path('pharmacist/newpatients/', views.newpatients, name='newpharmacistpatients'),
    path('pharmacy/records/', views.pharmacy_records, name='pharmacy_records'),
    path('patientrecords/', views.patient_records, name='patient_records'),
    path('prescribedpatients/<str:id>', views.prescribed_patients, name='prescribed_patients'),
    path('notprescribedpatients/<str:id>', views.not_prescribed_patients, name='not_prescribed_patients'),
    path('dispense/<str:id>/', views.mark_as_dispensed, name='mark_as_dispensed'),
    path('notprescribed/<str:id>/', views.mark_as_not_prescribed, name='mark_as_not_prescribed'),

    # doctor panel
    path('docsignup/', views.docsignup, name='docsignup'),
    path('doctorhome/', views.doctorhome, name='doctordashboard'),
    path('doctor/AddPatient', views.Add_Patient, name='addpatient'),
    path('doctor/ManagePatient/', views.Manage_Patient, name='managepatient'),
    path('doctor/ViewPatient/<str:id>', views.view_patient, name='viewpatient'),
    path('doctor/EditPatient', views.edit_patient, name='editpatient'),
    path('doctor/ViewPatientDetails/<str:id>', views.ViewPatientDetails, name='viewpatientdetails'),
    path('doctor/UpdatePatientMedicalRecord', views.update_patient_medical_record, name='updatepatientmedicalrecord'),
    path('doctor/ViewAppointmentDetails/<str:id>', views.View_Appointment_Details, name="viewappointmentdetails"),
    path('appointmentDetailsRemark/Update', views.Patient_Appointment_Details_Remark, name='PatientAppointmentDetailsRemark'),
    path('doctor/ApprovedAppointment', views.Approved_Appointments, name='approvedappointments'),
    path('doctor/CancelledAppointments', views.Cancelled_Appointments, name="cancelledappointments"), 
    path('doctor/NewAppointments/', views.New_Appointments, name="newappointments"),
    path('doctor/referralList/', views.doctor_referral_list, name='doctor_referrals'),
    path('doctor/referralRecord/', views.doctor_referral_record, name='doctor_referral_record'),
    path('Admin/Allappointment/', views.All_appointment, name="allappointment"),
    path('claim_insurance/<str:id>/', views.claim_insurance, name='claim_insurance'),
    path('dependants/<str:id>/', views.Dependants, name='dependants'),
    path('get_doctor_dates/', views.get_doctor_dates),
    path('doctor/add_availability/', views.add_availability, name='add_availability'),
    path('get_available_times/', views.get_available_times),
    path('doctor/searchpatientmedicalhistory/', views.search_history, name='searchpatienthistory'),
    path('doctor/medicalclaims', views.medicalclaims, name='medicalclaims'),
    path('doctor/medicalclaim/approve/<str:id>', views.doctor_approve_claim, name='approvedmedicalclaim'),
    path('doctor/medicalclaim/decline/<str:id>', views.doctor_decline_claim, name='doctordeclinedclaim'),
    path('doctor/studentreferral/', views.studentreferral, name='studentreferral'),
    
    # daraja
    path("mpesa/stkpush/", views.stk_push, name="stk_push"),
    path("mpesa/form/", views.stk_form, name="stk_form"),
    path("mpesa/callback/", views.mpesa_callback, name="mpesa_callback"),

    # Hospital
    path('signuphospital/', views.signuphospital, name='signuphospital'),
    path('hospital/', views.DependantsReferral, name='dependantsReferral'),
    path('hospital/studentsreferral', views.Studentreferrall, name='studentreferrall'),
    path('hospital/treatedreferrals/', views.TreatedReferrals, name='treatedreferrals'),
    path('hospital/referral/details/<str:id>/', views.ReferralDetails, name='referraldetails'),
    path('hospital/referral/remarks/', views.ReferralRemarks, name='referralappointmentremarks'),
    path('hospital/fileclaim/<str:id>/', views.file_claim, name='fileclaim'),

    # others
    path('HR/registration', views.HRsignup, name='hrregistration'),
    path('HR/medicalclaim', views.HRmedicalclaim, name='hrmedicalclaim'),
    path('HR/medicalclaim/approve/<str:id>', views.HR_approveclaim, name='hrapprovedclaim'),
    path('HR/medicalclaim/decline/<str:id>', views.HR_decline_claim, name='hrdeclineclaim'),
    path('DVC/registration', views.DVCsignup, name='dvcsignup'),
    path('DVC/medicalclaim/', views.DVCmedicalclaim, name='dvcmedicalclaim'),
    path('DVC/medicalclaim/approve/<str:id>', views.DVC_approveclaim, name='DVCapprovedclaim'),
    path('DVC/medicalclaim/decline/<str:id>', views.DVC_decline_claim, name='DVCdeclineclaim'),
    path('Finance/registration', views.Financesignup, name='financesignup'),
    path('Finance/medicalclaim/', views.financemedicalclaim, name='financemedicalclaim'),
    path('finance/medicalclaim/approve/<str:id>', views.finance_approveclaim, name='financeapprovedclaim'),
    path('finance/medicalclaim/decline/<str:id>', views.finance_decline_claim, name='financedeclineclaim'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)