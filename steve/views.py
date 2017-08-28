import feedparser
from rest_framework import viewsets
from rest_framework.response import Response
from steve import models, serializers


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        feed = feedparser.parse('https://blog.steve.ly/feed/')
        return Response(feed.entries[:5])


class EmployerViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Employer
    queryset = model.objects.all()
    serializer_class = serializers.EmployerSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Experience
    queryset = model.objects.all()
    serializer_class = serializers.ExperienceSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Project
    queryset = model.objects.all()
    serializer_class = serializers.ProjectSerializer


class ProjectContributionViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.ProjectContribution
    queryset = model.objects.all()
    serializer_class = serializers.ProjectContributionSerializer


class ProjectSkillViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.ProjectSkill
    queryset = model.objects.all()
    serializer_class = serializers.ProjectSkillSerializer


class QuoteViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Quote
    queryset = model.objects.all()
    serializer_class = serializers.QuoteSerializer


class RepositoryViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Repository
    queryset = model.objects.all()
    serializer_class = serializers.RepositorySerializer


class SetViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Set
    queryset = model.objects.all()
    serializer_class = serializers.SetSerializer


class ShotViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Shot
    queryset = model.objects.all()
    serializer_class = serializers.ShotSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Skill
    queryset = model.objects.all()
    serializer_class = serializers.SkillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            queryset = queryset.filter(set__slug=self.request.GET['set'])
        except KeyError:
            pass
        return queryset


class SummaryViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response([
            dict(
                id='coworkations',
                name='Coworkations',
                description='<span>Founder &amp; Platform Lead 2017</span>',
                image='https://images.steve.ly/images/coworkations.png',
                url='https://coworkations.co',
                content="""
                    <p>
                        Coworkations lets you book the best remote working retreats for
                        digital nomads. We index, review and rank workations like
                        <a href="https://coworkations.co/hacker-paradise" rel="nofollow">Hacker Paradise</a>,
                        <a href="https://coworkations.co/remote-year" rel="nofollow">Remote Year</a>
                        and
                        <a href="https://coworkations.co/we-roam" rel="nofollow">We Roam</a>.
                    </p>
                """,
                style='.content--coworkations a{color:#166CCB;border-color:#166CCB;}',
            ),
            dict(
                id='hanzo',
                name='Hanzo Archives',
                description='Platform Lead <span>2014 &ndash; 2016</span>',
                image='https://images.steve.ly/images/hanzo.png',
                url='https://www.hanzo.co',
                content="""
                    <p>
                        Hanzo specialise in building cutting edge web archiving technology,
                        I worked with Hanzo and Simpleweb to build their
                        <a href="https://portal.hanzoarchives.com" rel="nofollow">web app</a> and
                        <a href="https://portal.hanzoarchives.com/api/docs" rel="nofollow">API</a>
                        to give their customers better insight into what has been captured
                        as well as various web archiving tech &ndash; including new crawling strategies,
                        playback methods, change analysis and differential comparison.
                    </p>
                """,
                style='.content--hanzo a{color:#3B8425;border-color:#3B8425;}',
            ),
            dict(
                id='simpleweb',
                name='Simpleweb',
                description='Software Engineer <span>2013 &ndash; 2016</span>',
                image='https://images.steve.ly/images/simpleweb.png',
                url='https://simpleweb.co.uk',
                content="""
                    <p>
                        Since 2013 I worked with some great people at
                        <a href="https://simpleweb.co.uk" rel="nofollow">Simpleweb</a>,
                        specialising in building SaaS
                        products for startups, including
                        <a href="http://amlchecker.com" rel="nofollow">AMLchecker</a>,
                        <a href="https://contactzilla.com" rel="nofollow">Contactzilla</a>,
                        <a href="https://surveywizard.bpglobal.com" rel="nofollow">SurveyWizard</a>
                        and
                        working with
                        <a href="https://www.hanzo.co" rel="nofollow">Hanzo Archives</a>.
                    </p>
                """,
                style='.content--simpleweb a{color:#e43c22;border-color:#e43c22;}',
            ),
            dict(
                id='phpsw',
                name='PHPSW',
                description='Organizer <span>2013 &ndash; 2015</span>',
                image='https://images.steve.ly/images/phpsw.png',
                url='https://phpsw.uk',
                content="""
                    <p>
                        In 2013 I took over the PHP South West UK user group in Bristol,
                        organizing monthly talk nights and growing it over 2 years to
                        become one of the most regularly attended in the country.
                    </p>
                """,
                style='.content--phpsw a{color:#166CCB;border-color:#166CCB;}',
            ),
            dict(
                id='railsgirls',
                name='Rails Girls',
                description='Coach March &amp; November 2014',
                image='https://images.steve.ly/images/railsgirls.png',
                url='http://railsgirls.com',
                content="""
                    <p>
                        Rails Girls is a global, non-profit volunteer community, whose
                        aim is to give tools and a community for women to understand
                        technology and to build their ideas.
                    </p>
                """,
                style='.content--railsgirls a{color:#e72a24;border-color:#e72a24;}',
            ),
            dict(
                id='wiredmedia',
                name='Wired Media',
                description='Senior Developer <span>2010 &ndash; 2013</span>',
                image='https://images.steve.ly/images/wiredmedia.png',
                url='https://www.wiredmedia.co.uk/ecommerce',
                content="""
                    <p>
                        As technical lead I headed up various strategies including re-envisaging
                        the company\'s ecommerce offerings with a Symfony2-based solution
                        and recruiting and training junior developers.
                    </p>

                    <p>
                        Some of the things I built included:
                        <a href="http://www.easier.com" rel="nofollow">Easier</a>,
                        <a href="http://www.signworldlearn.com" rel="nofollow">Signworld</a>,
                        <a href="https://www.fleurofengland.com" rel="nofollow">Fleur of England</a>
                        &amp;
                        <a href="http://www.bbisolutions.com" rel="nofollow">BBI Solutions</a>.
                    </p>
                """,
                style='.content--wiredmedia a{color:#3B8425;border-color:#3B8425;}',
            ),
        ])


class TrackViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Track
    queryset = model.objects.all()
    serializer_class = serializers.TrackSerializer


class TweetViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.Tweet
    queryset = model.objects.all()
    serializer_class = serializers.TweetSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    model = models.User
    lookup_field = 'username'
    queryset = model.objects.all()
    serializer_class = serializers.UserSerializer
