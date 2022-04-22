import json
def read_from_json(file_name):
    output_json = json.load(open(file_name))
    for majorkey, subdict in output_json.items():
        for subkey, value in subdict.items():
            print (f"{subkey}=={value}")
    return output_json
            

    # for v, k in output_json.items():
    #     if not isinstance(k, list):
    #         for x, y in k.items():
    #             print(x,':', y)
    #     else:
    #         for i in k:
    #             for s, m in i.items():
    #                 print(s,':', m)

def write_to_json(json_data,file_name):
    json_data["interface"]["description"]="test"
    with open(file_name,'w') as data:
        json.dump(json_data,data,indent=4)
    print(json_data)

def main():
    file_name='code/json_sample.json'
    json_data=read_from_json(file_name)
    write_to_json(json_data,file_name)
    
if __name__=='__main__':
    main()

