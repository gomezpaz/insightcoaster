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

app = hy.HydraApp(title='Insight Coaster')

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
    with col1:
        st.image("./img/logo.png", width=500)

    st.markdown('Accidents in roller coasters are still common in 2021. Therefore, our team came together to develop a Computer Vision software which has the objective of reducing the number of accidents in these rides: the *Insight Coaster*.')

    st.subheader('1. What Does the Software Do?')
    st.markdown('We are a data gathering and analysis service that efficiently helps increase passenger safety in coaster rides. One injury is one too many. Using Computer Vision and Machine Learning techniques, we build on existing products to come up with a unique and unprecedented solution to this pressing issue.')

    st.subheader('2. Retrieving Data')
    st.markdown(
        'According to the data from [Saferparks](https://ridesdatabase.org/saferparks/data/), an organization that collects data from multiple amusement parks, there are cases of people getting injured in rides.')
    st.markdown(
        'From the total of people that reported injuries, the following graphs show how many of them')

    col1, col2 = st.columns(2)
    with col1:
        st.image("./img/rideInjuries.png",
                 caption="Percentage of each of the rypes of injuries.")
    with col2:
        st.image("./img/rideTypes.png",
                 caption="Percentage of accidents in different types of attractions.")

    st.markdown('Moreover, information from the International Association of Amusement Parks and Attractions (IAPA) shows that 1171 riders got a type of injury, meaning that 3.9 people out of 1 million will get injured.')

    st.subheader('3. Development of a Prototype')
    st.write('Using the SolidWorks software, a virtual model of a camera was created and implemented into the design of a roller coaster cart.')
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("./img/cam.jpg", caption="Camera prototype on SolidWorks.")

    st.subheader('4. Software Implementation')
    st.markdown("At the moment, there is no existent reliable solution for non-frontal face tracking in low-cost cameras. Therefore Insight Coaster combines linear-regression along with object tracking techniques to achieve a performant algorithm that detects the user's head and the movement.")

    st.subheader('5. Testing the Insight Coaster')
    st.markdown('Testing is a crucial part of testing software; therefore, we created a Demo app in the *Software* tab, where users can test the application with their own camera.')

# 3D Models tab


