# Data Engineering Projects with NumPy and Pandas
This repository showcases three distinct data engineering projects aimed at processing logs, audio, and images using Python with NumPy and Pandas libraries.


### Log_processing Folder
---

Contains a folder called CI_Error_extrator where a CI_Extrator.py will retrieve data from CI Test Workflows.
In our case we are workign with real world data from Human Essentials (A Diaper Bank Platform) project by NGO/Ruby4Good, but the configurations contained could be adapted to work well with other repositories.

If you want to re-populate the data with the most recent CI workflow runs, you'll need to generate a GitHub token from your personal account settings. Refer to the image below for guidance:

![alt text](assets/image.png)

Ensure to create a .env file with variables linking to your token information.

To understand the data, there is a .ipynb file that transforms and loads data and with help of external libraries bringing a visual representation of the Logs and it's behavior over time.

The main manipulations include:
1) Trends Over Time: Visualize test examples and failures over time to identify patterns or spikes in test outcomes.
2) Relationship Between Examples and Failures: Explore the correlation between the number of tests run and failures using a scatter plot.
3) Distribution of Failures: Analyze the frequency of failures to identify common failure rates and outliers with a histogram.
4) Daily Summary of Failures: Summarize daily failures to pinpoint days with high failure rates, suggesting potential areas for investigation.
5) Failures by Hour of the Day: Examine failure distribution by hour to determine if failures cluster at specific times, indicating optimal times for running tests.
6) Failures by Day of the Week: Aggregate failures by day of the week to reveal patterns, helping in planning test schedules more effectively.

Future Steps:
- Enhancing error log data extraction for more detailed analysis.
- Using machine learning to predict test outcomes based on historical data.
- Automating the identification of flaky tests to improve test reliability.

### Audio Processing.
---

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


### Image Processing.
---

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

### Installation
---

Ensure Python is installed on your system, then run the following commands to install necessary packages:

```sh
pip install ipykernel pandas numpy matplotlib seaborn scikit-learn python-dotenv requests spacy
```

If any errors occur related to missing packages, install them as described above.

### Source
---
1) [Kaggle Dataset: Emotional Speech Audio Dataset](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)
2) [Wikipedia: Sierpinski Triangle](https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Sierpinski)


