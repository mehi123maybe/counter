from django.http import HttpResponse
from django.shortcuts import render
import operator
def index(req):
    return render(req, 'index.html')


def count(req):
    fulltext = req.GET['fulltext']
    wordlist = fulltext.split()
    wordcountdict = dict()
    for word in wordlist:
        if word in wordcountdict:
            #icrease
            wordcountdict[word] += 1
        else:
            wordcountdict[word] = 1
    sorted_list = sorted(wordcountdict.items(), key=operator.itemgetter(1), reverse=True)
    return render(req, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'dicts':sorted_list})