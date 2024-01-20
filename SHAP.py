### ============================== 打开网页，在cmd命令界面运行下面一段 ============================== ###
# streamlit run C:\Users\Tracy\Desktop\2024寒假\科研\01.18Python-streamlit\SHAP.py [ARGUMENTS]
import streamlit as st

st.set_page_config(
    page_title="Streamlit-入门",  # 页面标题
    page_icon=":rainbow:",  # icon
    layout="wide",  # 页面布局
    initial_sidebar_state="auto"  # 侧边栏
)
st.title("多页面Streamlit简介")

## ============================== 后台记录 ============================== ##
def record():
    import streamlit as st
    import time
    ##  显示进度
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'Iteration {i+1}')
      bar.progress(i + 1)
      time.sleep(0.000001)
    '项目加载中，请君稍等...'
    ## 会话状态-用于计算页面的运行次数
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    st.session_state.counter += 1
    st.text(f"本网页已运行 {st.session_state.counter} 次.")
    st.button("重新运行")
    ##  状态存储【记录得到用户之前的输入和结果】
    # Initialization
    if 'key' not in st.session_state:
        st.session_state['key'] = 'value'
    # Session State also supports attribute based syntax
    if 'key' not in st.session_state:
        st.session_state.key = 'value'
    ## 回调函数
    def form_callback():
        st.write(st.session_state.my_slider)
        st.write(st.session_state.my_checkbox)

    with st.form(key='my_form'):
        slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
        checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
        submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

## ============================== 数据展示API ============================== ##
def data_show():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.figure_factory as ff
    import altair as alt
    ## 将需要展示的变量直接单独放置在一行
    df = pd.DataFrame({'col1': [1, 2, 3]})
    df  # 👈 Draw the dataframe
    ##title函数【用于设置应用的标题，支持Emoji、Latex和颜色设置】
    st.title("This text is :red[colored red], and this is **:blue[colored]** and bold.")
    ## header函数【用于设置应用内容的标题，支持Emoji、Latex和颜色设置】
    st.header("This text is :red[colored red], and this is **:blue[colored]** and bold.")
    ## subheader函数【用于设置应用内容的子标题，支持Emoji、Latex和颜色设置】
    st.subheader("This text is :red[colored red], and this is **:blue[colored]** and bold.")
    ## caption函数【用于标题、旁白、脚注、旁注和其他解释性文本，支持Emoji、Latex和颜色设置】
    st.caption("This text is :red[colored red], and this is **:blue[colored]** and bold.")
    ## text函数【将文本内容展示为等宽格式。】
    st.text("This text is nomogram.")
    ## code函数【将代码进行展示，支持多语言】
    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')
    ## dataframe函数【可以自行设置表格格式、宽度和高度】
    df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
    st.dataframe(df)  # Same as st.write(df)
    ## table函数【静态展示，不支持拖动和内容修改】
    df = pd.DataFrame(np.random.randn(10, 5), columns=('col %d' % i for i in range(5)))
    st.table(df)
    ## metric函数【以粗体显示指标，并可选指示指标如何变化】
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    ## json函数【将内容进行折叠展示】
    st.json({
        'foo': 'bar',
        'baz': 'boz',
        'stuff': [
            'stuff 1',
            'stuff 2',
            'stuff 3',
            'stuff 5',
        ],
    })
    ## line_chart函数【st.line_chart将使用altair展示折线图，支持交互式拖拽、放大和缩小】
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
    ## area_chart函数【将使用altair展示面积图，支持交互式拖拽、放大和缩小】
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.area_chart(chart_data)
    ## bar_chart函数【将使用altair展示折线图，支持交互式拖拽、放大和缩小】
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
    # altair_chart函数【将显示Altair内容，支持交互式拖拽、放大和缩小】
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    c = alt.Chart(chart_data).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(c, use_container_width=True)
    ## vega_lite_chart函数【将显示Vega-Lite内容，支持交互式信息展示，但不支持放大和缩小】
    chart_data = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
    st.vega_lite_chart(chart_data, {
        'mark': {'type': 'circle', 'tooltip': True},
        'encoding': {
            'x': {'field': 'a', 'type': 'quantitative'},
            'y': {'field': 'b', 'type': 'quantitative'},
            'size': {'field': 'c', 'type': 'quantitative'},
            'color': {'field': 'c', 'type': 'quantitative'},
        },
    })
    ## plotly_chart函数【将显示Plotly内容，支持交互式信息展示，支持放大和缩小】
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    hist_data = [x1, x2, x3]  # Group data together
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig, use_container_width=True)  # Plot!


