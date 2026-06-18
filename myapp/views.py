import datetime
import smtplib
from email.mime.text import MIMEText
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *

from myapp.Prediction import predictfn


def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script> alert('Successfully Logged Out');window.location='/';</script>''')


def login2(request):
    return render(request, 'index.html')


def login_post(request):
    name = request.POST['textfield']
    passw = request.POST['textfield2']
    ob= login_table.objects.filter(user_name=name, password=passw)
    if ob.exists():
        user = login_table.objects.get(user_name=name, password=passw)
        request.session['lid'] = user.id
        if user.type == 'admin':
            # ob1=auth.authenticate(username="admin",password="admin")
            # if ob is not None:
            #     auth.login(request,ob1)
            return HttpResponse('''<script> alert('Admin Logged');window.location='/AdminHome';</script>''')
        elif user.type == 'doctor':
            # ob1 = auth.authenticate(username="admin", password="admin")
            # if ob is not None:
            #     auth.login(request, ob1)
            obx=doctor_table.objects.filter(LOGIN=user.id)
            if len(obx)>0:
                return HttpResponse('''<script> alert('Doctor Logged');window.location='/DoctorHome';</script>''')
            else:
                return HttpResponse('''<script> alert('invalid ');window.location='/';</script>''')


        elif user.type == 'user':
            return HttpResponse('''<script> alert('User Logged');window.location='/UserHome';</script>''')
        else:
            return HttpResponse('''<script> alert('Invalid Username or password');window.location='/';</script>''')
    else:
        return HttpResponse('''<script> alert('Invalid user ');window.location='/';</script>''')






# @login_required(login_url='/')
def AdminHome(request):
    if request.session['lid']=='':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')

    # return render(request, 'Admin/AdminHome.html')
    return render(request, 'Admin/Adminindex.html')
# @login_required(login_url='/')
def ApproveDoctor(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')

    doc = doctor_table.objects.all()
    return render(request, 'Admin/ApproveDoctor.html', {'doc': doc})

# @login_required(login_url='/')
def searchApproveDoctor(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    name = request.POST["textfield"]
    doc = doctor_table.objects.filter(name__icontains=name)
    # ob = feedback_table.objects.filter(DOCTOR=name)
    return render(request, 'Admin/ApproveDoctor.html', { "doc": doc})

# @login_required(login_url='/')
def accept_doc(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    obj = login_table.objects.get(id=id)
    obj.type = 'doctor'
    obj.save()
    return HttpResponse('''<script> alert(' accepted');window.location='/ApproveDoctor';</script>''')

# @login_required(login_url='/')

def reject_doc(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    obj = login_table.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script> alert(' rejected');window.location='/ApproveDoctor';</script>''')

