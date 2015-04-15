from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl

import atexit

def index(request):

    # Get ServiceInstanceContent
    si = SmartConnect(host='172.20.10.2',
                      user='root',
                      pwd='vmware')
    if not si:
        return HttpResponse("Hi, guys. I'm sorry for that we can't connect to vcenter.")
    atexit.register(Disconnect, si)
    content = si.RetrieveContent()

    # Look up templates under the specific '__vapor_templates'
    templates = []
    objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                      [vim.Folder],
                                                      True)
    folderList = objView.view
    for folder in folderList:
       if folder.name == '__vapor_templates':
          vmList = folder.childEntity
          templates.extend(vmList)
          break
       else:
          continue 
  
    context = RequestContext(request, {
        'templates': templates    
    })

    template = loader.get_template('template/index.html')
    return HttpResponse(template.render(context))

