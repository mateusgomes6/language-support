import xml.etree.ElementTree as etree

def parse_decs_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    terms = []
    for descriptor in root.findall('DescriptorRecord'):
        term_element = descriptor.find('DescriptorName')
        term = term_element.text if term_element is not None else None
        terms.append(term)
    return terms