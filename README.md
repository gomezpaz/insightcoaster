# Insight Coaster
----
SHPE 2021 Hackathon project

![Logo](logo-horizontal.jpg)

## Executive Summary
We use Computer Vision techniques and a low-cost live camera in front of roller coaster passengers to predict—and prevent—acute body motions that could result in injury. Our solution provides key insights on a per-passenger basis, is non-invasive, and sets the grounds for model training in the entertainment industry.

## Our Mission
We are a data gathering and analysis service that efficiently helps increase passenger safety in coaster rides. One injury is one too many. Using Computer Vision and Machine Learning techniques, we build on existing products to come up with a unique and unprecedented solution to this pressing issue.

**Please note that this application is still in development, and no prediction model should be taken seriously.**

## Coaster Injuries by the numbers
- **+ 80%** of injuries in amusement parks occur on a ride attraction
- **1125** happened on a roller coaster during 2017
- **49%** of these happened as a result of body motion, impact, or dislocation

*Source: https://ridesdatabase.org/saferparks - 2017 records*

## Features

### LOW-COST
Insight Coaster proposes a low-cost solution. Our standard passenger seat attachment for the camera is flexible and can be adapted to any type of coaster vehicle. While current motion capturing systems are complex and expensive, Insight Coaster leverages data processing techniques and a low-cost onboard camera to provide a reliable tracking solution estimated to be ~20x cheaper.

### DATA-DRIVEN
As Artificial Intelligence clusters get faster and cheaper, an ever-growing number of companies are using these techniques more and more to get an edge on the market. By 2030, data collection and analysis will become the basis of all future service offerings and business models. “Data is the new gold”. Insight Coaster is here on time, to set the grounds for model training in the entertainment industry.

### COVID-19 COMPLIANT
Covid has forced us to take additional contact-prevention measures, including the use of face masks and respirators. Our computer vision algorithm is trained to recognize passengers with or without masks. It also allows for non-contact body motion sensing, without the need for conventional motion capture suits, complying with pandemic-safe measures.

## Our Process

### CAMERA INSTALLATION
A low-cost camera module with an onboard edge computer will be mounted in each individual seat with a bar-lock mechanism (see the proposal in the 3D MODELS tab). The safety harness is standard and should prove useful in most rollercoaster vehicle seats. The camera will be fixed to a special case. This cover will be attached to a rod system with a universal adapter for attachment to the safety harness.

### DATA GATHERING
Insight Coaster will only record data with riders’ consent and the sole purpose of increasing coaster safety. Storage can be optimized by saving only relevant sections of the frame (head tilting area) and trimming down portions of interest in the ride (acute curves, control curves, etc). Over time, data will create a coasters’ profile for each segment of the ride, that will later be used as a baseline for inference.

### DATA PROCESSING
Real-time image processing will occur at the edge, with a dedicated computer in each camera module. A combination of linear-regression face recognition and object tracking will allow for frontal as well as non-frontal face tracking. Essential parameters will be communicated in real-time with the coaster monitoring system. These parameters will then be compared with historical data to conclude if safety measures are needed.

### PROPOSED SAFETY MEASURES
Using data from Insight Coaster, we take safety measures to prevent body motion injuries. Measures should be determined case-by-case, as every coaster is different. These include:
1. Preset max velocity on critical curves: an initial low-danger curve can help us infer the body motion of passengers on more dangerous turns coming later in the ride. Calculating how the passengers perform on this “diagnosis” curve, will allow us to determine how hard to “press the pedal” while ensuring maximum safety.
2. Individual rider feedback: alert passengers to “hold tight” if captured motion looks abnormal.
3. General roller coaster improvements: periodic passenger analysis allows to spot trends to aid maintenance and guide ride improvements.

OUT OF SCOPE/FUTURE PLANS
- Infrared capability: the project could be easily adjusted to work at night rides (coasters like Sheikra, Hollywood Rip Ride Rockit) using an IR camera adaptor.
- Sentiment tracking: recognizing passenger satisfaction/engagement throughout the ride could open the door for unprecedented UX optimization.

