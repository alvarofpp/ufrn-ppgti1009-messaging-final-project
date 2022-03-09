from app.config import get_config
from app.views import OrderTable
import streamlit as st


def main():
    st.markdown("""
    # {}
    """.format(get_config('app.title')))

    OrderTable(render_component=st).render()


if __name__ == '__main__':
    st.set_page_config(
        page_title=get_config('app.title'),
        layout='wide',
        initial_sidebar_state='expanded',
    )
    main()
