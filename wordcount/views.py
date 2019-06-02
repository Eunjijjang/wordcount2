from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    text = request.GET['fulltext']
    words = text.split()
    #스트링이라는 문자열을 공백을 기준으로 나눠서 리스트로 저장해주는 함수를
    #스플릿 함수라고 한다. 텍스트(원문)라는 것을 문자열을 공백을 기준으로 나눠
    #리스트로 만들어주는것! 이것 자체가 리스트임 
    #이걸 또 변수로 만들어줌
    #텍스트라는 변수이 코드 자체가 원문의 글 전체를 뜻함.
    word_dictionary = {}
    #빈 사전의 이름은 word_dictionary 로 지정하구
    for word in words: 
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
            #새로운 단어이면(add to dictionary)
    # 워드 단어를 쭉 순회하고 해당 단어사전에 넣는 함수
    # word는 반복문 변수이다.
    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()})
    #렌더라고 하는 함수는 3개의 인자를 받을 수 있다. 
    # 첫번째는 리퀘스트라는 객체를 받고, 두번째는 템플릿의 이름을 인자로, 
    # 선택적으로 세번째 인자는 사전형 객체를 받는다.
    # dictionary 객체.
def about(request):
    return render(request, 'about.html')
# 어바웃페이지 함수
def result(request):
    text = request.GET['fulltext']
    words = text.split()
    #스트링이라는 문자열을 공백을 기준으로 나눠서 리스트로 저장해주는 함수를
    #스플릿 함수라고 한다. 텍스트(원문)라는 것을 문자열을 공백을 기준으로 나눠
    #리스트로 만들어주는것! 이것 자체가 리스트임 
    #이걸 또 변수로 만들어줌
    #텍스트라는 변수이 코드 자체가 원문의 글 전체를 뜻함.
    word_dictionary = {}
    #빈 사전의 이름은 word_dictionary 로 지정하구
    for word in words: 
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
            #새로운 단어이면(add to dictionary)
    # 워드 단어를 쭉 순회하고 해당 단어사전에 넣는 함수
    # word는 반복문 변수이다.
    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()})
    #  사전형 함수중에 <단어 : 몇번, 단어 : 몇번> 쌍들을 보내주는함수 .items()

def self(request):
    return render(request, 'self.html')
# 리절트 함수
# 파이썬의 사전형 객체(중요) 왼편엔 키값, 오른편엔 벨류!
#총 단어수는 words의 길이(len)
