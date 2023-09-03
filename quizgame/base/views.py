from django.shortcuts import render, redirect

mcqBank = [
    {
        'question': '1. Who is the father of Computers?',
        'options': ['James Gosling', 'Charles Babbage', 'Dennis Ritchie', 'Bjarne Stroustrup'],
        'answer': 'Charles Babbage'
    },
    {
        'question': '2. Which of the following is the correct abbreviation of COMPUTER?',
        'options': ['Commonly Occupied Machines Used in Technical and Educational Research', 'Commonly Operated Machines Used in Technical and Environmental Research', 'Commonly Oriented Machines Used in Technical and Educational Research', 'Commonly Operated Machines Used in Technical and Educational Research'],
        'answer': 'Commonly Operated Machines Used in Technical and Educational Research'
    },
    {
        'question': '3. What is the full form of CPU?',
        'options': ['Computer Processing Unit', 'Computer Principle Unit', 'Central Processing Unit', 'Control Processing Unit'],
        'answer': 'Central Processing Unit'
    },
    {
        'question': '4. Which of the following computer language is written in binary codes only?',
        'options': ['Pascal', 'Machine Language', 'C', 'C#'],
        'answer': 'Machine Language'
    },
    {
        'question': '5. Which of the following is the smallest unit of data in a computer?',
        'options': ['Bit', 'KB', 'Nibble', 'Byte'],
        'answer': 'Bit'
    },
    {
        'question': '6. Which of the following is designed to control the operations of a computer?',
        'options': ['User', 'Application Software', 'System Software', 'Utility Software'],
        'answer': 'System Software'
    }
]

score = 0

# Create your views here.
def homePage(request):
    global score
    score = 0
    context = {'total': len(mcqBank)}
    return render(request, 'base/home-page.html', context)


def quizPage(request):
    global score
    score = 0
    if request.method == 'POST':
        for question in mcqBank:
            if request.POST[question['question']] == question['answer']:
                score += 1
        # return redirect('result-page')
        total = len(mcqBank)
        percentage = int((score / total) * 100)
        context = {'score': score, 'total': total, 'percentage': percentage}
        return render(request, 'base/result-page.html', context)
    context = {'mcqBank': mcqBank, 'total': len(mcqBank)}
    return render(request, 'base/quiz-page.html', context)

# def resultPage(request):
#     global score
#     total = len(mcqBank)
#     percentage = int((score / total) * 100)
#     context = {'score': score, 'total': total, 'percentage': percentage}
#     return render(request, 'base/result-page.html', context)