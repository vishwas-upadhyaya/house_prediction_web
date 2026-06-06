# Bangalore House Price Prediction - Full-Stack Django Application

## Project Overview
This repository contains a sophisticated, end-to-end **House Price Prediction** system specifically tailored for the Bangalore real estate market. The project integrates a trained machine learning model with a robust **Django** web application, providing a user-friendly interface for instant property valuation based on various physical and geographical parameters.

## What is this Project?
The application provides a seamless 'Real Estate Valuation' experience:
- **Instant Estimation:** Predicts the price of a house in Bangalore based on square footage, number of bedrooms (BHK), bathrooms, and location.
- **Dynamic Data Loading:** Uses asynchronous requests to populate available locations dynamically, ensuring a responsive user experience.
- **Production-Ready Backend:** A full-stack implementation that demonstrates how to bridge the gap between a data science model and a web-based delivery platform.

## How it was done (Deep Technical Details)
- **Machine Learning Architecture:**
    - **Model:** **Linear Regression** trained on a curated Bangalore housing dataset.
    - **Pipeline:** The model is saved as a **Pickle** object (`banglore_price_predict_model.pickle`) for efficient deserialization and low-latency inference.
- **Feature Engineering & Preprocessing:**
    - **One-Hot Encoding:** Manually implemented in the inference logic to handle over 200+ distinct locations in Bangalore. It uses a `columns.json` mapping to ensure the feature vector alignment matches the training state.
    - **Vector Construction:** Inputs (sqft, bath, bhk) are combined with the one-hot encoded location index into a NumPy array before being fed to the model.
- **Backend Implementation (Django Framework):**
    - **View Logic:** Uses Django's `View` and `TemplateView` classes to separate concerns between page rendering and data processing.
    - **Asynchronous API:** Implements `JsonResponse` endpoints (`get_location`, `estimate`) that allow the frontend to interact with the model without page reloads.
    - **MVT Pattern:** Follows the Model-View-Template architectural pattern for clean, maintainable code.
- **Data Serialization:**
    - `columns.json`: Stores the feature column order required for consistent model input.
    - `pickle`: Used for high-speed loading of the regression model.

## Why it was done
- To solve the real-world problem of price opacity in the real estate market.
- To demonstrate the complete lifecycle of a machine learning project: from data cleaning and model training to deployment as a full-stack web application.
- To practice advanced Django techniques like AJAX integration and custom model-inference management.

## Tech Stack
- **Backend:** Python, Django
- **Machine Learning:** Scikit-learn (Linear Regression), NumPy
- **Data Handling:** JSON, Pickle
- **Frontend:** HTML5, CSS3, JavaScript (AJAX/Fetch)
- **Database:** SQLite (default for Django settings)

## Key Features
- **Bangalore Location Coverage:** Support for predicting prices in hundreds of specific localities.
- **AJAX-Powered Predictions:** Users get estimations instantly without leaving the page.
- **Mobile Responsive UI:** (Implied via Django templates) Designed to work across different device types.

## File Structure
- `prediction/views.py`: Orchestrates the prediction logic and API responses.
- `prediction/model_related.py`: Contains the core inference engine, feature vector construction, and model loading.
- `prediction/banglore_price_predict_model.pickle`: The pre-trained linear regression weights.
- `prediction/columns.json`: Mapping file for one-hot encoding.
- `templates/home.html`: The main user interface.

## Local Setup
1.  **Clone the repository:**
    ```bash
    git clone [repository-url]
    ```
2.  **Install dependencies:**
    ```bash
    pip install django numpy scikit-learn
    ```
3.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```
4.  **Start the Server:**
    ```bash
    python manage.py runserver
    ```
5.  **Access the App:** Navigate to `http://127.0.0.1:8000` in your web browser.
