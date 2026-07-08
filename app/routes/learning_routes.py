from fastapi import APIRouter
from app.services.flashcard_service import generate_flashcards
from app.services.question_services import generate_questions
from app.core.logger import logging
from app.core.exception import CustomException
import sys

router = APIRouter(
    prefix="/learning",
    tags = ["Learning System"]
)

@router.get("/test")
async def learning_test():
    return {
        "message": "Learning routes working successfully"
    }

@router.post("/generate-flashcards")
async def create_flashcards(data: dict):

    summary = data.get("summary")

    if not summary:
        return {
            "error": "Summary is required"
        }
    
    flashcards = generate_flashcards(summary)

    return {
        "flashcards": flashcards
    }

@router.post("/generate-questions")
async def create_questions(data: dict):
    try:
        logging.info("Question generation API called")

        summary = data.get("summary")

        if not summary:

            logging.warning("Summary not provided")

            return {
                "error": "Summary is required"
            }
        
        questions = generate_questions(summary)

        logging.info("Question generation successfully")

        return {
            "question": questions
        }
    
    except Exception as e:
        logging.error(f"Question route error: {str(e)}")

        raise CustomException(e, sys)