from math import floor

def get_speed_statistic(test_results):
    # Αν η λίστα είναι άδεια, επέστρεψε [0, 0, 0]
    if len(test_results) == 0:
        return [0, 0, 0]
    
    # Υπολογισμός των τιμών
    low = min(test_results)
    high = max(test_results)
    avg = floor(sum(test_results) / len(test_results))
    
    return [low, high, avg]
