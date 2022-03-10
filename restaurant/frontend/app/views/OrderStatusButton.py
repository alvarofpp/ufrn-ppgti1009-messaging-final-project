from app.enums import OrderStatusEnum
from app.mixins import RenderMixin
from app.models import Order
from app.services import OrderService


class OrderStatusButton(RenderMixin):

    def render(self, order: Order) -> None:
        button_text = self._get_text_by_status(order)
        if self.render_component.button(button_text, key='btn_change_status_{}'.format(order.id)):
            OrderService().change_status(order)

    def _get_text_by_status(self, order: Order) -> str:
        base_text = 'Change status to "{}"'

        if order.status == str(OrderStatusEnum.ORDER_NEW.value):
            return base_text.format('accepted')
        elif order.status == str(OrderStatusEnum.ORDER_ACCEPTED.value):
            return base_text.format('in delivery')

        return base_text.format('delivered')
