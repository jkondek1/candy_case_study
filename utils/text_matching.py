from difflib import SequenceMatcher


def find_closest_match(target_word: str, names_list: list[str], threshold: float=0.6) -> tuple[str | None, float]:
    """
    Find the closest matching name from a list using fuzzy string matching.

    Args:
        target_word (str): The word to match against
        names_list (list): List of names to search through
        threshold (float): Minimum similarity score (0-1) to consider a match

    Returns:
        tuple: (best_match, similarity_score) or (None, 0) if no match above threshold
    """
    best_match = None
    best_score = 0

    for name in names_list:
        # Calculate similarity ratio between target and current name
        similarity = SequenceMatcher(None, target_word.lower(), name.lower()).ratio()

        if similarity > best_score:
            best_score = similarity
            best_match = name

    # Return match only if it meets the threshold
    if best_score >= threshold:
        return best_match, best_score
    else:
        return None, 0
