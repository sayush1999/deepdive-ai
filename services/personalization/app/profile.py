from google.cloud import firestore

_db = None

def _col():
    global _db
    if _db is None:
        _db = firestore.Client()
    return _db.collection("learner_profiles")

def record_interaction(user_id: str, mode: str, language: str, topic: str) -> None:
    _col().document(user_id).set({
        f"mode_counts.{mode}": firestore.Increment(1),
        "language": language,
        "topics": firestore.ArrayUnion([topic]),
    }, merge=True)

def get_profile(user_id: str) -> dict:
    snap = _col().document(user_id).get()
    return snap.to_dict() if snap.exists else {}
