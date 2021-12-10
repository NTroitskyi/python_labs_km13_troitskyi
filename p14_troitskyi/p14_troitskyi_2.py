import json
Filename = 'image_info_test-dev2017.json'
with open(Filename, 'r') as ch:
    data = json.load(ch)
    count = 0
    for a in data["images"]:
        if 'file_name' in a:
            count += 1
        if '000000000001.jpg' == a['file_name']:
            print('\nUrl:', a['coco_url'], '\nHeight: ', a['height'],'\nWidth:', a['width'],'\nID:', a['id'])
        for q in a['file_name']:
            ''.join(q)
    print('Total images:', count)
    for a in data["images"]:
        if a["id"] == max([i['id'] for i in data['images']]):
            print('File with the highest id number:', a["file_name"])
