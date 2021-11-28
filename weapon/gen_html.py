
from collections import namedtuple
import os


WeaponItem = namedtuple("WeaponItem", ("name", "attr", "special", "get", "level_req", "key"))


def main():
    with open('武器介绍.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()[3:]

    result = []
    data = []
    for line in lines:
        line = line.strip()
        if line.startswith('第'):
            items = []
            data.append((line, items))
        else:
            weapon = WeaponItem(*line.split('\t'))
            items.append(weapon)

    for category, items in data:
        index = 0
        for weapon in items:
            result.append('<tr>')
            if index == 0:
                result.append('<th rowspan="{}">{}</th>'.format(len(items), category))
            result.append('<td>{}</td>'.format(weapon.name))
            result.append('<td><img src="images/{}.jpg"></td>'.format(weapon.key))
            result.append('<td>{}</td>'.format(weapon.attr))
            result.append('<td>{}</td>'.format(weapon.special))
            result.append('<td>{}</td>'.format(weapon.level_req.replace('最低等级限制：', '')))
            image_get1 = 'images_get/{}_get_01.jpg'.format(weapon.key)
            image_get2 = 'images_get/{}_get_02.jpg'.format(weapon.key)
            if not os.path.isfile(image_get1):
                image_get1 = None
            if not os.path.isfile(image_get2):
                image_get2 = None
            result.append('<td>{}<br>{}{}</td>'.format(
                weapon.get.replace('获得方法：', ''),
                '<img src="{}">'.format(image_get1) if image_get1 else '',
                '<img src="{}">'.format(image_get2) if image_get2 else ''
            ))
            result.append('</tr>')
            index += 1

    with open('template.html', 'r', encoding='utf-8') as file:
        output = file.read().replace('$content', '\n'.join(result))

    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(output)


if __name__ == "__main__":
    main()
