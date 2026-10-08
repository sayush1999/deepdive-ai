from .profile import get_profile

def recommend_mode(user_id: str, default: str = "eli5") -> str:
    """Suggest the perspective mode this learner uses most; fall back to a default."""
    counts = get_profile(user_id).get("mode_counts", {})
    return max(counts, key=counts.get) if counts else default
