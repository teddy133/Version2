from rest_framework import serializers
from models import Games
from models import Members
from models import StoreCategory
from models import Store
from models import Manager
from models import Region
import views


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    joiners = serializers.HyperlinkedRelatedField(view_name='members-detail', required=False, read_only=True, many=True)

    class Meta:
        model= Games
        fields = (
        'url',
        'name',
        'joiners',
        )

class MembersSerializer(serializers.HyperlinkedModelSerializer):
    GamesJoined = GamesSerializer(many=True)

    class Meta:
        model = Members
        fields = (
        'url',
        'name',
        'time',
        'GamesJoined',
        )

    # def create(self, validated_data):
    #     games_inserted = validated_data.pop('GamesJoined')
    #     game = Games.objects.create(**games_inserted)
    #     return game

    def create(self, validated_data):
        games_inserted = validated_data.pop('GamesJoined')
        member = Members.objects.create(**validated_data)

        for game in games_inserted:
            game, created = Games.objects.get_or_create(name=game['name'])
            member.GamesJoined.add(game)
        return member


    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('tracks')
    #     album = Album.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album


    # def create(self, validated_data):
    #     ingredients_data = validated_data.pop('ingredients')
    #     recipe = Recipe.objects.create(**validated_data)
    #
    #     for ingredient in ingredients_data:
    #         ingredient, created = Ingredient.objects.get_or_create(name=ingredient['name'])
    #         recipe.ingredients.add(ingredient)
    #     return recipe

class StoreCategorySerializer(serializers.HyperlinkedModelSerializer):
	stores = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='store-detail')

	class Meta:
		model = StoreCategory
		fields = (
		'url',
		'pk',
		'name',
		'stores')

class StoreSerializer(serializers.HyperlinkedModelSerializer):
	# Display the category name
	store_category = serializers.SlugRelatedField(queryset=StoreCategory.objects.all(),
		slug_field='name')

	class Meta:
		model = Store
		fields = (
			'url',
			'name',
			'store_category',
			'been_audited',
			'inserted_timestamp')


class RegionSerializer(serializers.HyperlinkedModelSerializer):
	# Display all the details for the related drone
	store = StoreSerializer()

	class Meta:
		model = Region
		fields = (
			'url',
			'pk',
			'store_of_month',
			'established',
			'store')


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
	regions = RegionSerializer(many=True, read_only=True)
	gender = serializers.ChoiceField(choices=Manager.GENDER_CHOICES)
	gender_description = serializers.CharField(
		source='get_gender_display',
		read_only=True)

	class Meta:
		model = Manager
		fields = (
			'url',
			'name',
			'gender',
			'gender_description',
			'timestamp',
			'regions')


class ManagerRegionSerializer(serializers.ModelSerializer):
	# Display the pilot's name
	manager = serializers.SlugRelatedField(queryset=Manager.objects.all(), slug_field='name')
	# Display the drone's name
	store = serializers.SlugRelatedField(queryset=Store.objects.all(), slug_field='name')

	class Meta:
		model = Region
		fields = (
			'url',
			'pk',
			'store_of_month',
			'established',
			'manager',
			'store')
