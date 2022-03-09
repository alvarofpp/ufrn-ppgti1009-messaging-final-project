from typing import List


class ItemList:
    @staticmethod
    def make(items: List = None):
        if items is None:
            items = []

        ul = '<ul>'

        for item in items:
            ul += '<li>R${} - {}'.format(item.price, item.name)

            if len(item.description) > 0:
                ul += ' ({})'.format(item.description)

            ul += '</li>'

        ul += '</ul>'

        return ul
