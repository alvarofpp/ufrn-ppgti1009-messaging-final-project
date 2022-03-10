from typing import Any

import streamlit as st


class SessionState:
    DEFAULT_VALUES = {
        'orders': [],
        'orders_count': 1,
        'order_id': None,
    }

    @staticmethod
    def clear(key: str):
        SessionState._check_key(key)
        st.session_state[key] = SessionState.DEFAULT_VALUES[key]

    @staticmethod
    def get(key: str = None) -> Any:
        if key is None:
            return st.session_state

        SessionState._check_key(key)
        SessionState._set_default_value_if_necessary(key)
        return st.session_state[key]

    @staticmethod
    def set(key: str, value: Any):
        SessionState._check_key(key)
        st.session_state[key] = value

    @staticmethod
    def _set_default_value_if_necessary(key: str):
        if key not in st.session_state:
            st.session_state[key] = SessionState.DEFAULT_VALUES[key]

    @staticmethod
    def _check_key(key: str):
        if key not in SessionState.DEFAULT_VALUES.keys():
            raise ValueError('Invalid key value.')
