# import threading

from app.config import get_config
from app.queue import OrdersCreatedConsumer
from app.services import OrderService
from app.views import OrderTable
import streamlit as st
# from streamlit.script_run_context import add_script_run_ctx

orders = OrderService().get_all()


def main():
    st.markdown("""
    # {}
    """.format(get_config('app.title')))
    global orders

    OrderTable(render_component=st).render(orders=orders)


def rabbit() -> None:
    consumer = OrdersCreatedConsumer().init()
    consumer.start_consuming()


if __name__ == '__main__':
    st.set_page_config(
        page_title=get_config('app.title'),
        layout='wide',
        initial_sidebar_state='expanded',
    )

    main()
    rabbit()

    # thread_queue = threading.Thread(target=rabbit)
    # add_script_run_ctx(thread_queue)
    # thread_queue.start()
