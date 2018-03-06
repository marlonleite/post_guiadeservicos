# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib.request as ur
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def index(request):
    # api_url = 'http://www.servicos.al.gov.br/api/services.json?q="' + key + '"'
    api_url = 'http://www.servicos.al.gov.br/api/services.json'
    res = ur.urlopen(api_url).read().decode('utf-8')
    data = json.loads(res)
    data = data['services']
    new_data = []
    for i, d in enumerate(data):
        if d['id'] == '56dd60658c36c73000000000' or d['id'] == '56dd637c8c36c73138000000':
            new_data.append(d)

    if request.method == 'GET':
        if new_data:
            return Response(new_data)

    elif request.method == 'POST':
        if new_data:
            return Response(new_data, status=status.HTTP_200_OK)
        return Response('Method not allowed', status=status.HTTP_400_BAD_REQUEST)
