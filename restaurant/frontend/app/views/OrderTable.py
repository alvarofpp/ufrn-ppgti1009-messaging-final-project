from app.mixins import RenderMixin


class OrderTable(RenderMixin):

    def render(self):
        table = '| # | Price | Actions |\n| --- | --- | --- |'

        self.render_component.markdown(table)
