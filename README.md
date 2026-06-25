# AI-Powered Developer Project Recommendation System

## Overview

This project is a content-based recommendation system that suggests software projects based on a user's interests and skills. It uses Natural Language Processing (NLP) techniques to compare user input with project descriptions and recommend the most relevant projects.

## Features

- Recommends projects based on user interests
- Uses TF-IDF Vectorization for text representation
- Uses Cosine Similarity for recommendation generation
- Interactive command-line interface
- Supports multiple searches until the user exits

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- NLP
- TF-IDF Vectorization
- Cosine Similarity

## Project Structure

```
AI_Project_Recommendation_System/
│
├── projects.csv
├── recommendation.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python recommendation.py
```

## Example

Input:

```
python nlp
```

Output:

```
Recommended Projects:

- Resume Analyzer
- Chatbot
- Sentiment Analysis Tool
```

## How It Works

1. Project descriptions are loaded from the dataset.
2. TF-IDF Vectorization converts text into numerical vectors.
3. User interests are transformed into vectors.
4. Cosine Similarity measures the similarity between user interests and project descriptions.
5. The most relevant projects are recommended.

## Author

Developed as part of the CodSoft Artificial Intelligence Internship.