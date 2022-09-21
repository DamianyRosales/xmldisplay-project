from users.models import User
import  xml.etree.ElementTree as xmltree
from xml.dom import minidom
from django.http import HttpResponse

# Create your views here.

save_path_file = "file.xml"

def my_view(request):
    
    root = xmltree.Element('Users')
    
    for i in User.objects.all():
        
        user = xmltree.Element('User')
        root.append(user)

        user_id = xmltree.SubElement(user, 'ID')
        user_id.text = str(i.user_id)

        user_email = xmltree.SubElement(user, 'Email')
        user_email.text = str(i.email)

        user_name = xmltree.SubElement(user, 'Name')
        user_name.text = str(i.name)
        
    #tree = xmltree.ElementTree(root)

    xmlstr = minidom.parseString(xmltree.tostring(root)).toprettyxml(indent="\t")
   
    with open ('file.xml', "w") as files :
        files.write(xmlstr)

    #return HttpResponse(open('file.xml').read(), content_type='application/xml')
    html = '<pre>' + open('file.xml').read() + '</pre>'
    return HttpResponse(html)
