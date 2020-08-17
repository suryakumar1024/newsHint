from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.scraper import Scraper
from datasource.serializers import NewsSerializer


class NewsCrawler(APIView):

    def get(self, request) -> dict:
        result = Scraper.run_scraper(
            self, url="http://www.bbc.com/travel/story/20200812-the-right-way-to-make-ratatouille")
        news_array = result['news_array']
        news_array_collected = news_array.categories
        botserializer_obj = NewsSerializer(data=news_array_collected, many=True)
        if botserializer_obj.is_valid():
            botserializer_obj.save()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
