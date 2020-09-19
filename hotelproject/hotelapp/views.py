from django.shortcuts import render,redirect
#from .forms import CustomerForm
from django.http import HttpResponse
from .models import CustomerModel,RoomModel,AdminModel,BookingModel
def home(request):
    return render(request,"hotelapp/home.html")

def addCustomer(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        emailid = request.POST['emailid']
        password = request.POST['password']
        contactno = request.POST['contactno']
        customermodel = CustomerModel(custName = fullname,custEmailId=emailid,custPassword=password,custContact=contactno)
        customermodel.save()
        status = "You are successfully registered"
        return render(request,"hotelapp/home.html",{'status':status})
    return render(request,"hotelapp/register.html")

def addRoom(request):
    if request.method == "POST":
       roomtype = request.POST['type']
       beds = request.POST['beds']
       capacity = request.POST['capacity']
       date = request.POST['date']
       price = request.POST['price']
       roommodel = RoomModel(roomType=roomtype,beds=beds,capacity=capacity,date=date,price=price)
       roommodel.save()
       print("Done")
       status = "You have successfully added the room"
       return render(request, "hotelapp/home.html", {'status': status})
    return render(request,"hotelapp/addroom.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        utype = request.POST['utype']
        print(username , password)

        if utype == 'Customer':
            customer = CustomerModel.objects.get(custEmailId = username)
            if customer != None:
                print(customer.custEmailId , customer.custPassword)
                if customer.custEmailId == username and customer.custPassword == password:
                    request.session['customer'] = username
                    return render(request, "hotelapp/home.html",{'status':'Login Successfully.'})
                else:
                    return render(request, "hotelapp/login.html",{'status':'Bad credentials'})
            else:
                return render(request, "hotelapp/login.html", {'status': 'Bad credentials'})

        elif utype == 'Admin':
            admin = AdminModel.objects.get(username = username)
            if admin.username == username and admin.password == password:
                request.session['admin'] = username
                return render(request, "hotelapp/home.html",{'status':'Login Successfully.'})
            else:
                return render(request, "hotelapp/login.html",{'status':'Bad credentials'})
    return render(request,"hotelapp/login.html")

def logout(request):
	request.session.clear()
	return render(request,'hotelapp/home.html')

def bookRoom(request,roomId):
    if request.method == "POST":
        name = request.POST['name']
        quest = request.POST['quest']
        roomId = request.POST['roomno']
        roomType = request.POST['type']
        beds = request.POST['beds']
        capacity = request.POST['capacity']
        price = request.POST['price']
        checkindate = request.POST['checkindate']
        checkoutdate = request.POST['checkoutdate']
        bookingmodel = BookingModel(user=name,quest=quest,roomId=roomId,roomType=roomType, beds=beds, capacity=capacity,price=price,check_in=checkindate,check_out=checkoutdate)
        bookingmodel.save()
        roommodel = RoomModel.objects.filter(roomId=roomId)
        obj = roommodel.update(status="Booked")
        return render(request, "hotelapp/home.html", {'status':"You have successfully booked your room"})
    else:
        roommodel = RoomModel.objects.get(roomId=roomId)
        custEmailId = request.session['customer']
        return render(request,"hotelapp/bookroom.html",{'room':roommodel,'customer':custEmailId})

    return render(request,"hotelapp/bookroom.html")



def bookingList(request):
    blist = BookingModel.objects.all()
    return render(request,"hotelapp/booking_list.html",{'blist':blist})

def roomList(request):
    rlist = RoomModel.objects.all()
    return render(request,"hotelapp/room_list.html",{'rlist':rlist})

def searchRoom(request):
    check_in = request.GET['checkindate']
    check_out = request.GET['checkoutdate']

    blist = BookingModel.objects.filter(check_in=check_in, check_out=check_out)
    return render(request, "hotelapp/booking_list.html", {'blist': blist})
