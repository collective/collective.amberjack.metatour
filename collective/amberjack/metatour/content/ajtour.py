"""Definition of the ajtour content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from collective.amberjack.metatour import ajmetatourMessageFactory as _
from collective.amberjack.metatour.interfaces import Iajtour
from collective.amberjack.metatour.config import PROJECTNAME


ajtourSchema = folder.ATFolderSchema.copy() + atapi.Schema((
))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

ajtourSchema['title'].storage = atapi.AnnotationStorage()
ajtourSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    ajtourSchema,
    folderish=True,
    moveDiscussion=False
)

class ajtour(folder.ATFolder):
    """Amberjack-Plone Tour's Folder"""
    implements(Iajtour)

    meta_type = "ajtour"
    schema = ajtourSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    _at_rename_after_creation = True
    
atapi.registerType(ajtour, PROJECTNAME)
