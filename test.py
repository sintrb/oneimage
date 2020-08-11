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
            {'type': 'text', 'text': 'Hello', 'font': 'https://cdn-qn.huaeb.com/ifarm/20200305/WeiRuanYaHei-1.ttf', 'left': 0, 'top': 100, 'width': 300, 'size': 20, 'height': 100, 'align': 'center', 'vertical': 'center', 'color': 'black'},
        ]
    }
    from oneimage import create_image
    img = create_image(data=data)
    img.show()


def test_image3():
    data = {'width': 1200, 'height': 2000, 'elements': [{'left': 204, 'top': 409, 'type': 'image', 'width': 810, 'height': 581, 'url': 'https://cdn-qn.huashangpay.cn/hsp/20200702/FmIS_MqG3JZY2K-pKB8upiCStKmA.jpg?vframe/jpg/offset/0', 'radius': 0, 'mode': 'fit'}, {'left': -4, 'top': 0, 'type': 'image', 'width': 1200, 'height': 2000, 'url': 'https://cdn-qn.huashangpay.cn/hsp/20200811/FnrlNi_Qfd3g8A3hkWmL4A9B2gVw.png', 'radius': 0, 'mode': 'fit'}, {'left': 394, 'top': 1331, 'type': 'image', 'width': 430, 'height': 430, 'url': 'http://127.0.0.1:8080/utils/wxacode?scene=SHARE3', 'radius': 0, 'mode': 'fit'}, {'left': 514, 'top': 1451, 'type': 'image', 'width': 190, 'height': 190, 'url': 'https://cdn-qn.huashangpay.cn/hsp/20200710/FlDiwjIdOR_EUkVBO06NyB3It-qA.jpg', 'radius': 95, 'mode': 'fit'}, {'left': 529, 'top': 129, 'type': 'image', 'width': 160, 'height': 160, 'url': 'https://cdn-qn.huashangpay.cn/hsp/20200710/FlDiwjIdOR_EUkVBO06NyB3It-qA.jpg', 'radius': 80, 'mode': 'fit'}, {'left': 204, 'top': 292, 'type': 'text', 'width': 810, 'height': 100, 'text': '小唐向你推荐', 'font': 'https://cdn-qn.huaeb.com/ifarm/20200305/WeiRuanYaHei-1.ttf', 'align': 'center', 'size': 60, 'vertical': 'center'}, {'left': 204, 'top': 1037, 'type': 'text', 'width': 810, 'height': 250, 'text': '特红二头 B级 ￥18', 'font': 'https://cdn-qn.huaeb.com/ifarm/20200310/Fs15pNOwATX0jqslGddZbn5PZ0K_.otf', 'align': 'left', 'size': 60, 'vertical': 'top'}]}
    from oneimage import create_image
    img = create_image(data=data, debug='red')
    img.show()


if __name__ == '__main__':
    # test_image1()
    # test_image2()
    test_image3()
