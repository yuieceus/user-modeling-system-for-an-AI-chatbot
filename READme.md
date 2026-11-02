# User Modeling System for an AI Chatbot

### Exploring Profile-Based Personalization in AI Tutoring

## Overview

This project explores how structured user profiles can influence the responses of an AI chatbot.

Three fictional learners with different knowledge levels, learning preferences, and learning goals were created. The same educational question was then used to compare responses generated with and without learner profile information.

The goal is to investigate whether personalization makes AI-generated explanations more relevant to individual learners.

## Research Question

**Does providing learner profiles improve the relevance of AI-generated educational responses?**

## Experimental Design

The experiment uses three fictional learner profiles:

| Learner | Knowledge Level | Learning Preference | Learning Goal |
|---|---|---|---|
| Student A | Beginner | Simple examples | Understand basic concepts |
| Student B | Intermediate | Step-by-step explanations | Solve practice problems |
| Student C | Advanced | Mathematical reasoning | Understand underlying theory |

All learners received the same question:

> Explain what a derivative is in mathematics.

Two conditions were compared:

**1. Baseline condition**

The chatbot received the question without any learner profile.

**2. Personalized condition**

The chatbot received the same question together with the learner's structured profile.

This resulted in six experimental cases.

## Technical Implementation

The project uses Python to:

- Store learner information in structured dictionaries.
- Generate baseline and personalized prompts.
- Organize experiment cases.
- Export prompts into a CSV file.

The project explores several concepts:

- Structured user profiles
- Context conditioning
- Prompt engineering
- Large Language Model (LLM) inference

### Response Collection

The original plan included using the Gemini API. However, API quota limitations prevented automated response generation.

Instead, the six prompts were generated using Python, and the corresponding responses were collected manually using ChatGPT.

Therefore, the current implementation demonstrates profile-based prompt generation and experimental comparison, rather than a fully automated API integration.

## Results and Observations

The personalized responses showed stronger alignment with the three learners' stated preferences and goals.

- **Student A:** Received simpler explanations and familiar examples.
- **Student B:** Received a structured, step-by-step explanation with a practice problem.
- **Student C:** Received a more advanced explanation covering mathematical definitions and theoretical concepts.

These observations suggest that structured learner profiles can guide the depth, style, and content of AI-generated explanations.

## Limitations

- Only three fictional learner profiles were tested.
- Only one mathematical question was used.
- Each condition was tested once per learner.
- Responses were collected manually rather than through an automated API.
- The evaluation was based on qualitative observations and does not establish statistical significance.

## Conclusion

This experiment demonstrates a simple approach to profile-based personalization in AI tutoring.

By providing structured learner information through prompts, an AI chatbot can adapt its explanations to different knowledge levels, learning preferences, and goals.

Although the experiment is small, it provides a starting point for exploring more advanced user modeling systems.

## Future Improvements

- Integrate an LLM API for automated response generation.
- Test additional subjects and questions.
- Evaluate responses using a consistent scoring rubric.
- Explore how user embeddings could complement structured learner profiles.

## Technologies

- Python
- CSV
- Prompt Engineering
- Large Language Models
- ChatGPT