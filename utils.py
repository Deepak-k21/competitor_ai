def estimate_footfall(reviews):
    if reviews > 500:
        return "High Footfall"
    elif reviews > 200:
        return "Moderate Footfall"
    else:
        return "Low Footfall"