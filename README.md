# Ex.05 Design a Website for Server Side Processing
## Date:04.12.24

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
maths.html

<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>Calculation of power</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style type="text/css">
body {
    background-color:aliceblue;
}
.edge {
    width: 100%;
    padding-top: 200px;
    text-align: center;
}
.box {
    display: inline-block;
    border: thick dashed rgb(191, 54, 212);
    width: 500px;
    min-height: 300px;
    font-size: 15px;
    background-color:blueviolet;
    margin-left:430px;
}
.formelt {
    color: rgb(19, 30, 32);
    text-align: center;
    margin-top: 9px;
    margin-bottom:8px;
}
h1 {
    color: rgb(130, 63, 63);
    padding-top: 20px;
}
</style>
</head>
<body>
     <center>
      <h1>R MANIYARSAN (24900020)</h1>
      </center>
     
      <div class="definition">
      <h1>POWER OF CALCULATION</h1>
    </div>
    <div class="box">
    
        <form method="POST">
            {% csrf_token %}
            <div class="formelt">
                Intensity: <input type="text" name="Intensity" value="{{I}} "></input>(in A)<br/>
            </div>
            <div class="formelt">
                Resistance: <input type="text" name="Resistance" value="{{R}} "></input>(in R)<br/>
            </div>
            <div class="formelt">
                <input type="submit" value="Calculate"></input><br/>
            </div>
            <div class="formelt">
                power: <input type="text" name="power" value="{{power}} "></input>watts<br/>
            </div>
        </div>
        </form>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin 
from django.urls import path 
from mathsapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('power/',views.power,name="calculatepower"),
    path('',views.power,name="calculatepower")
]
```

## SERVER SIDE PROCESSING:
![alt text](<1 (2).png>)


## HOMEPAGE:
![alt text](<2 (2).png>)


## RESULT:
The program for performing server side processing is completed successfully.
