from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apps.answer.models import Answers
from serializers import AnswersSerializer
import re
from cobe.brain import Brain

BRAIN_FILE = "cobe.brain"

brain = Brain(BRAIN_FILE)

def LearnAndReply(line):
	onmi = omniHal()
	onmi.question = line
	brain.learn(line)
	onmi.answer = brain.reply(line)
	return onmi

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def answers_list(request):
	if request.method == 'GET':	
		answer = LearnAndReply((request.GET['question']))
		serializer = AnswersSerializer(answer)
		return JSONResponse(serializer.data)
    

class omniHal(object):
    pk = "636"

def splitParagraphIntoSentences(paragraph):
    import re
    sentenceEnders = re.compile(r"""
        # Split sentences on whitespace between them.
        (?:               # Group for two positive lookbehinds.
          (?<=[.!?])      # Either an end of sentence punct,
        | (?<=[.!?]['"])  # or end of sentence punct and quote.
        )                 # End group of two positive lookbehinds.
        (?<!  Mr\.   )    # Don't end sentence on "Mr."
        (?<!  Mrs\.  )    # Don't end sentence on "Mrs."
        (?<!  Jr\.   )    # Don't end sentence on "Jr."
        (?<!  Dr\.   )    # Don't end sentence on "Dr."
        (?<!  Prof\. )    # Don't end sentence on "Prof."
        (?<!  Sr\.   )    # Don't end sentence on "Sr."
        \s+               # Split on whitespace between sentences.
        """,
        re.IGNORECASE | re.VERBOSE)
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList

def make_sentence(self):
    f = open("Neuromancer.txt", 'r')
    text = f.read()
    text = text.replace('\n', ' ').replace('\r', '').replace('  ', ' ').replace('   ', ' ').replace('"', ' ')
    mylist = []
    sentences = splitParagraphIntoSentences(text)
    print "sentences extracted"
    for s in sentences:
		if s and not line.startswith('.'):
			mylist.append(s.strip())
    print "list made"   



