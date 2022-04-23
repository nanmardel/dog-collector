from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # like res.render in Express

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog("Lou", 'Golden Retriever', 'very cute', 7),
    Dog('Trix', 'Chihuahua', 'fiesty', 3),
    Dog('Tood', 'Pug', 'happy little guy', 8),
    Dog('Molly', 'French Bulldog', 'party animal', 4)
]        

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return render(request, 'about.html')  

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})      