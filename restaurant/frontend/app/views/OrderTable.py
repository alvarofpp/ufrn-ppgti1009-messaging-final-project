from typing import List

from app.mixins import RenderMixin
from app.views import ItemList


class OrderTable(RenderMixin):

    def render(self, orders: List = None):
        if orders is None:
            orders = []

        for order in orders:
            expander_header = '#{} - R${}'.format(order.id, order.total_price)
            with self.render_component.expander(expander_header):
                self.render_component.markdown("""
                - **Customer**: #{}
                - **Total price**: R${}
                - **Status**: {}
                ---
                **Items**
                """.format(
                    order.customer_id,
                    order.total_price,
                    order.status,
                ))

                items_list = ''
                for item in order.items:
                    items_list += '- R${} - {}'.format(item.price, item.name)

                    if len(item.description) > 0:
                        items_list += ' ({})'.format(item.description)

                    items_list += '\n'

                self.render_component.markdown(items_list)

    def _headers(self) -> str:
        return """
        <tr>
        <th>#</th>
        <th>Price</th>
        <th>Items</th>
        <th>Actions</th>
        </tr>
        """
