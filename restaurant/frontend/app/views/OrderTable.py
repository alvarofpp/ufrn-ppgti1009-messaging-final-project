from typing import List

from app.mixins import RenderMixin
from app.views import OrderStatusButton


class OrderTable(RenderMixin):

    def render(self, orders: List = None):
        if orders is None:
            orders = []

        for order in orders:
            expander_header = '#{} - R${}'.format(order.id, order.total_price)
            with self.render_component.expander(expander_header):
                column_one, column_two = self.render_component.columns([2, 1])

                column_one.markdown("""
                - **Customer**: #{}
                - **Total price**: R${}
                - **Status**: {}
                """.format(
                    order.customer_id,
                    order.total_price,
                    order.status,
                ))

                OrderStatusButton(render_component=column_two).render(order)

                self.render_component.markdown("""
                ---
                **Items**
                """)

                items_list = ''
                for item in order.items:
                    items_list += '- R${} - {}'.format(item.price, item.name)

                    if len(item.description) > 0:
                        items_list += ' ({})'.format(item.description)

                    items_list += '\n'

                self.render_component.markdown(items_list)