## ============================== 输入控件API ============================== ##
def input_tools():
    import streamlit as st
    import pandas as pd
    import datetime
    from PIL import Image
    import os
    os.chdir(r'C:\Users\Tracy\Desktop\2024寒假\科研\01.18Python-streamlit')  # 设定文件路径

    ## button函数【将展示可以点击的按钮】
    # 如果按钮点击，则展示hello there
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')
    ## download_button函数【数据下载的按钮】
    # with open("任务分配.png", "rb") as file:
    #     btn = st.download_button(label="Download image", data=file, file_name="flower.png", mime="image/png")
    ## checkbox函数【展示单选框】
    agree = st.checkbox('I agree')
    if agree:
        st.write('Great!')
    ## radio函数【展示多选按钮】
    genre = st.radio("What\'s your favorite movie genre", ('Comedy', 'Drama', 'Documentary'))
    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn\'t select comedy.")
    ## selectbox【展示下拉选项】
    option = st.selectbox("How would you like to be contacted?", ("Email", "Home phone", "Mobile phone"))
    st.write('You selected:', option)
    ## multiselect【展示多选下拉选项】
    options = st.multiselect('What are your favorite colors', ['Green', 'Yellow', 'Red', 'Blue'], )
    st.write('You selected:', options)
    ## slider【展示数值滑动条】
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')
    ## select_slider【展示列表滑动条】
    color = st.select_slider('Select a color of the rainbow', options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('My favorite color is', color)
    ## text_input【单行文本输入】
    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)
    ## number_input【展示数值输入】
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)
    ## text_area【多行文本输入】
    txt = st.text_area('Text to input')
    st.write('Your input:', txt)
    ## date_input【日期输入】
    d = st.date_input("When\'s your birthday", datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)
    ## time_input【时间输入】
    t = st.time_input('Set an alarm for', datetime.time(8, 45))
    st.write('Alarm is set for', t)
    ## file_uploader【文件上传】
    uploaded_files = st.file_uploader("请选择文件(可多个)：", accept_multiple_files=True, type=["csv"])
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write("文件名:", uploaded_file.name)
        st.dataframe(df)
    # uploaded_files = st.file_uploader("请选择文件(可多个)：",accept_multiple_files=False, type=["xlsx","xls"])
    # for uploaded_file in uploaded_files:
    #     df = pd.read_excel(uploaded_file.read())
    #     st.dataframe(df)
    ## camera_input【摄像头拍照】
    picture = st.camera_input("Take a picture")
    if picture:
        st.image(picture)
    ## color_picker【颜色选择】
    color = st.color_picker('Pick A Color', '#00f900')
    st.write('The current color is', color)
    # image【展示图片】
    image = Image.open('任务分配.png')
    st.image(image, caption='Sunrise by the mountains')
    # ## audio【展示音频】
    # audio_file = open('myaudio.ogg', 'rb')
    # audio_bytes = audio_file.read()
    # st.audio(audio_bytes, format='audio/ogg')
    # video【video】
    # video_file = open('S4.原型演示(视频)-赛题08-可视化AI模型平台-视界AI.mp4', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)


## ============================== 页面布局API ============================== ##
def page_set():
    import streamlit as st
    ## sidebar【展示左侧栏】
    # Using object notation
    # add_selectbox = st.sidebar.selectbox("How would you like to be contacted?",("Email", "Home phone", "Mobile phone"))
    # Using "with" notation
    # with st.sidebar:
    #     add_radio = st.radio("Choose a shipping method",("Standard (5-15 days)", "Express (2-5 days)"))
    ## columns【分列展示内容】
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")
    ## tabs【分栏展示内容】
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    ## expander【折叠内容】
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
    with st.expander("See explanation"):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.image("https://static.streamlit.io/examples/dice.jpg")


page_names_to_funcs = {
    '项目管控':record,
    '数据API':data_show,
    '输入API':input_tools,
    '布局API':page_set
}
demo_name = st.sidebar.radio("选择一个界面", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()