@app.addapp(title='3D Models')
def Models():
    col1, col2, col3, col4, col5 = st.columns(5)
    st.header("3D Models")

    st.markdown(
        "At the moment, there are already many models of cameras suitable for the protection standard IP67.")
    st.markdown("All cameras have a slender design, a camera from IMPERX was chosen to create a 3D model, since the sheet with the specifications is publicly available. Using the SolidWorks software, a virtual model of this camera was created, and implemented into the design of a roller coaster cart.")
    st.markdown("The design of the camera itself has been recreated to provide an improvement for the task at hand. Based on this model, a special adapter case was created to simplify maintenance and installation on carts and seats.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('1. Roller Coaster Model')
        st.write('')

        components.html(
            """
            <div class="sketchfab-embed-wrapper"> <iframe title="Insight Coaster" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/4a64595deb6f4db8a7ff73ca087b5b85/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/insight-coaster-4a64595deb6f4db8a7ff73ca087b5b85?utm_medium=embed&utm_campaign=share-popup&utm_content=4a64595deb6f4db8a7ff73ca087b5b85" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Insight Coaster </a> by <a href="https://sketchfab.com/kizzie124?utm_medium=embed&utm_campaign=share-popup&utm_content=4a64595deb6f4db8a7ff73ca087b5b85" target="_blank" style="font-weight: bold; color: #1CAAD9;"> kizzie124 </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=4a64595deb6f4db8a7ff73ca087b5b85" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>
            """
        )
    with col2:
        st.subheader('2.  Camera Model')
        st.write('')
        components.html(
            """
            <div class="sketchfab-embed-wrapper"> <iframe title="Camera v2" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/c9c93ac4a7034e0f8bd15ad6b7c1951a/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/camera-v2-c9c93ac4a7034e0f8bd15ad6b7c1951a?utm_medium=embed&utm_campaign=share-popup&utm_content=c9c93ac4a7034e0f8bd15ad6b7c1951a" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Camera v2 </a> by <a href="https://sketchfab.com/kizzie124?utm_medium=embed&utm_campaign=share-popup&utm_content=c9c93ac4a7034e0f8bd15ad6b7c1951a" target="_blank" style="font-weight: bold; color: #1CAAD9;"> kizzie124 </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=c9c93ac4a7034e0f8bd15ad6b7c1951a" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>
            """
        )
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('3. Roller Coaster Seat')
        st.write('')

        components.html(
            """
            <div class="sketchfab-embed-wrapper"> <iframe title="Roller seat" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/76ff3282d6e84915b5f7f28dd70d0252/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/roller-seat-76ff3282d6e84915b5f7f28dd70d0252?utm_medium=embed&utm_campaign=share-popup&utm_content=76ff3282d6e84915b5f7f28dd70d0252" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Roller seat </a> by <a href="https://sketchfab.com/kizzie124?utm_medium=embed&utm_campaign=share-popup&utm_content=76ff3282d6e84915b5f7f28dd70d0252" target="_blank" style="font-weight: bold; color: #1CAAD9;"> kizzie124 </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=76ff3282d6e84915b5f7f28dd70d0252" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>
            """
        )
    with col2:
        st.subheader('4.  Adjustable Bar Lock')
        st.write('')
        components.html(
            """
            <div class="sketchfab-embed-wrapper"> <iframe title="Adjustable Bar Lock" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/901cb1dd33bd4bae8204b2f60f2b7805/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/adjustable-bar-lock-901cb1dd33bd4bae8204b2f60f2b7805?utm_medium=embed&utm_campaign=share-popup&utm_content=901cb1dd33bd4bae8204b2f60f2b7805" target="_blank" style="font-weight: bold; color: #1CAAD9;"> Adjustable Bar Lock </a> by <a href="https://sketchfab.com/kizzie124?utm_medium=embed&utm_campaign=share-popup&utm_content=901cb1dd33bd4bae8204b2f60f2b7805" target="_blank" style="font-weight: bold; color: #1CAAD9;"> kizzie124 </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=901cb1dd33bd4bae8204b2f60f2b7805" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>
            """
        )


@app.addapp(title='Software')
def Demo():
    st.header("Computer Vision Software")
    st.write('Press START and move from side to side as if you were in a coaster (wahoo!). Press SHOW DATA to visualize your motion chart.')
    st.write('*Make sure to have a high speed connection for the algo to perform correctly.*')

    webrtc_ctx = webrtc_streamer(
        key="motion-tracker",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        video_processor_factory=VideoProcessor,
        media_stream_constraints={"video": True, "audio": False},
        async_processing=True,
    )

    # Init chart
    plot = st.line_chart(pd.DataFrame([0], columns=['motion']))

    # Update data when user clicks
    if st.button('SHOW DATA'):
        if webrtc_ctx.video_processor:
            motion_list = webrtc_ctx.video_processor.motion_list
            plot.line_chart(pd.DataFrame(motion_list, columns=['motion']))


@app.addapp(title='Our Team')
def Contact():
    col1, col2, col3, col4, col5 = st.columns(5)
    st.header("Who are we?")

    st.subheader('Inspiration')
    st.markdown("On November 2nd, 2021, a group of engineers and computer scientist collectively came together to attend the SHPE 2021 Innovation Challenge with the objective of implementing a STEM project related to the Entertainment Industry.")

    st.subheader('Challenges faced')
    st.markdown("- There is no existent reliable solution for non-frontal face tracking in low-cost cameras. We had to combine linear-regression with object tracking techniques to achieve a performant algorithm.")
    st.markdown(
        "- Lack of testing data. Passengers are often filmed as a group, and not as individuals.")
    st.markdown("- Deprecated data about coaster injuries. Saferparks is no longer actively engaged in amusement ride accidents' research.")
    st.markdown(
        "- Lack of actual dimensions for 3D models. Research was necessary.")

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
    st.header('Ask us anything!')

    # link for Form Submit: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2Uyem5ldDJKVjRkaTBoTVJDRWNrUUZaWkhSZ3xBQ3Jtc0tsREpuSFdkbV9ENEFFUFNuNUlpZ3VsaVZWY1VLYl9PbHFFYnQtZk5pZnQtUjNQN1QzQ1NPNVUwcjFPWU9ONjVSQ1lVRmQxLXRKS1RHeVVmbVBieWxjU1RsVUlzNGtXM1Z4cGtLVHE1Z2hVbXYzZlZYWQ&q=https%3A%2F%2Fformsubmit.co%2F
    # AFTER SETTING THE HEADER for contact us section

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
