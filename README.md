# WeatherPlay 🌤️🎾

![GitHub Contributors](https://img.shields.io/github/contributors/Priyamjain1105/WeatherPlay) 
![GitHub License](https://img.shields.io/github/license/Priyamjain1105/WeatherPlay)
![GitHub Stars](https://img.shields.io/github/stars/Priyamjain1105/WeatherPlay?style=social)

Welcome to the **WeatherPlay** project! This web application predicts whether it’s suitable to play a match based on weather conditions. Built with Python Flask, HTML, and CSS, it integrates a pre-trained Gaussian Naive Bayes machine learning model for accurate predictions.

<div align="center">
  <img src="https://media.giphy.com/media/26FPCXdkvDbKBbgOI/giphy.gif" width="500"/>
</div>


## 🌟 Project Overview

This project demonstrates the integration of machine learning into a web application. The application uses a Gaussian Naive Bayes model to analyze weather conditions and determine match suitability. The interface is user-friendly and built with Flask for seamless interaction.

## ✨ Key Features

- **🔍 Machine Learning Integration**: Uses a Gaussian Naive Bayes model to predict match suitability.
- **🌐 Multi-Page Interface**: Developed with Flask, HTML, and CSS for an intuitive user experience.
- **⚡ Real-Time Predictions**: Provides immediate feedback based on user input.

## 🛠️ Technologies Used

- **Python**: Server-side scripting and machine learning integration.
- **Flask**: Web framework for handling HTTP requests and routing.
- **HTML/CSS**: For structuring and styling the web pages.
- **Scikit-learn**: For implementing the Gaussian Naive Bayes model.

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine:

## 📋 Prerequisites

- Python 3.x
- Flask
- Scikit-learn

## 📥 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Priyamjain1105/WeatherPlay.git
   cd WeatherPlay
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running The Application

1. **Start the Flask server:**
   ```bash
   flask run
   ```
2. **Open a web browser and navigate to:**
   ```bash
   http://localhost:5000
   ```

## 🖥️ Usage

1. **Enter Weather Data**
   - Go to the prediction page and input the weather conditions such as temperature, humidity, and wind speed.
2. **Submit and Get Prediction**
   - Click submit to receive a prediction on whether it's suitable to play a match.
3. **Explore the Interface**
   - Use the navigation bar to visit different pages and access various features.

## 📂 Project Structure
```csharp
WeatherPlay/
│
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html        # Home page
│   ├── predict.html      # Prediction page
│   └── layout.html       # Base template
│
├── static/               # Static files (CSS, JS)
│   ├── styles.css        # Stylesheet
│
├── model/                # Pre-trained model
│   └── model.pkl         # Serialized model file
│
├── requirements.txt      # Project dependencies
└── README.md             # Project README file
```

## 📸 Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/aab879cd-af06-4497-b08d-ae70cac49ba9)

### Prediction Page (Weather Suitable)
![Prediction Suitable](https://github.com/user-attachments/assets/f30b1b13-8d4c-4595-ae39-78e0366669b5)

### Prediction Page (Weather Not Suitable)
![Prediction Not Suitable](https://github.com/user-attachments/assets/d4f74ea4-0cff-48f5-8402-3f8c19c7a195)

## 🌟 Contributors
[![Contributors](https://contrib.rocks/image?repo=Priyamjain1105/WeatherPlay)](https://github.com/Priyamjain1105/WeatherPlay/graphs/contributors)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<div align="center">
  <img src="https://media.giphy.com/media/l0HlNf9v4z9Eyfe7u/giphy.gif" width="200"/>
</div>

Feel free to suggest additional enhancements or provide feedback! Happy coding! 🎉
