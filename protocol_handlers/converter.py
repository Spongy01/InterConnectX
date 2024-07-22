import xmltodict
import json



def parseSOAP(data):
    soap_dict = xmltodict.parse(data)
    
    return soap_dict