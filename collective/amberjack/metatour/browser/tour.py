from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.amberjack.metatour import ajmetatourMessageFactory as _

from collective.amberjack.core.browser import tour

class ITour(Interface):
    """
    the Tour interface
    """


class Tour(tour.TourView):
    """
    tour view
    """
    implements(ITour)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.ajsteps = list()
    
    def id(self):
        return self.context.tourId
        
    def steps(self):
        """returns a dict:
        {
        url: ..., 
        title: ..., 
        text: ..., 
        steps: ((description, idstep, selector, text), ...)}
        """
        output = list()
        for item in self.context.listFolderContents():
            url = item.getUrl()
            if url.startswith('/') or url=='':
                url = self.portal() + url
            else:
                url = self.portal() + '/' + url
            d = {
                'url':  url,
                'title': item.title,
                'text': item.getText(),
                'steps': self._highlight(self.getSteps(item)),
                'xpath': item.getXpath(),
                'xcontent': item.getXcontent(),
                }
            output.append(d)

        return output

    def _highlight(self, steps):        
        return steps
        
    def getStepNumber(self, step):
        """
        adds the step to the ajsteps tuple and returns its position
        """
        if not step in self.ajsteps:
            self.ajsteps.append(step)
        
        return self.ajsteps.index(step) + 1
            
    def getSteps(self, item):
        sspan = '<span class="ajHighlight">'
        espan = '</span>'
        steps = list()
        for step in item.getSteps():
            step['description'] = step['description'].replace('[', sspan).replace(']', espan)
            steps.append(step)
        return tuple(steps)
        
    
    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')
    
