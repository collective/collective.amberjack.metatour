"""Definition of the ajstep content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.Archetypes.public import DisplayList

from collective.amberjack.metatour import ajmetatourMessageFactory as _
from collective.amberjack.metatour.interfaces import Iajstep
from collective.amberjack.metatour.config import PROJECTNAME

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn

from collective.amberjack.core.javascript.ajStandardSteps import ajStandardSteps

ajstepSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.TextField(
        'text',
        widget=atapi.RichWidget(
            label=_(u"User's description"),
            description=_(u"Enter a description for the user")
        )
    ),

    atapi.StringField(
        'url',
    ),
    
    atapi.StringField(
        'xpath',
    ),
    
    atapi.StringField(
        'xcontent',
    ),

    DataGridField(
        'steps',
        columns=('description','idStep', 'selector', 'text'),
        allow_empty_rows=False, # Must be false to make auto insert feature perform correctly
        widget=DataGridWidget(
            label=_(u"Steps"),
            description = _(u"Enter:<ol> <li>the description for the user (use [] to <span class='ajHighlight'>highlight</span> parts)</li> <li>the step id</li> <li>an optional selector</li> <li>an optional text used by the step</li> </ol>"),
            auto_insert=False,
            allow_empty_rows=False,
            columns={
                'description': Column(_(u"Description")),
                'idStep' : SelectColumn(_(u"Step"), vocabulary="getStepsVocabulary"),
                'selector' : Column(_(u"A css or xpath selector")),
                'text' : Column(_(u"The text associated with the step"))
            },
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
    
    def getStepsVocabulary(self):
        return DisplayList(
                     ((key, key) for (key, value) in (('None', ''),) + ajStandardSteps)
                     )


atapi.registerType(ajstep, PROJECTNAME)
