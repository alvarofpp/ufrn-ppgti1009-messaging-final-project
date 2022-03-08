from app import SessionState
from app.mixins import RenderMixin

class OrderTable(RenderMixin):

    def render(self):
        orders = SessionState.get('orders')
        table = '| # | Price | Actions |\n| --- | --- | --- |'

        self.render_component.markdown(table)
