![GitHub Contributors](https://img.shields.io/github/contributors/Priyamjain1105/WeatherPlay)
# WeatherPlay

Welcome to the **WeatherPlay** project! This web application predicts whether it’s suitable to play a match based on weather conditions. Built with Python Flask, HTML, and CSS, it integrates a pre-trained Gaussian Naive Bayes machine learning model for accurate predictions.

## Project Overview

This project demonstrates the integration of machine learning into a web application. The application uses a Gaussian Naive Bayes model to analyze weather conditions and determine match suitability. The interface is user-friendly and built with Flask for seamless interaction.

## Key Features

- **Machine Learning Integration**: Uses a Gaussian Naive Bayes model to predict match suitability.
- **Multi-Page Interface**: Developed with Flask, HTML, and CSS for an intuitive user experience.
- **Real-Time Predictions**: Provides immediate feedback based on user input.

## Technologies Used

- **Python**: Server-side scripting and machine learning integration.
- **Flask**: Web framework for handling HTTP requests and routing.
- **HTML/CSS**: For structuring and styling the web pages.
- **Scikit-learn**: For implementing the Gaussian Naive Bayes model.

## Getting Started

Follow these steps to set up and run the project on your local machine:

## Prerequisites

- Python 3.x
- Flask
- Scikit-learn

## Installation

1. **Clone the repository:**

   ```bash
   [git clone https://github.com/yourusername/match-suitability-predictor.git
   cd match-suitability-predictor](https://github.com/Priyamjain1105/WeatherPlay.git)
   ```
2. **Create and activate a virtual environment**
   ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required dependencies**
   ```bash
      pip install -r requirements.txt
   ```
## Running The Application
1. Start the Flask server:
   ```bash
      flask run
   ```
2. Open a web browser and navigate to:
   ```bash
      http://localhost:5000
   ```
## Usuage
1. Enter Weather Data
   - Go to the prediction page and input the weather conditions such as temperature, 
     humidity, and wind speed.
2. Submit and Get Prediction
   - Click submit to receive a prediction on whether it's suitable to play a match
3. Explore the Interface
   - Use the navigation bar to visit different pages and access various features.

## Project Structure
```csharp
match-suitability-predictor/
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

# Screenshots
## Home Page
![Screenshot 2024-08-01 214906](https://github.com/user-attachments/assets/aab879cd-af06-4497-b08d-ae70cac49ba9)
## Prediction Page (Weather Suitable)
![Screenshot 2024-08-01 214952](https://github.com/user-attachments/assets/f30b1b13-8d4c-4595-ae39-78e0366669b5)
## Prediction Page (Weather Not Suitable)
![WhatsApp Image 2024-08-01 at 21 50 38_202e6e0f](https://github.com/user-attachments/assets/d4f74ea4-0cff-48f5-8402-3f8c19c7a195)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


