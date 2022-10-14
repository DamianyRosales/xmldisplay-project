from users.models import Tab
import  xml.etree.ElementTree as xmltree
from xml.dom import minidom
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response
from .serializers import TabSerializer

# Create your views here.

save_path_file = "file.xml"

class My_view(APIView):

    def get(self, request):
        root = xmltree.Element('Tabs')
        current_year=0
        for i in Tab.objects.all():
            if current_year != i.year:
                current_year = i.year
                yy = 'year'+str(current_year)
                year = xmltree.Element(yy)
                root.append(year)

            tab_month = xmltree.SubElement(year, str(i.month))

            tab_food = xmltree.SubElement(tab_month, 'FOOD')
            tab_food.text = str(i.food)

            tab_brewery = xmltree.SubElement(tab_month, 'BREWERY')
            tab_brewery.text = str(i.brewery)

            tab_chemical_products = xmltree.SubElement(tab_month, 'CHEMICAL_PRODUCTS')
            tab_chemical_products.text = str(i.chemical_products)

            tab_other_manufactures = xmltree.SubElement(tab_month, 'OTHER_MANUFACTURES')
            tab_other_manufactures.text = str(i.other_manufactures)

            tab_textiles_leather = xmltree.SubElement(tab_month, 'TEXTILES_AND_LEATHER')
            tab_textiles_leather.text = str(i.textiles_leather)

            tab_total = xmltree.SubElement(tab_month, 'TOTAL')
            tab_total.text = str(i.total)


        xmlstr = minidom.parseString(xmltree.tostring(root).decode("utf-8")).toprettyxml(indent="\t")

        with open ('file.xml', "w") as files :
            files.write(xmlstr)

        
        #return HttpResponse(open('file.xml').read(), content_type='application/xml')
        html = '<pre>' + open('file.xml').read() + '</pre>'
        return HttpResponse(html)

class MyXMLRenderer(XMLRenderer):
    root_tag_name = 'tabs'
    item_tag_name = 'tabs'

class ViewTab(APIView):
    renderer_classes = [XMLRenderer,]

    def get(self, request):
        tab = Tab.objects.all()
        tab_serializer = TabSerializer(tab, many=True)
        return Response(tab_serializer.data)
