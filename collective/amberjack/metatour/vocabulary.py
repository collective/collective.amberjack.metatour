from zope.app.schema.vocabulary import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.utils import getToolByName

class AvailableMetatoursVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        portal_catalog = getToolByName(context, 'portal_catalog', None)
        tours = portal_catalog(portal_type='ajtour')
        
        items = [SimpleTerm(value=t.getTourId, token=t.Title) for t in tours]
        return SimpleVocabulary(items)

AvailableMetatoursVocabularyFactory = AvailableMetatoursVocabulary()
