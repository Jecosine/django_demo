from django.shortcuts import HttpResponse
import json
def test(request):
  d = {'status': 200, 'message': 'fuck!'}
  return HttpResponse(json.dumps(d))