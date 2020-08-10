# -*- coding: UTF-8 -*
'''
Created on 2020-08-10
'''
import yaml, json


def test_image1():
    data = yaml.load(open('test/img1.yaml'), Loader=yaml.SafeLoader)
    if data.get('args'):
        args = data.get('args')
        if type(args) == dict:
            args = [{'key': k, 'value': str(v)} for k, v in args.items()]
        args.sort(key=lambda a: -len(a['key']))
        datastr = json.dumps(data)
        for a in args:
            k = a['key']
            v = a.get('default', '')
            if v is None:
                v = ''
            rv = ('%s' % v).replace('\n', '\\n')
            datastr = datastr.replace('$%s' % a['key'], rv).replace('${%s}' % a['key'], rv)
        data = json.loads(datastr)
    from oneimage import create_image

    img = create_image(data=data)
    img.show()


def test_image2():
    data = {
        'width': 300,
        'height': 300,
        'background': 'white',
        'elements': [
            {'type': 'image', 'url': 'http://www.inruan.com/static/img/logo.png', 'left': 0, 'top': 0, 'width': 100, 'height': 100},
            {'type': 'image', 'url': 'http://www.inruan.com/static/img/logo.png', 'left': 200, 'top': 200, 'width': 100, 'height': 100},
            {'type': 'text', 'text': 'Hello', 'font': 'https://cdn-qn.huaeb.com/ifarm/20200305/WeiRuanYaHei-1.ttf', 'left': 0, 'top': 100, 'width': 300, 'size': 20, 'height': 100, 'align': 'center', 'vertical': 'center', 'color': 'black'}
        ]
    }
    from oneimage import create_image

    img = create_image(data=data)
    img.show()


if __name__ == '__main__':
    # test_image1()
    test_image2()
