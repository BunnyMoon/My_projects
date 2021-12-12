##################################################
#Author:Kefa
#Date: 12/12/2021 
#Task:Create xml-file
##################################################

import xml.etree.ElementTree as ET

class XmlTreeHelper:
    def add_tags_with_text(self, parent,tags):
        elements = []
        for tag in tags:
            element = ET.SubElement(parent, tag)
            element.text = tags[tag]
            elements.append(element)
          
        return elements

root = ET.Element('shop')

category = ET.SubElement(root, 'category', {'name' : 'Vegan Products'})

product_1 = ET.SubElement(category, 'tproduct', {'name' : 'Good morning Sunshine'})
product_2 = ET.SubElement(category, 'tproduct', {'name' : 'Spagetti Veganietti'})
product_3 = ET.SubElement(category, 'tproduct', {'name' : 'Fantastic Almond Milk'})

xml_tree_helper =  XmlTreeHelper()
xml_tree_helper.add_tags_with_text(product_1, {
    'type' : 'cereals',
    'producer': 'Foods Limited',
    'price' : '9.90',
    'currency' : 'USD'
})

xml_tree_helper.add_tags_with_text(product_2,{
    'type' : 'pasts',
   'producer': 'Programmer Eat Pasta GMBH',
    'price' : '14.49',
    'currency' : 'EUR'
})

xml_tree_helper.add_tags_with_text(product_3,{
    'type' : 'pasts',
   'producer': 'Fantastic Almond Milk',
    'price' : '19.75',
    'currency' : 'USD'
})

#ET.dump (root)

tree = ET.ElementTree(root)
tree.write('shop.xml', 'UTF-8', True)