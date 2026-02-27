import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
header = f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}"
print(header)
print(f"{'-' * 50} {'-' * 20} {'-' * 7} {'-' * 6}")

for item in data['imdata']:
    attrs = item['l1PhysIf']['attributes']
    dn = attrs.get('dn', '')
    descr = attrs.get('descr', '')
    speed = attrs.get('speed', '')
    mtu = attrs.get('mtu', '')
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")