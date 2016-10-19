from django.shortcuts import render
from django.template.response import TemplateResponse,HttpResponse

# Create your views here.

def index(request):
    context = dict(


    )
    return TemplateResponse(request, "sometemplate.html", context)



def shouyin(request):
    context = dict(


    )
    return TemplateResponse(request, "sometemplate.html", context)

def ruku(request):
    context = dict(


    )
    return TemplateResponse(request, "sometemplate.html", context)


def gettxt(request):
    try:
        file_name = "tmp/newp.txt"
        ss = []
        with open(file_name) as f:
            for x in f.read():
                ss.append(x)
            c = '\n\r'.join(ss)

        from django.http import StreamingHttpResponse
        response = StreamingHttpResponse(c)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
    except Exception as e:
        print e
        response = ''
    if response:
        return response
    else:
        return HttpResponse('')