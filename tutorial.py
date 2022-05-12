from pathlib import Path
import streamlit as st

st.set_page_config(layout="wide")

def load_step(file_path: str):
    code_body = Path(file_path).read_text()

    with st.sidebar:
        st.write("---")

    with st.expander("Code"):
        st.code(code_body)

    ## WARNING: DO NOT DO THIS IN PRODUCTION ENVIRONMENTS!
    ## ONLY RUN THIS WITH TRUSTED SOURCES! FOR DEMONSTRATION PURPOSES ONLY!
    ## YOU HAVE BEEN WARNED!
    exec(code_body)

def celebrate():
    st.markdown("""
# You did it!

You made it to the end! Rejoice!

Hope you enjoyed this journey! 

If you have any feedback please send them to ...
""")

    st.balloons()

navigation = {
    "Tutorial": lambda: st.markdown(Path("tutorial.md").read_text()),
    "Step 1": lambda: load_step("tutorial_000.py"),
    "Step 2": lambda: load_step("tutorial_001.py"),
    "Step 2.1": lambda: load_step("tutorial_002.py"),
    "Step 3": lambda: load_step("tutorial_003.py"),
    "Step 4": lambda: load_step("tutorial_004.py"),
    "Step 4.1": lambda: load_step("tutorial_0041.py"),
    "Step 5": lambda: load_step("tutorial_005.py"),
    "Bonus: Step 6": lambda: load_step("tutorial_006.py"),
    "Bonus: Step 7": lambda: load_step("tutorial_007.py"),
    "🎉 Celebrate! 🎉": celebrate
}

with st.sidebar:
    step = st.radio("Navigation", navigation.keys())

if navigation.get(step, None):
    navigation[step]()