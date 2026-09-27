def generate_summary(text: str, max_bullets: int):
    sentences = [
        sentence.strip()
        for sentence in text.split(".")
        if sentence.strip()
    ]

    bullets = sentences[:max_bullets]

    return bullets