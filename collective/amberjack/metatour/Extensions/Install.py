def addToFactoryTool(self, out):
     print >> out, 'portal_factory modifications started.'
     
     ftool = getToolByName(self, 'portal_factory')
     
     if ftool:
          portal_factory_types = ftool.getFactoryTypes().keys()
               
     for portalType in [ typeDict['portal_type'] for typeDict in listTypes(PROJECTNAME) ]:
          if portalType not in portal_factory_types:
               portal_factory_types.append(portalType)
               ftool.manage_setPortalFactoryTypes(listOfTypeIds=portal_factory_types)
               print >> out, '    %s now uses portal_factory' % portalType
                    
     print >> out, 'portal_factory modifications done.'
