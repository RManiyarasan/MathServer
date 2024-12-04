from django.shortcuts import render
def power(request): 
    context={} 
    context['power'] = "0"
    context['I'] = "0" 
    context['R'] = "0"  
    if request.method == 'POST': 
        print("POST method is used")
        R = request.POST.get('Resistance','0')
        I = request.POST.get('Intensity','0')
        print('request=',request)  
        print('Intensity=',I) 
        print('Resistance=',R)
        power= int(R) * int(I) *int(I)
        context['power'] = power
        context['I'] = I
        context['R'] = R
        print('Power=',power) 
    return render(request,'mathsapp/maths.html',context)
