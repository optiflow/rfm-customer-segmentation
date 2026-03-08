def segment_me(df):
    """
    Segments customers based on their RFM score.
    """
    try:
        score = df['RFM_Score']
        if score is None:
            return '3.Bronze'

        if score >= 9:
            return '1.Gold'
        elif (score >= 5) and (score < 9):
            return '2.Silver'
        else:
            return '3.Bronze'
    except (KeyError, TypeError):
        return '3.Bronze'
