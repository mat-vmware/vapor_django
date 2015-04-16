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

def launch(request, template_name):
    context = RequestContext(request, {
        'image': template_name
    })
    template = loader.get_template('template/launch.html')
    return HttpResponse(template.render(context))

def vm_new(request):
    image = request.POST['image']
    vmName = request.POST['name']

    # Get ServiceInstanceContent
    si = SmartConnect(host='172.20.10.2',
                      user='root',
                      pwd='vmware')
    if not si:
        return HttpResponse("Hi, guys. I'm sorry for that we can't connect to vcenter.")
    atexit.register(Disconnect, si)
    content = si.RetrieveContent()

    objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                      [vim.VirtualMachine],
                                                      True)
    vmList = objView.view
    objView.Destroy()

    # Get all vms under the specific '__vapor_vms'
    objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                      [vim.Folder],
                                                      True)
    folderList = objView.view
    objView.Destroy()
    
    def clone(vm):
       def cloneto(folder):
          print("Clone VM %s to folder %s" % (vm, folder))

          relocateSpec = vim.vm.RelocateSpec()

          cloneSpec = vim.vm.CloneSpec()
          cloneSpec.location = relocateSpec

          return vm.Clone(folder, vmName, cloneSpec)

       return [cloneto(folder) for folder in folderList if folder.name == '__vapor_vms']

    tasks = [clone(vm) for vm in vmList if vm.name == image]

    context = RequestContext(request, {
    })
    template = loader.get_template('template/vm_new.html')
    return HttpResponse(template.render(context))

def vm_list(request):
    # Get ServiceInstanceContent
    si = SmartConnect(host='172.20.10.2',
                      user='root',
                      pwd='vmware')
    if not si:
        return HttpResponse("Hi, guys. I'm sorry for that we can't connect to vcenter.")
    atexit.register(Disconnect, si)
    content = si.RetrieveContent()

    # Get all vms under the specific '__vapor_vms'
    vms = []
    objView = content.viewManager.CreateContainerView(content.rootFolder,
                                                      [vim.Folder],
                                                      True)
    folderList = objView.view
    for folder in folderList:
       if folder.name == '__vapor_vms':
          vmList = folder.childEntity
          vms.extend(vmList)
          break
       else:
          continue 
 
    context = RequestContext(request, {
        'vms': vms
    })
    template = loader.get_template('template/vm_list.html')
    return HttpResponse(template.render(context))

