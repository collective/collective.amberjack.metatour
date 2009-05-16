from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from collective.amberjack.metatour import ajmetatourMessageFactory as _

class Iajstep(Interface):
    """Amberjack-Plone Tour's Step"""
    
    # -*- schema definition goes here -*-
