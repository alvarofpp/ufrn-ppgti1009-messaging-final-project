from typing import Dict

from app.config import get_config
from app.services import OrderService
from app.views import OrderTable
import streamlit as st
from streamlit.legacy_caching import caching


@st.cache
def get_data() -> Dict:
    return {
        'orders': OrderService().get_all(),
    }


def main():
    st.markdown("""
    # {}
    """.format(get_config('app.title')))

    if st.button('Refresh orders'):
        caching.clear_cache()

    data = get_data()

    OrderTable(render_component=st).render(orders=data['orders'])


if __name__ == '__main__':
    st.set_page_config(
        page_title=get_config('app.title'),
        layout='wide',
        initial_sidebar_state='expanded',
    )
    main()
