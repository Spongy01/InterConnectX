import xmltodict
import json



def parseSOAP(data):
    soap_dict = xmltodict.parse(data)
    
    return soap_dict

def convertJSONtoSOAP(data):
    json_dict = xmltodict.unparse(data)
    return json_dict