"""Definition of the ajstep content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from collective.amberjack.metatour import ajmetatourMessageFactory as _
from collective.amberjack.metatour.interfaces import Iajstep
from collective.amberjack.metatour.config import PROJECTNAME

ajstepSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        'type_step',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Step Type"),
            description=_(u"Field description"),
        ),
        required=True,
    ),


    atapi.StringField(
        'jq_selector',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Jquery Selector"),
            description=_(u"Field description"),
        ),
    ),


    atapi.StringField(
        'value_step',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Step Value"),
            description=_(u"Field description"),
        ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ajstepSchema['title'].storage = atapi.AnnotationStorage()
ajstepSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ajstepSchema, moveDiscussion=False)

class ajstep(base.ATCTContent):
    """Amberjack-Plone Tour's Step"""
    implements(Iajstep)

    meta_type = "ajstep"
    schema = ajstepSchema
    _at_rename_after_creation = True

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    type_step = atapi.ATFieldProperty('type_step')
    jq_selector = atapi.ATFieldProperty('jq_selector')
    value_step = atapi.ATFieldProperty('value_step')

atapi.registerType(ajstep, PROJECTNAME)
