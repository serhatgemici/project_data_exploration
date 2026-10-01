from streamlit_extras.avatar import *

st.subheader("Basic avatars")

col1, col2 = st.columns(2)

with col1:
    if avatar(
        "https://avatars.githubusercontent.com/u/1673013?v=4",
        height=128,
        label="Click me!",
        caption="I'm interactive",
        on_click="rerun",
        key="clickable_avatar",
    ):
        st.toast("Avatar clicked!")

with col2:
    if avatar(
        "https://avatars.githubusercontent.com/u/1673013?v=4",
        height=128,
        label="Click me!",
        caption="I'm interactive",
        on_click="rerun",
        key="clickable_avatar_2",
    ):
        st.toast("Avatar clicked!")
