from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from hook_receiver.mcrobofaceutils import smile, wink

import requests

@csrf_exempt
def hook(request):
    if request.method == "POST" and request.POST['token'] == settings.SLACK_KEY:
        post_data = { 'text': 'You got it, boss!' }
        requests.post(request.POST['response_url'], json=post_data)
        wink()
        print(request.POST)

    return HttpResponse("Beep boop!")
