# evaluate.py

from typing import List, Dict, Tuple

def recall_at_k(recommended: List[str], relevant: List[str], k: int = 3) -> float:
    """Calculate Recall@k."""
    recommended_k = recommended[:k]
    relevant_set = set(relevant)
    if not relevant_set:
        return 0.0
    hits = sum(1 for item in recommended_k if item in relevant_set)
    return hits / len(relevant_set)

def average_precision_at_k(recommended: List[str], relevant: List[str], k: int = 3) -> float:
    """Calculate Average Precision@k."""
    relevant_set = set(relevant)
    if not relevant_set:
        return 0.0
    score = 0.0
    hits = 0
    for idx, item in enumerate(recommended[:k]):
        if item in relevant_set:
            hits += 1
            score += hits / (idx + 1)
    return score / min(len(relevant_set), k)

def evaluate_all(queries_results: List[Dict], k: int = 3) -> Tuple[float, float]:
    """Compute mean Recall@k and MAP@k for a list of queries."""
    recalls = []
    maps = []
    for result in queries_results:
        recommended = result["recommended"]
        relevant = result["relevant"]
        recalls.append(recall_at_k(recommended, relevant, k))
        maps.append(average_precision_at_k(recommended, relevant, k))
    mean_recall = sum(recalls) / len(recalls) if recalls else 0.0
    mean_map = sum(maps) / len(maps) if maps else 0.0
    return mean_recall, mean_map

# --- Sample Test Execution ---
if __name__ == "__main__":
    test_queries = [
        {
            "query": "Hiring Java devs under 45 mins",
            "recommended": ["Java Basics", "SQL Intermediate", "Python Fundamentals"],
            "relevant": ["Java Basics", "SQL Intermediate"]
        },
        {
            "query": "Analyst cognitive & personality test",
            "recommended": ["Cognitive Aptitude", "Personality Fit", "Excel Skills"],
            "relevant": ["Cognitive Aptitude", "Personality Fit"]
        },
        {
            "query": "Mid-level Python, JS, SQL",
            "recommended": ["Python Intermediate", "SQL Advanced", "JS Fundamentals"],
            "relevant": ["Python Intermediate", "SQL Advanced", "JS Fundamentals"]
        }
    ]

    mean_recall, mean_ap = evaluate_all(test_queries, k=3)
    print(f"🎯 Mean Recall@3: {mean_recall:.3f}")
    print(f"📊 MAP@3: {mean_ap:.3f}")
