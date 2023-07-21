from rest_framework import serializers
from phoenix.models import Bangalore_POI_Updated
from rest_framework_gis.serializers import GeoFeatureModelSerializer

#SERIALIZER
class POI_Serializer(GeoFeatureModelSerializer):
    '''serializer'''
    class Meta:
        model = Bangalore_POI_Updated
        fields = '__all__'
        geo_field = 'geom'


#------------------------------------------------------------------------------------------------#

# serializers.py
from rest_framework import serializers

class Parentchild(serializers.ModelSerializer):
    class Meta:
        model = Bangalore_POI_Updated
        fields = ['gid','poi_id','poi_name','parent_chi', 'build_late', 'build_lone']


class GeocodeSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()