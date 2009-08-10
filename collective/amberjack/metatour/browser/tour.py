from collective.amberjack.metatour import ajmetatourMessageFactory as _
from collective.amberjack.core.browser import tour


class Tour(tour.TourView):
    """Tour view."""
    def tourId(self):
        return self.context.tourId
        
    def steps(self):
        """Return a dict:
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
    
    def getSteps(self, item):
        return tuple(item.getSteps())

