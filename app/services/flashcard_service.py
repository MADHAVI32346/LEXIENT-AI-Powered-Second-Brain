import re

from app.core.logger import logging

def generate_flashcards(summary: str):
    """
        Generate simple flashcard from summary text.
    """

    flashcards = []

    # Split summary into sentences
    sentences = re.split(r'(?<=[.!?]) +', summary)

    for sentence in sentences[:5]:
        sentence = sentence.strip()

        if len(sentence) < 20:
            continue

        words = sentence.split()

        if len(words) < 5:
            continue

        # Create simple question
        question = f"'What is meant by: {' '.join(words[:5])}...?'"

        flashcards.append({
            "question": question,
            "answer": sentence
        })

    return flashcards