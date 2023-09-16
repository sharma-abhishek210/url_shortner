from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializer import URLSerializer
import random
import string
from django.utils import timezone

SHORT_URL_LENGTH = 7

class URLShortener(APIView):
    def post(self, request):
        original_url = request.data.get('original_url')
        if not original_url:
            return Response({'error': 'original_url is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = URL.objects.filter(original_url=original_url)
        if url:
            return Response(URLSerializer(url[0]).data)
        else:
            url = URL.objects.create(original_url=original_url)   
        short_url = self.generate_short_url()
        url.short_url = short_url
        url.save()
        serializer = URLSerializer(url)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choice(characters) for i in range(SHORT_URL_LENGTH))
            if not URL.objects.filter(short_url=short_url).exists():
                break
        return f'http://localhost:8000/{short_url}'

    def get(self, request, short_url):
        try:
            shortUrl = f'http://localhost:8000/{short_url}'
            url = URL.objects.get(short_url=shortUrl)
            if url.expiry_time < timezone.now():
                return Response({'error': 'This URL has expired'}, status=status.HTTP_400_BAD_REQUEST)
            url.click_count += 1
            url.save()
            serializer = URLSerializer(url)
            return Response(serializer.data, status=status.HTTP_302_FOUND, headers={'Location': url.original_url})
        except URL.DoesNotExist:
            return Response({'error': 'Invalid URL'}, status=status.HTTP_400_BAD_REQUEST)