# @login_required(login_url='/')
def ManageSchedule(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    return render(request, 'Admin/ManageSchedule.html')

# @login_required(login_url='/')
def SendReply(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    request.session['did'] = id
    return render(request, 'Admin/SendReply.html')

# @login_required(login_url='/')
def sendreply_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    reply = request.POST['textfield']
    ob = complaint_table.objects.get(id=request.session['did'])
    ob.reply = reply
    ob.save()
    return HttpResponse('''<script> alert(' successful');window.location='/ViewComplaint';</script>''')

# @login_required(login_url='/')
def ViewComplaint(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    ob = doctor_table.objects.filter(LOGIN__type="doctor")
    a = complaint_table.objects.all()
    return render(request, 'Admin/ViewComplaint.html', {"doctor": ob, 'comp': a})

# @login_required(login_url='/')
def ViewComplaintSearch(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    did = request.POST["did"]
    ob = doctor_table.objects.filter(LOGIN__type="doctor")
    ob1 = complaint_table.objects.filter(DOCTOR=did)
    return render(request, 'Admin/ViewComplaint.html', {"doctor": ob, "comp": ob1})

# @login_required(login_url='/')

def viewFeedback(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    doc = doctor_table.objects.filter(LOGIN__type="doctor")
    feed = feedback_table.objects.all()
    return render(request, 'Admin/viewFeedback.html', {'data': doc, 'feed': feed})

# @login_required(login_url='/')
def searchFeedback(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    name = request.POST["select"]
    doc = doctor_table.objects.all()
    ob = feedback_table.objects.filter(DOCTOR=name)
    return render(request, 'Admin/ViewFeedback.html', {"feed": ob, "data": doc})

# @login_required(login_url='/')
def ViewUser(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    ob = user_table.objects.all()
    return render(request, 'Admin/ViewUser.html', {"data": ob})

# @login_required(login_url='/')
def searchuser(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    name = request.POST["textfield"]
    ob = user_table.objects.filter(name__icontains=name)
    return render(request, 'Admin/ViewUser.html', {"data": ob})


# def viewUserSearch(request):
#   did = request.POST["did"]
#  ob = user_table.objects.all()
# ob1 = user_table.objects.filter(USER=did)
# return render(request, 'Admin/ViewUser.html', {"user": ob, "data": ob1})


# @login_required(login_url='/')
def DoctorHome(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    # return render(request, 'Doctor/index.html')
    return render(request, 'Doctor/indexmain.html')

# @login_required(login_url='/')
def Doctor_signup(request):
    # if request.session['lid'] == '':
    #     return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    return render(request, 'Doctor/DoctorReg.html')

# @login_required(login_url='/')
def Doctor_signup_post(request):
    # if request.session['lid'] == '':
    #     return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    Name = request.POST['textfield']
    DOB = request.POST['textfield2']
    gender = request.POST['radiobutton']
    Qualification = request.POST['textfield3']
    Experience = request.POST['textfield4']
    Places = request.POST['textfield5']
    Post = request.POST['textfield6']
    PIN = request.POST['textfield7']
    Landmark = request.POST['textfield8']
    Phoneno = request.POST['textfield9']
    Email = request.POST['textfield10']
    passw = request.POST['textfield11']

    if request.FILES:
        image = request.FILES['file']
        fs = FileSystemStorage()
        fp = fs.save(image.name, image)

    ob = login_table()
    ob.user_name = Email
    ob.password = passw
    ob.type = 'pending'
    ob.save()

    ob2 = doctor_table()
    ob2.LOGIN = ob
    ob2.name = Name
    ob2.image = fp
    ob2.date_of_birth = DOB
    ob2.gender = gender
    ob2.qualification = Qualification
    ob2.experience = Experience
    ob2.place = Places
    ob2.phone_number = Phoneno
    ob2.email = Email
    ob2.post = Post
    ob2.pin = PIN
    ob2.landmark = Landmark

    ob2.save()

    return HttpResponse('''<script> alert('Registere');window.location='/';</script>''')

# @login_required(login_url='/')
def docManageSchedule(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    a=schedule_table.objects.filter(DOCTOR__LOGIN_id=request.session['lid'])
    return render(request, 'Doctor/ManageSchedule.html',{'data':a})

# @login_required(login_url='/')
def deletedocschedule(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    ob=schedule_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert('deleted');window.location='/docManageSchedule';</script>''')





# def select_booking(request, id):
# request.session['bid'] = id  # Set the booking ID in the session
# return render(request,'Doctor/add_report')  # Redirect to the page where the report is added
#
# def AddSchedule(request, id):
#     request.session['sid'] = id
#     return render(request, 'Doctor/AddSchedule.html')


# @login_required(login_url='/')
def AddSchedule(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    # datt=datetime.datetime.now().date().isoformat()

    datt = (datetime.datetime.now().date() + datetime.timedelta(days=1)).isoformat()
    print(datt,"=================================")
    return render(request, 'Doctor/AddSchedule.html',{"date":datt})

# @login_required(login_url='/')
def AddSchedule_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    From_Date = request.POST['textfield']
    To_Date = request.POST['textfield2']
    From_Time = request.POST['textfield3']
    To_Time = request.POST['textfield4']
    # Days = request.POST.getlist('checkbox')
    Days = request.POST.getlist('days[]')

    print(Days)

    for i in Days:

        ob = schedule_table()
        ob.from_Date = From_Date
        ob.to_Date = To_Date
        ob.foom_time = From_Time
        ob.to_time = To_Time
        ob.days = i
        ob.DOCTOR = doctor_table.objects.get(LOGIN_id=request.session['lid'])
        ob.save()
    return HttpResponse('''<script> alert('Schedule added');window.location='/docManageSchedule';</script>''')
# @login_required(login_url='/')

def viewbooking(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    ob = booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN_id=request.session['lid'])
    return render(request, 'Doctor/viewbooking.html', {'data': ob})
# @login_required(login_url='/')
def search_booking(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    date=request.POST['textfield']
    ob = booking_table.objects.filter(date__icontains=date)
    return render(request, 'Doctor/viewbooking.html', {'data': ob,'date':date})

# @login_required(login_url='/')
def view_report(request,id):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    request.session['bid']=id
    ob=booking_table.objects.get(id=id)
    obb=report_table.objects.filter(booking_id=request.session['bid'])
    return render(request,'Doctor/viewReport.html',{'data': ob,'val':obb})


# def view_report(request):
#   ob = report_table.objects.filter(booking__id=request.session['bid'])  # Adjust this based on your relationships
#  return render(request, 'Doctor/viewReport.html', {'data': ob})
#def view_report(request):
   # reports = report_table.objects.all()
    #return render(request, 'Doctor/viewReport.html', {'data': reports})

# @login_required(login_url='/')
def add_report(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    return render(request, 'Doctor/Addreport.html')


# def add_report_post(request):
#  booking_id = request.session.get('bid')
#  if not booking_id:
#     return HttpResponse("Booking ID is missing from the session", status=400)

# report = request.FILES.get('file')
# findings = request.POST['textfield']
# fs = FileSystemStorage()
# fp = fs.save(report.name, report)
# ob = report_table()
# ob.booking = booking_table.objects.get(id=booking_id)
# ob.report = fp
# ob.report_typr = findings
# ob.date = datetime.datetime.today()
# ob.save()
# return HttpResponse('''<script> alert('added');window.location='/viewbooking';</script>''')
# @login_required(login_url='/')
def add_report_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    report = request.FILES.get('file')
        # report_type=request.POST['textfield1']
    finding = request.POST['textfield']
    fs = FileSystemStorage()
    fp = fs.save(report.name, report)
    ob = report_table()
    ob.booking = booking_table.objects.get(id=request.session['bid'])
    ob.report = fp
        # ob.finding = findings
    ob.report_typr = finding
    ob.date = datetime.datetime.today()
    ob.save()
    return HttpResponse('''<script> alert('added');window.location='/viewbooking';</script>''')
    #   ob.report_typr = findings
# @login_required(login_url='/')
def UserHome(request):
    return render(request, 'User/index.html')

# @login_required(login_url='/')
def User_signup(request):
    return render(request, 'User/userreg.html')

# @login_required(login_url='/')
def User_signup_post(request):
    Name = request.POST['textfield']
    gender = request.POST['radiobutton']
    DOB = request.POST['textfield2']
    place = request.POST['textfield5']
    Phone = request.POST['textfield9']
    email = request.POST['textfield10']
    #username = request.POST['textfield11']
    Password = request.POST['textfield12']

    if login_table.objects.filter(user_name=email).exists():
        return HttpResponse(
            '''<script> alert('User already registered with this email');window.location='/User_signup';</script>''')
    if login_table.objects.filter(password=Password).exists():
        return HttpResponse(
            '''<script> alert('Password already in use. Please choose a different password');window.location='/User_signup';</script>''')
    ob = login_table()
    ob.user_name = email
    ob.password = Password
    ob.type = 'user'
    ob.save()

    ob2 = user_table()
    ob2.LOGIN = ob
    ob2.name = Name
    ob2.gender = gender
    ob2.date_of_birth = DOB
    ob2.place = place
    ob2.phone_number = Phone
    ob2.email = email
    ob2.save()
    return HttpResponse('''<script> alert('Registere');window.location='/';</script>''')

# @login_required(login_url='/')
def viewDoctor(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    doc = doctor_table.objects.filter(LOGIN__type="doctor")
    return render(request, 'User/viewdoc.html', {"data": doc})


# def view_user_complaints(request):
#    user_id = request.session.get('lid')
#   comp = complaint_table.objects.filter(USER_id=user_id)  # Filter complaints for this user
# return render(request, 'User/ViewComplaaint.html', {"com": comp})
#  return HttpResponse(f"Complaints: {list(comp)}")
# @login_required(login_url='/')
def view_user_complaints(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    user_id = request.session.get('lid')
    comp = complaint_table.objects.filter(USER_id=user_id)
    return render(request, 'User/viewcomplaaint.html', {"com": comp})

# @login_required(login_url='/')
def SendFeedback(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    request.session['did'] = id
    return render(request, 'User/sendfeedbackk.html')

# @login_required(login_url='/')
def sendFeedback_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    feedback = request.POST['textfield']
    Rating = request.POST['textfield2']
    ob = feedback_table()
    ob.feedback = feedback
    ob.rating = Rating
    ob.DOCTOR = doctor_table.objects.get(id=request.session['did'])
    ob.USER = user_table.objects.get(LOGIN__id=request.session['lid'])
    ob.date = datetime.datetime.now()
    ob.save()
    return HttpResponse('''<script> alert('Feedback Added');window.location='/viewDoctor';</script>''')

# @login_required(login_url='/')
def ViewSchedule(request, id):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    ob = schedule_table.objects.filter(DOCTOR_id=id)
    return render(request, 'User/viewschedule.html', {"doc": ob})
# def ViewSchedule(request, id):
#     if request.session['lid'] == '':
#         return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
#
#     schedules = schedule_table.objects.filter(DOCTOR_id=id)
#     days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#
#     schedule_by_day = {day: [] for day in days_of_week}
#
#     for sched in schedules:
#         # Make sure sched.days is a list (assuming it's stored like a Python list or comma-separated string)
#         days = sched.days if isinstance(sched.days, list) else eval(sched.days)
#         for day in days:
#             if day in schedule_by_day:
#                 schedule_by_day[day].append(sched)
#
#     return render(request, 'User/viewschedule.html', {"schedule_by_day": schedule_by_day})


# # @login_required(login_url='/')
# def ViewSchedule(request, id):
#     if request.session['lid'] == '':
#         return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
#     ob = schedule_table.objects.filter(DOCTOR_id=id, to_Date__gt=datetime.datetime.today())
#     return render(request, 'User/viewschedule.html', {"doc": ob})

# @login_required(login_url='/')
# def  book_schedule(request,id):
#     if request.session['lid'] == '':
#         return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
#     request.session['sid']=id
#
#     ob=booking_table()
#     ob.SCHEDULE=schedule_table.objects.get(id= request.session['sid'])
#     ob.USER=user_table.objects.get(LOGIN_id=request.session['lid'])
#     ob.status='booked'
#     ob.date=datetime.datetime.today()
#     ob.save()
#     return HttpResponse('''<script> alert('booked');window.location='/viewDoctor';</script>''')
#




def book_schedule(request, id):
    if request.session.get('lid', '') == '':
        return HttpResponse('''<script>alert('Logged out'); window.location='/';</script>''')

    request.session['sid'] = id
    user = user_table.objects.get(LOGIN_id=request.session['lid'])
    schedule = schedule_table.objects.get(id=request.session['sid'])

    # Check if already booked
    existing_booking = booking_table.objects.filter(USER=user, SCHEDULE=schedule).first()
    if existing_booking:
        return HttpResponse('''<script>alert('Already booked this schedule'); window.location='/viewDoctor';</script>''')

    # If not already booked, proceed
    ob = booking_table()
    ob.SCHEDULE = schedule
    ob.USER = user
    ob.status = 'booked'
    ob.date = datetime.datetime.today()
    ob.save()

    return HttpResponse('''<script>alert('Booked successfully'); window.location='/viewDoctor';</script>''')



# def book_schedule(request, id):
#     if request.session.get('lid', '') == '':
#         return HttpResponse('''<script>alert('Logged out'); window.location='/';</script>''')
#
#     request.session['sid'] = id
#     user = user_table.objects.get(LOGIN_id=request.session['lid'])
#     schedule = schedule_table.objects.get(id=request.session['sid'])
#
#     # Check if already booked
#     existing_booking = booking_table.objects.filter(USER=user, SCHEDULE=schedule).first()
#     if existing_booking:
#         return HttpResponse('''<script>alert('Already booked this schedule'); window.location='/viewDoctor';</script>''')
#
#     # Check if schedule is at least 24 hours away
#     current_time = datetime.datetime.now()
#     schedule_time = schedule.datetime_field  # Replace `datetime_field` with the actual field in schedule_table
#     time_diff = schedule_time - current_time
#
#     if time_diff.total_seconds() < 86400:  # 86400 seconds = 24 hours
#         return HttpResponse('''<script>alert('Slot must be booked at least 24 hours in advance'); window.location='/viewDoctor';</script>''')
#
#     # Proceed with booking
#     ob = booking_table()
#     ob.SCHEDULE = schedule
#     ob.USER = user
#     ob.status = 'booked'
#     ob.date = current_time
#     ob.save()
#
#     return HttpResponse('''<script>alert('Booked successfully'); window.location='/viewDoctor';</script>''')
#


def Prediction(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    return render(request, 'User/prediction.html')

# @login_required(login_url='/')
def Prediction_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    img = request.FILES["file"]

    fs = FileSystemStorage()
    fsave = fs.save(img.name, img)

    ps = predictfn(r'C:\Users\kshiv\PycharmProjects\stroke_identification\media\\' + fsave)

    return render(request, 'User/prediction.html', {"res": ps})

def Prediction2(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    return render(request, 'User/clinicaldata.html')
# original:from .rf_training import predict_rf_fn
# def Prediction2_POST(request):
#     print(request.POST)
#     if request.session['lid'] == '':
#         return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
#     gender=float(request.POST["gender"])
#     age = request.POST["age"]
#     hypertension = request.POST["hypertension"]
#     heart_disease = request.POST["heart_disease"]
#     ever_married = request.POST["ever_married"]
#     work = request.POST["work_type"]
#     residence = request.POST["Residence_type"]
#     glucose = float(request.POST["avg_glucose_level"])
#     bmi = float(request.POST["bmi"])
#     smoke=request.POST["smoking_status"]
#     row=[gender,age,hypertension,heart_disease,ever_married,work,residence,glucose,bmi,smoke]
#     res=predict_rf_fn(row)
#     print(res)
#     pr=int(res[0])
#     if(pr==0):
#         pr="Normal"
#         print("Normal")
#
#     else:
#         pr=res[1]+" Stroke"
#         print("stroke")
#
#     # print(pr)
#
#
#   -->  return render(request, 'User/clinicaldata.html', {"res":pr})
from .rf_training import predict_stroke_and_severity


def Prediction2_POST(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logged out');window.location='/';</script>''')
    print(request.POST)

    # if request.session.get('lid', '') == '':
    #     return HttpResponse('''<script> alert('Logged out');window.location='/';</script>''')

    # Get form values
    gender = int(request.POST["gender"])
    age = int(request.POST["age"])
    hypertension = int(request.POST["hypertension"])
    heart_disease = int(request.POST["heart_disease"])
    ever_married = int(request.POST["ever_married"])
    work = int(request.POST["work_type"])
    residence = int(request.POST["Residence_type"])
    glucose = float(request.POST["avg_glucose_level"])
    bmi = float(request.POST["bmi"])
    smoke = int(request.POST["smoking_status"])

    # Input row for prediction
    row = [gender, age, hypertension, heart_disease, ever_married,
           work, residence, glucose, bmi, smoke]

    # Predict stroke and severity (feature-based only)
    prediction, severity = predict_stroke_and_severity(row)

    print("Prediction:", prediction)
    print("Severity:", severity)

    return render(request, 'User/clinicaldata.html', {
        "res": prediction,
        "severity": severity
    })

# from .rf_training import predict_rf_fn
#
# def Prediction2_POST(request):
#     print(request.POST)
#
#     # Check session
#     if request.session.get('lid', '') == '':
#         return HttpResponse('''<script> alert('Logged out'); window.location='/';</script>''')
#
#     # Extract POST data
#     gender = float(request.POST["gender"])
#     age = float(request.POST["age"])
#     hypertension = float(request.POST["hypertension"])
#     heart_disease = float(request.POST["heart_disease"])
#     ever_married = float(request.POST["ever_married"])
#     work = float(request.POST["work_type"])
#     residence = float(request.POST["Residence_type"])
#     glucose = float(request.POST["avg_glucose_level"])
#     bmi = float(request.POST["bmi"])
#     smoke = float(request.POST["smoking_status"])
#
#     # Prepare input row for model
#     row = [gender, age, hypertension, heart_disease, ever_married, work, residence, glucose, bmi, smoke]
#
#     # Run prediction
#     result = predict_rf_fn(row)
#     prediction = int(result[0])
#     severity = result[1]
#
#     # Format result for display
#     if prediction == 0:
#         status = "Normal"
#     else:
#         status = f"{severity} Stroke"
#
#     print("Prediction Result:", status)
#
#     # Pass result to template
#     return render(request, 'User/clinicaldata.html', {'prediction_result': status})

# @login_required(login_url='/')
# def Prediction3(request):
#     if request.session['lid'] == '':
#         return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
#     return render(request, 'User/risk.html')
# from .knn_risk import predict_user_input
# def prediction3_post(request):
#     chest= request.POST["chest_pain"]
#     breath=request.POST["shortness_of_breath"]
#     heartbeat=request.POST["irregular_heartbeat"]
#     weakness=request.POST["fatigue_weakness"]
#     dizziness=request.POST["dizziness"]
#     swelling=request.POST["swelling_edema"]
#     pain=request.POST["pain_neck_jaw"]
#     sweating=request.POST["excessive_sweating"]
#     cough=request.POST["persistent_cough"]
#     nausea=request.POST["nausea_vomiting"]
#     bp=request.POST["high_bp"]
#     discomfort=request.POST["chest_discomfort_activity"]
#     cold=request.POST["cold_hands_feet"]
#     snoring=request.POST["snoring_apnea"]
#     anxiety=request.POST["anxiety"]
#     ages=float(request.POST["age"])
#     row = [chest, breath, heartbeat, weakness, dizziness, swelling, pain, sweating, cough, nausea,bp,discomfort,cold,snoring,anxiety,ages]
#     risk_class= predict_user_input(row)
#     print(risk_class)
#     risk=int(risk_class[0])
#     if risk == 1:
#         result = f"⚠️ High Stroke Risk ({risk_percent:.2f}%)"
#
#     else:
#         result = f"✅ Low Stroke Risk ({risk_percent:.2f}%)"
#     return render(request,'User/risk.html', {"res":result})
#     # print(pr)
#




# Scale the input using the same scalers
# input_scaled_c = scaler_c.transform([input_features])
# input_scaled_r = scaler_r.transform([input_features])
#
# # Make predictions
# risk_class = knn_classifier.predict(input_scaled_c)[0]
# risk_percent = knn_regressor.predict(input_scaled_r)[0]

# Optional: Format result text
#    if risk == 1:
#     result = f"⚠️ High Stroke Risk ({risk_percent:.2f}%)"
# else:
#     result = f"✅ Low Stroke Risk ({risk_percent:.2f}%)"
#
# return render("User/risk.html", res=result)


def user_view_com(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    user_id=request.session['lid']
    comp = complaint_table.objects.filter(USER__LOGIN__id=user_id)
    return render(request,'User/viewcomp.html',{"com": comp})

# @login_required(login_url='/')
# def add_new(request):
#     if request.session['lid'] == '':
#         return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
#     a=doctor_table.objects.filter(LOGIN__type='doctor')
#     ob=booking_table.objects.filter(SCHEDULE__DOCTOR_id=a.id)
#     return render(request, 'User/addcomplaint.html',{"val":ob})



from django.shortcuts import render, HttpResponse
from .models import doctor_table, booking_table

def add_new(request):
    if 'lid' not in request.session or request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logged out'); window.location='/'; </script>''')

    # Get distinct doctor IDs from bookings
    booked_doctor_ids = booking_table.objects.filter(USER__LOGIN__id=request.session['lid']).values_list('SCHEDULE__DOCTOR', flat=True).distinct()

    # Get doctor details only for booked doctors
    booked_doctors = doctor_table.objects.filter(id__in=booked_doctor_ids)

    return render(request, 'User/addcomplaint.html', {"val": booked_doctors})

# @login_required(login_url='/')
def add_new_Post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')

    comp = request.POST['textfield2']
    doct = request.POST['select']
    ob=complaint_table()
    ob.DOCTOR = doctor_table.objects.get(id=doct)
    ob.USER = user_table.objects.get(LOGIN__id=request.session['lid'])
    ob.complaint=comp
    ob.reply='pending'
    ob.date = datetime.datetime.today()
    ob.save()
    return HttpResponse('''<script> alert('added');window.location='/add_new';</script>''')
# @login_required(login_url='/')
def user_view_report(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script> alert('Logouted');window.location='/';</script>''')
    ob=report_table.objects.filter(booking__USER__LOGIN_id=request.session['lid'])
    return render(request,'User/viewreport .html',{'data':ob})


def forget_password(request):
   return render(request,'forget.html')
def forgot_password(request):
    print(request.POST)
    try:
        print("1")
        print(request.POST)
        email = request.POST['email']
        print(email)
        s=login_table.objects.filter(user_name=email)

        print(s, "=============")
        if len(s)==0:
            return HttpResponse('''<script>alert('invalid email');window.location='/forget_password'</script>''')

            # return jsonify({'task': 'invalid email'})
        else:
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('a41514250@gmail.com', 'hqly ibgw igds gxmq')
                print("login=======")
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText("Your new password id : " + str(s[0].password))
            print(msg)
            msg['Subject'] = 'OutPass'
            msg['To'] = email
            msg['From'] = 'a41514250@gmail.com'

            print("ok====")

            try:
                gmail.send_message(msg)
            except Exception as e:
                return HttpResponse('''<script>alert('invalid email');window.location='/forget_password'</script>''')
            return HttpResponse('''<script>alert('sended');window.location='/'</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert('invalid email');window.location='/forget_password'</script>''')
#def forget_password_post(request):
 #   email=request.POST['email']
  #  return render(request,'/reset.html')



#def admin_Dashboard(request):
 #   return render(request, 'admin.html')