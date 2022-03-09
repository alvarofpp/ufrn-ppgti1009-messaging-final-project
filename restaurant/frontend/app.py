from app.config import get_config
from app.services import OrderService
from app.views import OrderTable
import streamlit as st


# @st.cache
def get_data():
    return {
        'orders': OrderService().get_all(),
    }

def main():
    st.markdown("""
    # {}
    """.format(get_config('app.title')))
    OrderTable(render_component=st).render(orders=get_data()['orders'])


if __name__ == '__main__':
    st.set_page_config(
        page_title=get_config('app.title'),
        layout='wide',
        initial_sidebar_state='expanded',
    )
    main()
