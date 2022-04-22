import yaml

with open('code/yaml_sample.yaml')as data:
    yaml_sample=data.read()
# print(yaml_sample)
yaml_dict = yaml.load(yaml_sample,Loader=yaml.FullLoader)
print(yaml_dict)

yaml_dict["interface"]["ipv4"]["-ip"]="1.1.1.1"
with open('code/yaml_sample.yaml','w')as data:
    data.write(yaml.dump(yaml_dict,default_flow_style=False))

print(yaml_dict)