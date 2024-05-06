import streamlit as st
import pandas as pd
import time
MAIN_PATH = 'data/'
PLASMID_File = MAIN_PATH + '质粒抽提.csv'
progress_text = "Operation in progress. Please wait."
import streamlit as st
import time
st.set_page_config(page_title='Bio', page_icon='🔥', layout="wide", initial_sidebar_state="expanded", menu_items=None)

# @st.experimental_fragment
def bar(seconds):
    with st.empty():
        for second in range(seconds):
            st.write(f"⏳ {second} seconds have passed")
            time.sleep(1)
        st.write("✔️ 1 minute over!")
    # if st.button('开始计时'):
    #     count =0
    #     with st.container():
    #         while count<second:
    #             time.sleep(1)
    #             st.write(count)
    #             count+=1
    #     st.write('end')


def get_protocol(file_path,):
    data = pd.read_csv(file_path,keep_default_na=None)
    return data.iterrows()
@st.cache_data
def get_len():
    data = pd.read_csv(PLASMID_File,keep_default_na=None)
    return len(data)
if 'button_index' not in st.session_state:
    st.session_state.button_index = 0
@st.experimental_fragment
def on_click(plas_itter):
    col1,col2 = st.columns([1,2])
    if col1.button('下一步', key=st.session_state.button_index, ):
        st.session_state.button_index+=1
        if st.session_state.button_index<get_len()+1:

            content = next(plas_itter)
            col2.subheader(f'第{content[0]+1}步')
            col2.subheader(content[1]['name'])
            st.write('---')
            col1.write('---')
            col2.write('---')
            for txt,index_name in zip(content[1],content[1].index):
                if index_name == 'url':
                    col1.image(txt)
                if index_name == 'time':
                    if txt:
                        # if col1.button('开始计时'):
                        time_min = txt.rstrip('min')
                        # bar(int(time_min)*60)

                if index_name in['entity','entity_volumn','do','time','note']:

                    if txt:
                        col2.write(index_name)
                        col2.subheader(txt)
                if index_name in['plasmid_type','entity_components',]:
                    if txt:
                        col1.write(index_name)
                        col1.subheader(txt)






            # st.write(content)
        else:
            st.write('end')

st.header('质粒抽提——大抽')
with st.container():
    st.markdown('[质粒抽提常见问题](https://www.yaoxuanzhi.com/informationdetail?id=3d3b1564e233dc73b3719bd9d5fc91d0)')
    if st.button('start'):

        plas_itter = get_protocol(PLASMID_File, )

        on_click(plas_itter)
        # content = next(plas_itter)
        # st.write(content)
        # on_click(plas_itter)


