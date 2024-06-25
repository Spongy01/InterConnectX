# InterConnectX: Empowering Interoperability between Systems

A backend middleware application to power bi-directional integration between two separate systems supporting REST and SOAP  communication with compatibility between them. 
Compatibility can be throttles, data transformation, security or protocols.

# Problem it solves
1. Integration Complexity: It eliminates the need for complex custom integrations and enables efficient data exchange.
2. Protocol Interoperability: REST and SOAP are different communication protocols, and integrating systems using these protocols can be challenging. The middleware acts as a bridge, enabling the two systems to communicate and exchange data seamlessly.
3. Data Transformation: The middleware facilitates the transformation of data formats between REST and SOAP, ensuring compatibility between the systems. It handles the mapping and conversion of data structures, making it easier for the systems to understand and process the exchanged information.
4. Security and Authentication: It enforces security protocols to protect sensitive data during transmission, maintaining the integrity and confidentiality of the exchanged information.

# Challenges we ran into

1. Understanding the requirements: At the beginning of the conversation, we needed to clarify the requirements and goals of the project to ensure that we were on the same page.
2. Module installation and import errors: We encountered issues with installing and importing certain Python modules, such as requests and xmltodict, which required troubleshooting and debugging.
3. SOAP XML parsing: We faced challenges in parsing SOAP XML data and converting it to Python dictionaries, which required using the xml.etree.ElementTree and xmltodict modules.
4. Debugging and error handling: Throughout the conversation, we encountered various errors and issues that required debugging and error handling to resolve.

# Technologies we used
* Django
* JSON
* XML
* Python
* Swagger
* ThunderClient
