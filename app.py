import os

import streamlit as st

# from utils.assistant import Assistant
from utils.load_data import load_text_data
from utils.pie_chart import pie_chart
from utils.line_graph import pe_vc_vs_sp500

# os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

# assistant = Assistant()
text_data = load_text_data()
strategies_pie_chart = pie_chart()

# with st.sidebar:
#     st.subheader("Ask me anything about VCCs")
#     chat_container = st.container(height=300)
#     for message in assistant.get_history():
#         with chat_container.chat_message(message.role):
#             st.markdown(message.content[0].text.value)

#     if prompt := st.chat_input('Say something'):
#         with chat_container.chat_message('user'):
#             st.markdown(prompt)
#         with chat_container.chat_message('assistant'):
#             stream = assistant.ask(prompt)
#             chat_container.write_stream(stream)


col1, col2 = st.columns(2)
sub_col1, sub_col2 = col2.columns(2)
col1.header('VARIABLE CAPITAL COMPANY', anchor=None)
sub_col1.metric(label="Number of VCC", value="1,029", delta="60")
sub_col2.metric(label="Number of Sub-Funds", value="2,158", delta="163")

overview_container = st.container()
overview_container.subheader('Overview')
overview_container.markdown(text_data['description'][0])

st.write('---')

structure_container = st.container()
structure_container.subheader('Structure')
structure_container.image("./assets/structure.png")
structure_container.markdown(text_data['description'][1])

st.write('---')

benefits_container = st.container()
benefits_container.subheader('Benefits of Registering a VCC in Singapore')
benefits_container.markdown(text_data['description'][2])

st.write('---')
strategies_container = st.container()
strategies_container.subheader('Proposed Strategies')
strategies_container.pyplot(strategies_pie_chart)

tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Tax Benefits', 'Historical Performance', 'Proposed Strategies'])

with tab1:
    st.subheader('Private Equity/Venture Capital')
    st.markdown(text_data['description'][3])

with tab2:
    st.subheader('Tax Benefits')
    st.markdown(text_data['description'][4])

with tab3:
    st.subheader('Historical Performance')
    pe_vc_vs_sp500()
    st.markdown(text_data['description'][5])

with tab4:
    sub_tab1, sub_tab2, sub_tab3, sub_tab4 = st.tabs(['Early Stage Startups', 'Growth Stage Startups', 'Private Equity', 'Feeder Fund'])
    with sub_tab1:
        st.subheader('High-Risk Sub-Fund: Early-Stage Startups Focused on AI')
        st.markdown(text_data['description'][6])
    with sub_tab2:
        st.subheader('Medium-Risk Sub-Fund: Series A & B Tech Companies')
        st.markdown(text_data['description'][7])
    with sub_tab3:
        st.subheader('Low-Risk Sub-Fund: Private Equity in Plastic Manufacturing')
        st.markdown(text_data['description'][8])
    with sub_tab4:
        st.subheader('Feeder Fund: Diverse Fund Investments')
        st.markdown(text_data['description'][9])