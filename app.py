from os import write
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import streamlit.components.v1 as components
import hydralit as hy
from computervision.motiontracker import VideoProcessor
import pandas as pd
import numpy as np

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

app = hy.HydraApp(title='Head Tracker App')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

@app.addapp(title='Home')   
def Home():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.image("./img/logo.png", width=500)

    
    st.markdown('Accidents in roller coasters are still common in 2021. Therefore, the our team came together to develop a Computer Vision software which has the objective of reducing the number of accidents in these rides: the *Insight Coaster*.')

    st.subheader('1. What Does the Software Do?')
    st.write('The Insight Coaster is a system developed for theme parks to help detect injuries in rollercoaster rides.')

    st.subheader('2. Retrieving Data')
    st.markdown('According to the data from [Saferparks](https://ridesdatabase.org/saferparks/data/), an organization that collects data from multiple amusement parks, there are cases of people getting injured in rides.')
    st.markdown('From the total of people that reported injuries, the following graphs show how many of them')

    col1, col2 = st.columns(2)
    with col1:
        st.image("./img/rideInjuries.png", caption="Percentage of each of the rypes of injuries.")
    with col2:
        st.image("./img/rideTypes.png", caption="Percentage of accidents in different types of attractions.")


    st.markdown('Moreover, information from the International Association of Amusement Parks and Attractions (IAPA) shows that 1171 riders got a type of injury, meaning that 3.9 people out of 1 million will get injured.')

    st.subheader('3. Development of a Prototype')
    st.write('Using the SolidWorks software, a virtual model of a camera was created and implemented into the design of a roller coaster cart.')
    st.image("./img/cam.jpg", caption="Camera prototype on SolidWorks.")

    st.subheader('4. Software Implementation')
    st.write('')

    st.subheader('5. Testing the Insight Coaster')
    st.write('')

## 3D Models tab
@app.addapp(title='3D Models')
def Models():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.header("3D Models")
    
    st.markdown("At the moment, there are already many models of cameras suitable for the protection standard IP67.")
    st.markdown("All cameras have a slender design, a camera from IMPERX was chosen to create a 3D model, since the sheet with the specifications is publicly available. Using the SolidWorks software, a virtual model of this camera was created, and implemented into the design of a roller coaster cart.")
    st.markdown("The design of the camera itself has been recreated to provide an improvement for the task at hand. Based on this model, a special adapter case was created to simplify maintenance and installation on carts and seats.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('1. Roller Coaster Model')
        st.write('')

        components.html(
            """
            <div class="sketchfab-embed-wrapper"> <iframe title="Train v1" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/4a64595deb6f4db8a7ff73ca087b5b85/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/train-v1-4a64595deb6f4db8a7ff73ca087b5b85?utm_medium=embed&utm_campaign=share-popup&utm_content=4a64595deb6f4db8a7ff73ca087b5b85" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Train v1 </a> by <a href="https://sketchfab.com/kizzie124?utm_medium=embed&utm_campaign=share-popup&utm_content=4a64595deb6f4db8a7ff73ca087b5b85" target="_blank" style="font-weight: bold; color: #1CAAD9;"> kizzie124 </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=4a64595deb6f4db8a7ff73ca087b5b85" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>
            """
        )
    with col2:
        st.subheader('2.  Camera Model')
        st.write('')
        components.html(
            """
            <div class="sketchfab-embed-wrapper"> 
            <iframe title="Camera" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/1f1768423f2e4de08f5854d514ccf7f1/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/camera-1f1768423f2e4de08f5854d514ccf7f1?utm_medium=embed&utm_campaign=share-popup&utm_content=1f1768423f2e4de08f5854d514ccf7f1" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Camera </a> by <a href="https://sketchfab.com/kizzie124?utm_medium=embed&utm_campaign=share-popup&utm_content=1f1768423f2e4de08f5854d514ccf7f1" target="_blank" style="font-weight: bold; color: #1CAAD9;"> kizzie124 </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=1f1768423f2e4de08f5854d514ccf7f1" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p>
            </div>
            """
        )


@app.addapp(title='Software')
def Demo():
    col1, col2, col3= st.columns(3)
    with col2:
        st.header("Computer Vision Software")
    # webrtc_streamer(key="demo",
    #                 video_transformer_factory=VideoTransformer)

    webrtc_ctx = webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        video_processor_factory=VideoProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )

    # Showcase data
    chart_data = pd.DataFrame(np.random.randn(20, 3),
                              columns=['a', 'b', 'c'])

    plot = st.line_chart(chart_data)

@app.addapp(title='Our Team')
def Contact():
    st.subheader('Inspiration')
    st.markdown("On November 2nd, 2021, a group of engineers and computer scientist collectively came together to attend the SHPE 2021 Innovation Challenge with the objective of implementing a STEM project related to the Entertainment Industry.")

    # st.header('Challenges faced')

    st.subheader('What we learned')
    st.markdown("The team was able to be creative and work together effectively. Even though most of the members were not familiar with each other before the beginning of the Innovation Challenge, they worked respectfully and fast-paced. Besides that, the students were able to practice their programming and design skills and even build new ones -which will be very helpful throughout their STEM careers.")


    st.subheader('Meet the Team')
    col1, col2 = st.columns(2)
    with col1:
        st.image("./img/bianca.jpg", width=300)
        st.write("Bianca Silva")
        st.write("Computer Engineering")
        st.write("Florida Polytechnic University")
        st.write("careerbiancasilva@gmail.com")

        st.image("./img/santiago.jpg", width=300)
        st.write("Santiago Gomez")
        st.write("Computer Science")
        st.write("Brigham Young University")
        st.write("gomezpaz@byu.edu")

    with col2:
        st.image("./img/chris.jpg", width=300)
        st.write("Christopher Molina")
        st.write("Computer Engineering")
        st.write("Florida Polytechnic University")
        st.write("christophermolina99@gmail.com")

        st.image("./img/kirill.jpg", width=300)
        st.write("Kirill Sokov")
        st.write("Mechatronic Engineering")
        st.write("Vaughn College of Aeronautics and Technology")
        st.write("kirill.sokolov124@gmail.com")

@app.addapp(title='Contact Us')
def Contact():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.header('Get in touch')
   
    ##link for Form Submit: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2Uyem5ldDJKVjRkaTBoTVJDRWNrUUZaWkhSZ3xBQ3Jtc0tsREpuSFdkbV9ENEFFUFNuNUlpZ3VsaVZWY1VLYl9PbHFFYnQtZk5pZnQtUjNQN1QzQ1NPNVUwcjFPWU9ONjVSQ1lVRmQxLXRKS1RHeVVmbVBieWxjU1RsVUlzNGtXM1Z4cGtLVHE1Z2hVbXYzZlZYWQ&q=https%3A%2F%2Fformsubmit.co%2F
    ##AFTER SETTING THE HEADER for contact us section

    contact_us = """
    <form action="https://formsubmit.co/cris23molina@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_us, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")
    


app.run()
