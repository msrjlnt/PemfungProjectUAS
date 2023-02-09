import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from itertools import permutations, combinations
import time, openai, os

# st.set_page_config(layout="wide")

# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
openai.api_key = "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"

def title(text):
    st.title(text)
    st.markdown('''
    <hr style="height:2px;width:100%;border-width:0;color:gray;background-color:gray">
                ''', unsafe_allow_html=True)


menu = ['Permutation', 'Combination', 'AingBotz', 'About', 'Developer']
choice = st.sidebar.selectbox("Menu", menu)


if choice == 'Permutation':
    title('Permutation & Combination Calculator')
    st.header("""Permutation""")
    st.header("")
    st.latex(r""" ^nP_r = \frac{n!}{(n-r)!} """)
    st.header("")

    iterable = st.text_input(label="Enter Iterable separated by a space")

    if iterable:
        iterable = list(int(n) for n in iterable.split(' ') if n != '')

    try:

        num2 = int(st.number_input("Enter number for **r**"))
        calc = permutations(iterable, num2)

        calc = [i for i in calc]
        result = str(calc).strip('[]')

        if iterable:
            with st.spinner(text='Process'):
                time.sleep(1)
                st.success(f"""Result : \n\n{result}\n\nThere are **{len(calc)}** 
                        ways to permute the iterable""")

    except ValueError as err:
        st.warning(f"{err}")


elif choice == 'Combination':
    title('Permutation & Combination Calculator')
    st.header("""Combination""")
    st.header("")
    st.latex(r""" ^nC_k = \frac{n!}{k!(n-r)!} """)
    st.header("")

    iterable = st.text_input(label="Enter Iterable separated by a space")

    if iterable:
        iterable = list(int(n) for n in iterable.split(' ') if n != '')

    try:

        num2 = int(st.number_input("Enter number for **k**"))
        calc = combinations(iterable, num2)

        calc = [i for i in calc]
        result = str(calc).strip('[]')

        if iterable:
            with st.spinner(text='Process'):
                time.sleep(1)
                st.success(f"""Result : \n\n{result}\n\nThere are **{len(calc)}** 
                        ways to combine the iterable""")

    except ValueError as err:
        st.warning(f"{err}")


elif choice == 'About':
    st.subheader('About')

    components.html("""
        <iframe width="800" height="475" src="https://www.youtube.com/embed/jfKfPfyJRdk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                    """,
                    width=800, height=475)
    # st.snow()

    # components.iframe(
    #     src="https://docs.streamlit.io/library/cheatsheet", scrolling=True, width=1000, height=800)


elif choice == 'Developer':
    title('Developers')
    st.markdown("# <center> Kelompok 2 </center>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    memory = {}

    def memoize_image(func):

        def inner(img):
            if img not in memory:
                memory[img] = func(img)  # path as a key, image name as a value

            return memory[img]

        return inner


    @memoize_image
    def show_image(path):
        image = Image.open(path)
        st.image(image=image)

        return os.path.basename(path)

    
    with col1:
        show_image(
            r'D:\A.TELKOM\semester 3\Pemrograman Fungsional\Tubes\Our Project\The Project\img\asyafa.png')

        st.write("### <center> Asyafa Ditra Al Hauna<br><br><br>21102116</center>",
                 unsafe_allow_html=True)

    with col2:
        show_image(
            r'D:\A.TELKOM\semester 3\Pemrograman Fungsional\Tubes\Our Project\The Project\img\ammar.png')

        st.write("### <center> Muhammad Ammar Izzudin <br><br> 21102122</center>",
                 unsafe_allow_html=True)

    with col3:
        show_image(
            r'D:\A.TELKOM\semester 3\Pemrograman Fungsional\Tubes\Our Project\The Project\img\mansur.png')
        
        st.write("### <center> Mansur Julianto <br><br><br>21102121</center>",
                 unsafe_allow_html=True)

    with col4:
        show_image(
            r'D:\A.TELKOM\semester 3\Pemrograman Fungsional\Tubes\Our Project\The Project\img\yoko.png')

        st.write("### <center> Setyoko Almuludin <br><br><br>21102128 </center>",
                 unsafe_allow_html=True)
        st.write("### <center>  </center>",
                 unsafe_allow_html=True)

    # st.snow()
    # st.write(memory)  # ? Check memoization

elif choice == 'AingBotz':
    
    @st.experimental_memo(persist='disk')
    def ChatGPT(user_query):
        ''' 
          This function uses the OpenAI API to generate a response to the given 
          user_query using the ChatGPT model
          '''

        # Use the OpenAI API to generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=user_query,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )
        response = completion.choices[0].text
        return response

    st.title("Chatting with ChatGPT:sparkles:")
    st.sidebar.header("Instructions")
    st.sidebar.info('''This is a web application that allows you to interact with
          the OpenAI API's implementation of the ChatGPT model.
          Enter a **query** in the **text box** and **press enter** to receive
          a **response** from the ChatGPT
          ''')

    # Get user input
    user_query = st.text_input("Your Question:grey_question:",
                               "what the difference between permutation and combination?")

    if user_query:
        # Generate response
        response = ChatGPT(user_query)
        # Display response
        st.success(response)
