import streamlit
def main():
    streamlit.title("Welcome to PyManager application website!")
    streamlit.header("Thank you for viewing the website!")
    streamlit.markdown("Click the button below to install the application:")
    install = streamlit.button("Install PyManager")
    view = streamlit.selectbox("Please use the application and give you views!:", ("Brilliant", "Good", "Fine", "Flawless", "Bad"))
    submit = streamlit.button("Submit view")
    if install:
        streamlit.markdown("Please search the URL: github.com/Bhumanyu-git/pymanager")
    if submit:
        streamlit.markdown(f"Your view: {view}")
main()