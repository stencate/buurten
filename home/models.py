from django.db import models

from wagtail.models import Page
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    
    hero_title = RichTextField(blank=True)
    sub_title = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('sub_title')
    ]
