# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.core.urlresolvers import reverse
from .fields import ThumbnailImageField
from django.contrib.auth.models import User
from django.utils.text import slugify
from hitcount.models import HitCount, HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.


@python_2_unicode_compatible
class HoneyTip(models.Model):
    title = models.CharField('title',max_length=50)
    slug = models.SlugField('SLUG', help_text='one word for title alias.')
    owner = models.ForeignKey(User, null=True)
    titleimage = ThumbnailImageField('대표 사진',upload_to='honeytip/titleiamge/%y/%m/%d')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    scraps = models.IntegerField(default=0)
    app_name=models.CharField(default='HoneyTip',max_length=20,  null=True)

    class Meta:
        verbose_name = 'honeytip'
        verbose_name_plural = 'honeytips'
        db_table  = 'honeytip_posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('honeytip:honeytip_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
   
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super(HoneyTip, self).save(*args, **kwargs)

 
@python_2_unicode_compatible
class Contents(models.Model):
    honeycontents = models.ForeignKey(HoneyTip, on_delete=models.CASCADE)
    honeyimage = ThumbnailImageField('honeyimage',upload_to='honeytip/content/%y/%m/%d')
    honeydescription = models.TextField('honeydescription', blank=True)
   
    def __str__(self):
        return self.honeydescription