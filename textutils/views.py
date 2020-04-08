from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello bilal" + '"<input type="submit" value="Send Request">"')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    if removepunc == "on":
        analyzed = ""
        print(djtext)
        pucntuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in pucntuations:
                analyzed = analyzed + char

        parm = {"purpose": "Removed punctuation", "analyzed_text": analyzed}
        return render(request, 'analyzed.html', parm)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        parm = {"purpose": "Changed text", "analyzed_text": analyzed}
        return render(request, 'analyzed.html', parm)
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        parm = {"purpose": "New lines removed", "analyzed_text": analyzed}
        return render(request, 'analyzed.html', parm)

    elif (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        parm = {"purpose": "New lines removed", "analyzed_text": analyzed}
        return render(request, 'analyzed.html', parm)





    else:
        return HttpResponse("You must need to check Remove punctuation:")



# def camptalizeFirst(request):
#     return HttpResponse("will captalize")
#
#
# def newLineremove(request):
#     return HttpResponse("will remove new line")
#
#
# def spaceremove(request):
#     return HttpResponse("will remove space")
#
#
# def charcount(request):
#     return HttpResponse("Hello bilal bahi")
