from django.contrib.auth.models import User
from phoenix.api.serializers import POI_Serializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from phoenix.models import Bangalore_POI_Updated
from .serializers import POI_Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from geopy.geocoders import Nominatim

class Poi_list(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    #----------------------------------------------#
    queryset = Bangalore_POI_Updated.objects.all()
    serializer_class = POI_Serializer
    #----------------------------------------------#


class Poi_create(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    #----------------------------------------------#
    queryset = Bangalore_POI_Updated.objects.all()
    serializer_class = POI_Serializer
    #----------------------------------------------#
    def perform_create(self, serializer):
        pro_resour = User.objects.get(id=self.request.user.id)
        serializer.save(pro_resour=pro_resour)

#----------------------------------------------------------------------------------------#

# views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.gis.geos import Point
# from django.contrib.gis.db.models.functions import Distance
# from phoenix.models import Bangalore_POI_Updated
# from .serializers import Parentchild

# class NearestParentObjectsAPI(APIView):
#     def get(self, request):
#         try:
#             # Get latitude and longitude from the request parameters
#             lat = float(request.GET.get('lat'))
#             lon = float(request.GET.get('lon'))

#             # Create a point object using the provided coordinates
#             user_location = Point(lon, lat, srid=4326)

#             # Get the 50 nearest parent objects based on the user's location
#             nearest_parent_objects = Bangalore_POI_Updated.objects.filter(
#                 parent_chi='parent',
#                 build_late__isnull=False,
#                 build_lone__isnull=False,
#             ).annotate(
#                 distance=Distance('location', user_location)
#             ).order_by('distance')[:50]

#             # Serialize the queryset
#             serializer = Parentchild(nearest_parent_objects, many=True)

#             return Response(serializer.data, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from phoenix.models import Bangalore_POI_Updated
from .serializers import Parentchild

# class NearestParentObjectsAPI(APIView):
#     def get(self, request):
#         try:
#             # Get latitude and longitude from the request parameters
#             lat = float(request.GET.get('lat'))
#             lon = float(request.GET.get('lon'))

#             # Create a point object using the provided coordinates
#             user_location = Point(lon, lat, srid=4326)

#             # Get the 50 nearest parent objects based on the user's location
#             nearest_parent_objects = BangalorePoiDataDeleteThisModel.objects.filter(
#                 parent_chi='parent',
#                 build_late__isnull=False,
#                 build_lone__isnull=False,
#             ).annotate(
#                 distance=Distance('geom', user_location, spheroid=True)
#             ).order_by('distance')[:50]

#             # Serialize the queryset
#             serializer = Parentchild(nearest_parent_objects, many=True)

#             return Response(serializer.data, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class NearestParentObjectsAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            # Get latitude and longitude from the request parameters
            lat = float(request.GET.get('lat'))
            lon = float(request.GET.get('lon'))

            # Create a point object using the provided coordinates
            user_location = Point(lon, lat, srid=4326)

            # Get the 50 nearest parent objects based on the user's location
            nearest_parent_objects = Bangalore_POI_Updated.objects.filter(
                parent_chi='PARENT',
                build_late__isnull=False,
                build_lone__isnull=False,
                geom__isnull=False,
            ).annotate(
                distance=Distance('geom', user_location)
            ).order_by('distance')[:50]

            # Serialize the queryset
            serializer = Parentchild(nearest_parent_objects, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        



from .serializers import GeocodeSerializer

class GeocodeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = GeocodeSerializer(data=request.data)
        if serializer.is_valid():
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']

            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.reverse(f"{latitude},{longitude}")

            data = {
                'address': location.address,
                'latitude': location.latitude,
                'longitude': location.longitude,
            }

            return Response(data)
        else:
            return Response(serializer.errors, status=400)