import xmltodict


def read_xml(xml_file_location):
    with open("code/interface.xml")as data:
        xml_example = data.read()   
    # print(xml_example)
    xml_dict = xmltodict.parse(xml_example)
    print(xml_dict)
    return xml_dict
    

def write_to_xml(xml_file_location,xml_dict):
    xml_dict["interface"]["ipv4"]["address"]["ip"]="10.1.1.1"
    with open(xml_file_location,"w")as data:
        data.write(xmltodict.unparse(xml_dict,pretty=True))
    print(xml_dict)


def main():
    xml_file_location="code/interface.xml"
    xml_dict=read_xml(xml_file_location)
    print(xmltodict.unparse(xml_dict,pretty=True))
    write_to_xml(xml_file_location,xml_dict)
    print(xmltodict.unparse(xml_dict,pretty=True))
if __name__=='__main__':
    main()
