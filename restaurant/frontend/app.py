import threading

from app.config import get_config
from app.queue import OrdersCreatedConsumer, OrdersStatusUpdatedConsumer
from app.services import OrderService
from app.views import OrderTable
import streamlit as st
from streamlit.script_run_context import add_script_run_ctx

orders = OrderService().get_all()


def main():
    st.markdown("""
    # {}
    """.format(get_config('app.title')))
    global orders

    if st.button('Refresh orders'):
        orders = OrderService().get_all()

    OrderTable(render_component=st).render(orders=orders)


def queue_orders_created() -> None:
    consumer = OrdersCreatedConsumer().init()
    consumer.start_consuming()


def queue_orders_status_updated() -> None:
    consumer = OrdersStatusUpdatedConsumer().init()
    consumer.start_consuming()


if __name__ == '__main__':
    st.set_page_config(
        page_title=get_config('app.title'),
        layout='wide',
        initial_sidebar_state='expanded',
    )

    main()
    # queue_orders_created()
    # queue_orders_status_updated()

    thread_queue_orders_created = threading.Thread(target=queue_orders_created)
    add_script_run_ctx(thread_queue_orders_created)
    thread_queue_orders_created.start()

    thread_queue_orders_status_updated = threading.Thread(target=queue_orders_status_updated)
    add_script_run_ctx(thread_queue_orders_status_updated)
    thread_queue_orders_status_updated.start()
