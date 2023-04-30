import xml.etree.ElementTree as ET
from xml.etree import cElementTree as ElementTree

def dict_to_soap(dictionary):
    # Create the SOAP envelope
    envelope = ET.Element('soap:Envelope')
    envelope.set('xmlns:soap', 'http://schemas.xmlsoap.org/soap/envelope/')
    envelope.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    envelope.set('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema')

    # Create the SOAP body and add it to the envelope
    body = ET.SubElement(envelope, 'soap:Body')

    # Convert the dictionary to XML and add it to the body
    dict_to_xml(dictionary, body)

    # Convert the envelope to a string and return it
    return ET.tostring(envelope, encoding='unicode', method='xml')


def dict_to_xml(dictionary, parent):
    # Iterate over the dictionary items
    for key, value in dictionary.items():
        # Create a new element for the key
        key_element = ET.SubElement(parent, key)

        # Check if the value is a dictionary
        if isinstance(value, dict):
            # If it is, call this function recursively on the value
            dict_to_xml(value, key_element)
        else:
            # Otherwise, set the text of the element to the value
            key_element.text = str(value)



class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class XmlDictConfig(dict):
    '''
    Example usage:

    >>> tree = ElementTree.parse('your_file.xml')
    >>> root = tree.getroot()
    >>> xmldict = XmlDictConfig(root)

    Or, if you want to use an XML string:

    >>> root = ElementTree.XML(xml_string)
    >>> xmldict = XmlDictConfig(root)

    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if element:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})


def xml_to_dict(xml):
    root = ElementTree.XML(xml)
    xmldict = XmlDictConfig(root)
    return xmldict