import yaml
with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
for section in cfg:
        print(section)
print(cfg['AppConfig'])
print(cfg['Other']['Microservice'])