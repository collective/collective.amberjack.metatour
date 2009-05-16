from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from collective.amberjack.metatour import ajmetatourMessageFactory as _

class Iajtour(Interface):
    """Amberjack-Plone Tour's Folder"""
    
    # -*- schema definition goes here -*-
