from django.conf import settings
from django.conf.urls import include, url
from steve import routers, views


router = routers.Router(trailing_slash=False)

router.register(r'articles', views.ArticleViewSet, 'Article')
router.register(r'employers', views.EmployerViewSet, 'Employer')
router.register(r'experiences', views.ExperienceViewSet, 'Experience')
router.register(r'projects', views.ProjectViewSet, 'Project')
router.register(r'quotes', views.QuoteViewSet, 'Quote')
router.register(r'repositories', views.RepositoryViewSet, 'Repository')
router.register(r'sets', views.SetViewSet, 'Set')
router.register(r'users', views.UserViewSet, 'User')
router.register(r'shots', views.ShotViewSet, 'Shot')
router.register(r'skills', views.SkillViewSet, 'Skill')
router.register(r'summary', views.SummaryViewSet, 'Summary')
router.register(r'tracks', views.TrackViewSet, 'Track')
router.register(r'tweets', views.TweetViewSet, 'Tweet')

urlpatterns = router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
