This repo contains 3 different data engineering projects.
---
Folder CI_Error
contains a CI Run Extrator program, that analyzes data from a real NGO project by Ruby4Good. 

To run it successfully, you need to generate a Github token from the settings of your personal account. Below is a picture that demonstrates that process:

![alt text](assets/image.png)

Important to create the .env file with variable linking to your token information.
---

Audio Processing.
---

This project aims to demonstrate audio processing using the following Python libraries listed below in the index description.

Database: https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio

The database contains a wide range of audio files that can be converted into ndarrays - Different actors recorded audio with different emotions.
In the present work, there are some audio manipulations, such as:

1) Amplitude Alteration
2) Frequency Change
3) Adding Noise
4) Audio Reversal
5) Integration of audio from different actors - same emotion
6) Integration of audio with different emotions - same actor
7) Convolution
8) Creation of Metadata.

At the end of the project, we have the creation of a DataFrame with all the audios and their respective Metadata in .csv format.

To access the saved audios (coming from a DataFrame), simply enter the "output" folder. In the "output" folder, there is also a .csv file coming from the audio DataFrame.

There is also the possibility to develop next steps as described at the end of the code.

The project functions appear throughout the code, as they are created according to the demand of the topics.

## Installation

Before running the project, ensure you have Python installed on your system. Then, install the required Python packages using the following commands:

```sh
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install scikit-learn
```

If you have errors related to any packages being used by the program, you have to run the commands to install them like explained before.


