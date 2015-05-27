from django.db import modelsfrom django_extensions.db.fields import AutoSlugFieldclass Application(models.Model):    # Fields    created = models.DateTimeField(auto_now_add=True, editable=False)    last_updated = models.DateTimeField(auto_now=True, editable=False)    name = models.CharField(max_length=255)    gender = models.CharField(max_length=10)    birthdate = models.DateTimeField()    timezone = models.IntegerField()    longitude = models.DecimalField(max_digits=11, decimal_places=7)    latitude = models.DecimalField(max_digits=11, decimal_places=7)    character_name = models.CharField(max_length=255)    character_class = models.CharField(max_length=255)    character_level = models.IntegerField()    technical_expertise = models.CharField(max_length=30)    technical_skills = models.TextField()    playtime = models.IntegerField()    player_type = models.CharField(max_length=30)    game_detailed_history = models.TextField()    why_join = models.TextField()    game_officer_history = models.TextField()    # Relationship Fields    answers = models.ManyToManyField('applications.ApplicationQuestion',)    class Meta:        ordering = ('-created',)    def __unicode__(self):        return u'%s' % self.idclass ApplicationQuestion(models.Model):    # Fields    question = models.CharField(max_length=255)    slug = AutoSlugField(populate_from='question', blank=True)    created = models.DateTimeField(auto_now_add=True, editable=False)    last_updated = models.DateTimeField(auto_now=True, editable=False)    # Relationship Fields    chapter = models.ForeignKey('games.Chapter',)    class Meta:        ordering = ('-created',)    def __unicode__(self):        return u'%s' % self.slugclass ApplicationAnswer(models.Model):    # Fields    answer = models.TextField()    created = models.DateTimeField(auto_now_add=True, editable=False)    # Relationship Fields    question = models.OneToOneField('applications.ApplicationQuestion',)    class Meta:        ordering = ('-created',)    def __unicode__(self):        return u'%s' % self.id