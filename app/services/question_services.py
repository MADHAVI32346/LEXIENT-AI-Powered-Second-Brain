from app.core.logger import logging
from app.core.exception import CustomException
import sys

def generate_questions(summary: str):
    try:
        logging.info("Starting question generation")

        questions = []

        # Temporary dummy question
        questions.append({
            "question": "What is the main topic of the summary?",
            "options": [
                "Artificial Intelligence",
                "Database",
                "Networking",
                "Cyber Security"
            ],
            "answer": "Artificial Intelligence"
        })

        logging.info("Questions generated successfully")

        return questions
    
    except Exception as e:

        logging.error(f"Question generation failed: {str(e)}")

        raise CustomException(e, sys)