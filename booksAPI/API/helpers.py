import xml.etree.ElementTree as ET


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

