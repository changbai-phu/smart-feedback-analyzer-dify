import json

def main(classified_json_str: str):
    try:
        cleaned = classified_json_str.strip()
        parsed = json.loads(cleaned)
        
    except Exception as e:
        return {"summary_json": f"JSON parse error: {str(e)}"}

    items = parsed.get("classified_feedbacks", [])

    if not items:
        return {"result": "No feedback items found. Check input format."}

    total = len(items)
    by_category = {}
    by_urgency = {}
    by_sentiment = {}
    top_urgent = []

    for it in items:
        cat = it.get("category", "unknown")
        by_category[cat] = by_category.get(cat, 0) + 1

        urg = str(it.get("urgency_score", 1))
        by_urgency[urg] = by_urgency.get(urg, 0) + 1

        sen = it.get("sentiment", "neutral")
        by_sentiment[sen] = by_sentiment.get(sen, 0) + 1

        if it.get("urgency_score", 0) >= 4:
            top_urgent.append({
                "id": it.get("id"),
                "text": it.get("original_text", ""),
                "category": cat,
                "urgency_score": it.get("urgency_score", 0)
            })

    top_urgent = sorted(
        top_urgent,
        key=lambda x: x["urgency_score"],
        reverse=True
    )[:5]

    summary = {
        "total_feedback": total,
        "by_category": by_category,
        "by_urgency": by_urgency,
        "by_sentiment": by_sentiment,
        "top_urgent_examples": top_urgent
    }

    summary_json = json.dumps(summary, indent=2)

    return {"result": summary_json}