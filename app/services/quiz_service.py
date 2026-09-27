def generate_quiz(topic: str, number_of_questions: int):
    questions = []

    for i in range(1, number_of_questions + 1):
        questions.append({
            "id": i,
            "question": f"What is an important concept in {topic}?",
            "options": [
                "Concept A",
                "Concept B",
                "Concept C",
                "Concept D"
            ]
        })

    return questions