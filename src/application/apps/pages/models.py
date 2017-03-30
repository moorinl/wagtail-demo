from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock
from wagtail.wagtailsnippets.models import register_snippet


@register_snippet
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=128)

    panels = [
        FieldPanel('quote'),
        FieldPanel('author'),
    ]

    def __str__(self):
        return self.quote


class QuoteBlock(blocks.StructBlock):
    quote = SnippetChooserBlock(Quote)

    class Meta:
        icon = 'fa-quote-right'
        template = 'blocks/quote.html'


class CarouselSlideBlock(blocks.StructBlock):
    caption = blocks.CharBlock(max_length=32)
    image = ImageChooserBlock()

    class Meta:
        label = 'Slide'


class CarouselBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=64)
    subtitle = blocks.CharBlock(max_length=128)
    slides = blocks.ListBlock(CarouselSlideBlock())

    class Meta:
        label = 'Carousel'
        template = 'blocks/carousel.html'


class CallToActionBlock(blocks.StructBlock):
    call_to_action = blocks.CharBlock(max_length=32)
    page = blocks.PageChooserBlock()

    class Meta:
        label = 'Call to action'
        template = 'blocks/call_to_action.html'


class BannerBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=64)
    image = ImageChooserBlock()

    class Meta:
        label = 'Banner'
        template = 'blocks/banner.html'


class HomePage(Page):
    content_top = StreamField([
        ('demo', blocks.StructBlock([
            ('is_cool', blocks.BooleanBlock()),
        ], template='blocks/demo.html')),
    ])
    content = StreamField([
        ('carousel', CarouselBlock()),
        ('cta', CallToActionBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content_top'),
        StreamFieldPanel('content'),
    ]

    api_fields = ['content']
    parent_page_types = ['wagtailcore.Page']
    subpage_types = ['pages.GenericPage', 'pages.ContactPage']
    template = 'pages/home.html'

    class Meta:
        verbose_name = 'home'


class GenericPage(Page):
    content = StreamField([
        ('quote', QuoteBlock()),
        ('carousel', CarouselBlock()),
        ('cta', CallToActionBlock()),
        ('banners', blocks.ListBlock(
            BannerBlock(), template='blocks/banners.html', icon='fa-picture-o')),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    api_fields = ['content']
    parent_page_types = ['pages.HomePage']
    subpage_types = ['pages.GenericPage', 'pages.ContactPage']
    template = 'pages/generic.html'

    class Meta:
        verbose_name = 'generic'


class ContactPage(Page):
    parent_page_types = ['pages.HomePage', 'pages.GenericPage']
    subpage_types = []
    template = 'pages/contact.html'

    class Meta:
        verbose_name = 'contact'
