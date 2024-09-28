from django.db import models

from wagtail.models import Page
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    
    hero_title = RichTextField(blank=True, verbose_name='Hero sectie titel')
    sub_title = RichTextField(blank=True, verbose_name='Sub titel')

    hhw_titel = models.CharField(blank=True, max_length=255, verbose_name='HHW Paragraaf titel')
    hhw_paragraaf = RichTextField(blank=True, verbose_name="Hoe het werkt")

    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('sub_title'),
        FieldPanel('hhw_titel'),
        FieldPanel('hhw_paragraaf'),
    ]
