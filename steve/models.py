from django.db import models


class Contribution(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ForeignKey('Image', models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    position = models.BigIntegerField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'contribution'
        managed = False
        ordering = ('position', '-created_at',)


class Employer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey('Image', models.DO_NOTHING)
    url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'employer'
        managed = False
        ordering = ('-created_at',)


class Experience(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    employer = models.ForeignKey('Employer', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'experience'
        managed = False
        ordering = ('-created_at',)


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True, related_name='images')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def url(self):
        return 'http://steve/uploads/image/' + self.path

    class Meta:
        db_table = 'image'
        managed = False
        ordering = ('-created_at',)


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    image = models.ForeignKey('Image', models.DO_NOTHING, blank=True, null=True, related_name='+')
    slug = models.CharField(max_length=255, blank=True, null=True)
    teaser = models.CharField(max_length=255, blank=True, null=True)
    employer = models.ForeignKey('Employer', models.DO_NOTHING, blank=True, null=True)
    position = models.BigIntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    ios = models.CharField(max_length=255, blank=True, null=True)
    android = models.CharField(max_length=255, blank=True, null=True)
    repository = models.ForeignKey('Repository', models.DO_NOTHING, blank=True, null=True)
    draft = models.BooleanField()
    featured = models.BooleanField()
    publish_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'project'
        managed = False
        ordering = ('position', '-publish_at',)


class ProjectContribution(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    contribution = models.ForeignKey('Contribution', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        db_table = 'project_contribution'
        managed = False
        unique_together = (('project', 'contribution', 'user'),)


class ProjectSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey('Project', models.DO_NOTHING)
    skill = models.ForeignKey('Skill', models.DO_NOTHING)

    class Meta:
        db_table = 'project_skill'
        managed = False


class Quote(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    uri = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    position = models.BigIntegerField(unique=True, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'quote'
        managed = False
        ordering = ('position', '-created_at',)


class Repository(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    watchers = models.BigIntegerField()
    forks = models.BigIntegerField()
    has_downloads = models.IntegerField()
    fork = models.IntegerField()
    has_wiki = models.IntegerField()
    has_issues = models.IntegerField()
    open_issues = models.BigIntegerField()
    size = models.BigIntegerField()
    private = models.IntegerField()
    pushed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'repository'
        managed = False
        ordering = ('-created_at',)


class Set(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    position = models.BigIntegerField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'set'
        managed = False
        ordering = ('position', '-created_at',)


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=128)
    description = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    followers_count = models.BigIntegerField()
    friends_count = models.BigIntegerField()
    statuses_count = models.BigIntegerField()
    is_active = models.IntegerField(blank=True, null=True)
    is_super_admin = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'user'
        managed = False
        ordering = ('-created_at',)


class Shot(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    width = models.BigIntegerField()
    height = models.BigIntegerField()
    likes_count = models.BigIntegerField()
    rebound_source_id = models.BigIntegerField(blank=True, null=True)
    rebounds_count = models.BigIntegerField()
    image_teaser_url = models.CharField(max_length=255)
    views_count = models.BigIntegerField()
    comments_count = models.BigIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'shot'
        managed = False
        ordering = ('-created_at',)


class Skill(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ForeignKey('Image', models.DO_NOTHING)
    set = models.ForeignKey('Set', models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    position = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'skill'
        managed = False
        ordering = ('position', '-created_at',)


class Track(models.Model):
    id = models.BigIntegerField(primary_key=True)
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=255)
    image_small = models.CharField(max_length=255)
    image_medium = models.CharField(max_length=255)
    image_large = models.CharField(max_length=255, blank=True, null=True)
    image_extra_large = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'track'
        managed = False
        ordering = ('-created_at',)


class Tweet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    text = models.CharField(max_length=140)
    html = models.TextField()
    uri = models.CharField(max_length=255)
    reply_id = models.BigIntegerField(blank=True, null=True)
    reply_user_id = models.BigIntegerField(blank=True, null=True)
    reply_username = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=2)
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'tweet'
        managed = False
        ordering = ('-created_at',)
