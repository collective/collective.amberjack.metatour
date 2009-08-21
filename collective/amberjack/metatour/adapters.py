from zope.component import adapts
from zope.interface import implements

from collective.amberjack.core.interfaces import ITourDefinition
from collective.amberjack.metatour.interfaces import Iajtour

class TourAdapter(object):
    implements(ITourDefinition)
    adapts(Iajtour)

    def __init__(self, context):
        self.context = context

    @property
    def tourId(self):
        """Return the tourId."""
        return self.context.getId()

    @property
    def title(self):
        """Return the title."""
        return self.context.title

    @property
    def steps(self):
        """Return a dict:
        {'url': 'url',
         'xpath': 'xpath expression',
         'xcontent': 'xcontent',
         'title': 'title',
         'text': 'text',
         'steps': ((description, idStep, selector, text), ...)}

        """
        output = []

        for item in self.context.listFolderContents():
            d = {'url':  item.getUrl(),
                 'xpath': item.getXpath(),
                 'xcontent': item.getXcontent(),
                 'title': item.Title(),
                 'text': item.getText(),
                 'steps': item.getSteps()}
            output.append(d)
        
        return output

