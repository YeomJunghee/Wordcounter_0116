from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']

    words = text.split() 
    #split - 괄호 안의 값으로 문자열을 나누어줌

    word_dictionary={}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1

    #len = 문자열 길이 세는 함수
    return render(request, 'result.html', {'full': text,'total': len(text),'total_s':len(text.replace(" ", "")) ,'di':word_dictionary.items()})