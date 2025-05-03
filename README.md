# SHL Assessment Recommender

![SHL Assessment Recommender](https://img.shields.io/badge/SHL-Assessment%20Recommender-00cec9)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini%20AI-4285F4?style=flat&logo=google&logoColor=white)

## Overview

SHL Assessment Recommender is an AI-powered web application that helps hiring managers and recruiters quickly identify the most suitable SHL assessments for their specific job requirements. By analyzing job descriptions or hiring queries, the application leverages Google's Gemini 2.5 Pro AI to recommend relevant assessments from the SHL catalog.

![image](https://github.com/user-attachments/assets/41a94f0a-fd46-478b-a85a-1df035639056)


## Features

- **Smart Matching**: Uses advanced AI to analyze job requirements and match them with appropriate assessments
- **Comprehensive Results**: Provides detailed information about each recommended assessment
- **User-Friendly Interface**: Clean, modern UI designed for ease of use
- **API Support**: Can be accessed programmatically via query parameters

## Prerequisites

- Python 3.7+
- Streamlit
- Pandas
- Google Generative AI Python SDK
- A Google AI API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/shl-assessment-recommender.git
   cd shl-assessment-recommender
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter a job description or specific requirements in the text area

4. Click "Get Smart Recommendations" to receive tailored assessment suggestions

## API Usage

The application can be accessed programmatically by appending a query parameter:

```
http://localhost:8501/?query=Hiring%20Java%20developers%20with%20strong%20business%20communication
```

This will return a JSON response with the recommended assessments.

## Data

The application requires an SHL assessment catalog CSV file named `shl_assessment_catalog.csv` with the following columns:
- Assessment Name
- Test Type
- Assessment URL
- Duration
- Remote Testing Support
- Adaptive/IRT Support

## Security Note

This application includes an API key in the source code. For production use, please:
1. Move the API key to environment variables
2. Add proper authentication for API usage
3. Implement rate limiting

## Customization

You can adjust the following parameters in the code:
- `top_k`: Number of recommendations to display (default: 10)
- `temperature`: Controls randomness in AI responses (default: 0.7)

## License

[MIT License](LICENSE)

## Acknowledgements

- Built with Streamlit and Google Gemini AI
- Created by RS Krishna

---

For questions or support, please contact [krishna61223@gmail.com]
