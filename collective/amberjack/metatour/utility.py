from collective.amberjack.core.interfaces import ITourDefinition
from collective.amberjack.core.interfaces import ITourRetriever
from Products.CMFCore.utils import getToolByName
from zope.interface import implements


class TourRetriever(object):
    implements(ITourRetriever)

    def getTours(self, context=None):
        portal_catalog = getToolByName(context, 'portal_catalog', None)
        brains = portal_catalog(portal_type='ajtour')
        return [(b.id, b.Title) for b in brains]

    def getTour(self, tour_id, context=None):
        portal_catalog = getToolByName(context, 'portal_catalog', None)
        brains = portal_catalog(portal_type='ajtour', id=tour_id)
        if brains:
            return ITourDefinition(brains[0].getObject())
        else:
            return None
