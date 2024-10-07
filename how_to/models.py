from django.db import models

from wagtail.models import Page
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.

class HowTo(Page):

    hhw_titel = models.CharField(blank=True, max_length=255, verbose_name='HHW Paragraaf titel')
    hhw_paragraaf = RichTextField(blank=True, verbose_name="Hoe het werkt")

    content_panels = Page.content_panels + [
        FieldPanel('hhw_titel'),
        FieldPanel('hhw_paragraaf'),
    ]

