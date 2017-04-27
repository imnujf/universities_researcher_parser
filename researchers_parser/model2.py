# -*- encoding:utf8 -*-

import codecs

from xpaw import Selector


def work_flow():
    print('AAAAAAAAA')
    pass


if __name__ == '__main__':

    f = codecs.open("running-1.html", "r", "utf-8")
    content = f.read()
    f.close()
    # tree = etree.HTML(content)
    tree = Selector(content)
    #print(tree)

    nodes = tree.xpath(u"//body[@id='myzone3']/div[@id='main-content']/div[@class='container']/div[@class='m-itme']")
    #print(nodes)
    for n in nodes:
        print(n.text)

