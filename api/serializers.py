from rest_framework import serializers
class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    origname = serializers.CharField()
    code = serializers.CharField()
    uid = serializers.UUIDField()
    type_uid = serializers.IntegerField()
    parent_uid = serializers.UUIDField()