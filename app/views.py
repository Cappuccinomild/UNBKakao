from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def keyboard(request):
    return JsonResponse(
        {
            "type" : "buttons",
            #노래추천 
            "buttons" : ["노래 추천", "우노반 일정"]
        }
    )

@csrf_exempt
def answer(requset):

    json_str = (requset.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']

    if content_name == '노래 추천':

        return JsonResponse({
            'message': {
                'text' : '노래 추천\n양식은 노래제목 - 가수 로 해주세요.'
            },

            'keyboard':{
                'type' : 'buttons',
                'buttons' : ['']
            }
        })

    elif content_name == '우노반 일정':

        return JsonResponse({
            'message': {
                'text' : '노래 추천\n양식은 노래제목 - 가수 로 해주세요.'
            },

            'keyboard':{
                'type' : 'buttons',
                'buttons' : ['']
            }
        })

    else:
        return JsonResponse({
            'message': {
                'text' : '다시 입력해주세요.'
            },

            'keyboard':{
                'type' : 'buttons',
                'buttons' : ["노래 추천", "우노반 일정"]
            }
        })
