from django.shortcuts import render

# Create your views here.
def getinfo(request):
    context={"Name":"Vijay",
            "Email":"vijaykumar.b@apssdc.in",
            "Designation":"Python Developer",
            "Experince":"5+"
            }
    return render(request,'Employee/getinfo.html',context)
def senddata(request):
        if request.method=='POST':
                name=request.POST['name']
                email=request.POST['email']
                desig=request.POST['designation']
                ex=request.POST['ex']
                context={'Name':name,
                        "Email":email,
                        "Designation":desig,
                        "Experince":ex}

                return render(request,'Employee/getinfo.html',context)

        return render(request,'Employee/senddata.html')