import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
# from chatterbot import ChatBot
from aido.chatbot import ChatBot
from chatterbot.ext.django_chatterbot import settings


class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    # chatterbot = ChatBot(**settings.CHATTERBOT)
    chatterbot = ChatBot()

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data['text'])

        # response_data = response.serialize()
        self.chatterbot.text2voice(response)

        return JsonResponse({
            'text': [
                response
            ],
            'audioname': [
                'voice_ss.mp3'
            ]
        }, status=200, safe=False)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
