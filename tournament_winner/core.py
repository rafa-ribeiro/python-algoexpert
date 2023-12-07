def tournament_winner(competitions, results):
    """
    Complexity:

    Time: O(n)
    Space: O(1)
    """
    champion = ""
    high_score = 0
    classification = dict()
    for i in range(len(competitions)):
        score = results[i]
        match_winner = competitions[i][0] if score == 1 else competitions[i][1]
        new_score = classification.get(match_winner, 0) + 3
        classification[match_winner] = new_score
        if new_score > high_score:
            high_score = new_score
            champion = match_winner

    return champion
