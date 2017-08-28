from rest_framework import serializers
from steve import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = [
            'title',
            'url',
            'slug',
            'caption',
        ]


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contribution
        exclude = ('id', 'position',)


class EmployerSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = models.Employer
        exclude = ('id',)


class ExperienceSerializer(serializers.ModelSerializer):
    employer = EmployerSerializer()

    class Meta:
        model = models.Experience
        exclude = ('id',)


class ProjectSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = models.Project
        exclude = ('id', 'position',)


class ProjectContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectContribution
        exclude = ('id',)


class ProjectSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectSkill
        exclude = ('id',)


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quote
        exclude = ('id', 'position',)


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Repository
        exclude = ('id',)


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Set
        exclude = ('id', 'position',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('id',)


class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shot
        exclude = ('id',)


class SkillSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    set = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = models.Skill
        exclude = ('id', 'position',)


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        exclude = ('id',)


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tweet
        exclude = ('id',)
