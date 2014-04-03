from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apps.answer.models import Answers
from serializers import AnswersSerializer
from megahal import *
import re

megahal = MegaHAL()


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def answers_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        print megahal.get_reply('hey, wazzap')
        try:
            looking = request.GET['question']
        except:
            pass

        try:
            answer = Answers.objects.get(question__icontains=looking)
            print answer
            print "database pattern"
        except:
            try:
                answer = ask_omniHal(request.GET['question'])
                print "omniHal patter"
            except:
                answer = "{'pk': 1, 'answer': 'Piracy is your friend'}"
                print "lazy pattern"


        serializer = AnswersSerializer(answer)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnswersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

csrf_exempt
def answers_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    answer = Answers.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = AnswersSerializer(answer)
        return JSONResponse(serializer.data)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AnswersSerializer(answer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Answers.delete()
        return HttpResponse(status=204)



def ask_omniHal(question):
    onmi = omniHal()
    onmi.question = question
    onmi.answer = megahal.get_reply(question)
    print onmi.answer
    return onmi


class omniHal(object):
    pk = "636"

def omniLearn():

    file = open("/home/palle/Project/django/pt/talk/talk/apps/answer/Neuromancer.txt")
    text = file.read()
    megahal.learn(text)

