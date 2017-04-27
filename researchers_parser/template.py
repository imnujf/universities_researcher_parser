# -*- encoding:utf8 -*-

import yaml


class TemplateMatch(object):

    def __init__(self, tpl_list, html_tree):
        self.tpl_list = tpl_list
        self.html_tree = html_tree
        self.match_res = dict()

    def match(self):

        for i in range(len(self.tpl_list)):
            if self._is_match(self.tpl_list[i]):
                return i

        return -1

    def _is_match(self, tpl):

        for nth in range(len(tpl)):

            _rules = tpl[nth].split('*****')
            _xpath = _rules[0]
            _times = int(_rules[1])

            _xpath_value = self.html_tree.xpath(_xpath)

            if len(_xpath_value) < _times:
                self.match_res = dict()
                return False
            else:
                for i in _xpath_value:
                    _key = 'xpath_'+str(nth)+'_'+str(i)
                    _value = _xpath_value[i]
                    self.match_res[_key] = _value

        return True


def update_tpl(tpl_base_file, new_tpl_file):

    f = open(tpl_base_file)
    tpl_base = yaml.load(f)
    f.close()

    f = open(new_tpl_file)
    new_tpl = yaml.load(f)
    f.close()

    modified_flag = False
    if tpl_base is not None:
        for each_tpl in tpl_base:
            if new_tpl['school'] == each_tpl['school']:
                if 'college' in each_tpl:
                    if new_tpl['college'] == each_tpl['college']:
                        each_tpl['tpl_rules'].append(new_tpl['tpl_base'])
                        if 'department' in each_tpl:
                            if new_tpl['college'] == each_tpl['college']:
                                each_tpl['tpl_rules'].append(new_tpl['tpl_rules'])
                                modified_flag = True
                        else:
                            each_tpl['tpl_rules'].append(new_tpl['tpl_rules'])
                            modified_flag = True
                else:
                    print(each_tpl['tpl_rules'])
                    print(new_tpl['tpl_rules'])
                    each_tpl['tpl_rules'].append(new_tpl['tpl_rules'])
                    modified_flag = True

            if modified_flag is True:
                break

    if modified_flag is False:
        _tp = new_tpl['tpl_rules']
        new_tpl['tpl_rules'] = []
        new_tpl['tpl_rules'].append(_tp)
        if tpl_base is None:
            tpl_base = []
        tpl_base.append(new_tpl)

    f = open(tpl_base_file, "w")
    yaml.dump(tpl_base, f)
    f.close()

    return


if __name__ == '__main__':
    tpl_base_file = '../templates.yaml'
    new_tpl_file = '../new_template.yaml'
    update_tpl(tpl_base_file, new_tpl_file)