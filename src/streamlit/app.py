import streamlit as st

st.set_page_config(
    page_title="Titanic Classification",
    page_icon="🚙",
    layout="wide",
)

home_page = st.Page(
    "app_pages/home.py",
    title="Home",
    icon="🏠",
)

exploration_page = st.Page(
    "app_pages/exploration.py",
    title="Exploration",
    icon="🔍",
)

visualization_page = st.Page(
    "app_pages/data_visualization.py",
    title="Data Visualization",
    icon="📊",
)

modeling_page = st.Page(
    "app_pages/modeling.py",
    title="Modeling",
    icon="👾",
)

references_page = st.Page(
    "app_pages/references.py",
    title="References",
    icon="📚",
)

about_page = st.Page(
    "app_pages/about.py",
    title="About",
    icon="👤",
)

navigation = st.navigation(
    {
        "CO2 Project": [
            home_page,
            exploration_page,
            visualization_page,
            modeling_page,
            references_page,
            about_page,
        ],
    },
    position="sidebar",
)

navigation.run()
