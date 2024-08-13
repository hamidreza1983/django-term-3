from rest_framework import serializers
from services.models import Services, Team, Category, Skills
from ...models import Category, Options

# class ServiceSerializer(serializers.Serializer):

#     name = serializers.CharField(max_length=100)
#     image = serializers.ImageField()
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField(max_length=100)


class TeamSerializer(serializers.ModelSerializer):
    
    class Meta : 
        model = Team
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta : 
        model = Category
        fields = "__all__"

class SkillsSerializer(serializers.ModelSerializer):
    
    class Meta : 
        model = Skills
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):

    #name = serializers.ReadOnlyField()
    name = serializers.SerializerMethodField(method_name="cat_name")
    created_at = serializers.SerializerMethodField(method_name="year")
    # category = serializers.SlugRelatedField(many=True, queryset=Category.objects.all(),slug_field="title")
    # generals = serializers.SlugRelatedField(many=True, queryset=Options.objects.all(), slug_field="title")
    detail_link = serializers.SerializerMethodField(method_name="detail")
    
    class Meta : 
        model = Services
        fields = ['name', 'content', 'title', 'description', 'price', 'category', "generals", "created_at", "detail_link"]
        read_only_fields = ["name"]

    def cat_name(self, instanse):
        return str(instanse.name).upper()
    
    def year(self, instanse):
        return (str(instanse.created_at).split("-"))[0]
    
    def detail(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.id)
    

    # def to_representation(self, instance):
    #     rep =  super().to_representation(instance)
    #     rep["category"] = [cat.title for cat in instance.category.all()]
    #     return rep
    
    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        request = self.context.get("request")
        kwargs = request.parser_context.get("kwargs")

        if kwargs.get("pk"):
            rep["category"]= [cat.title for cat in instance.category.all()]
            
        else:
            rep.pop("category")
        return rep






