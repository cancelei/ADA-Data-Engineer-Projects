# Data Engineering Projects with NumPy and Pandas
This repository showcases three distinct data engineering projects aimed at processing logs, audio, and images using Python with NumPy and Pandas libraries.
---

### CI_Error Folder
This folder contains a program called CI Run Extractor, which analyzes data from a real NGO project by Ruby4Good.

To run it successfully, you'll need to generate a GitHub token from your personal account settings. Refer to the image below for guidance:

![alt text](assets/image.png)

Ensure to create a .env file with variables linking to your token information.
---

### Audio Processing.
This project demonstrates audio processing utilizing various Python libraries.

Database: [Emotional Speech Audio Dataset](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

The dataset comprises audio files recorded by different actors expressing various emotions. In this project, we perform several audio manipulations, including:

1) Amplitude Alteration
2) Frequency Change
3) Adding Noise
4) Audio Reversal
5) Integration of audio from different actors with the same emotion
6) Integration of audio with different emotions from the same actor
7) Convolution
8) Creation of Metadata

The output includes a DataFrame containing all audios and their respective metadata in .csv format, stored in the "output" folder.

There is also the possibility to develop next steps as described at the end of the code.

Each stage of development is divided into very explanatory topics in the "audio.ipynb" file
---

### Image Processing.
This project focuses on image processing using Python libraries to create a fractal similar to the Sierpinski Triangle.
The main manipulations include:

1) Scaling
2) Rotation
3) Translation

The processing is divided into three levels:

* Level 1: Inserting a triangle within the main triangle
* Level 2: Inserting three triangles within the main triangle
* Level 3: Inserting nine triangles within the main triangle

The images were joined by replacing the values of the main image array in the correct positions for the values of the arrays of each triangle created.

The final results are stored in the "Images" folder, showcasing the primary image after transformations and insertions for each processing level.

For future projects, recursive fractal creation is suggested for cleaner and more elegant code.

Each stage of development is divided into very explanatory topics in the "imagem.ipynb" file
---

### Installation
Ensure Python is installed on your system, then run the following commands to install necessary packages:

```sh
pip install ipykernel pandas numpy matplotlib seaborn scikit-learn python-dotenv requests spacy
```

If any errors occur related to missing packages, install them as described above.

### Source
1) [Kaggle Dataset: Emotional Speech Audio Dataset](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)
2) [Wikipedia: Sierpinski Triangle](https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Sierpinski)


