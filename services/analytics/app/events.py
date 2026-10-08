import json, os, time, uuid
from google.cloud import pubsub_v1

_publisher = None

def log_event(video_id: str, timestamp_s: float, mode: str, language: str,
              question: str, user_id: str, latency_ms: int | None = None,
              answer_helpful: bool | None = None) -> None:
    """Publish an interaction event; a Pub/Sub BigQuery subscription lands it in interaction_events."""
    global _publisher
    if _publisher is None:
        _publisher = pubsub_v1.PublisherClient()
    topic = _publisher.topic_path(os.environ["GCP_PROJECT_ID"], os.environ.get("PUBSUB_EVENTS_TOPIC", "interaction-events"))
    event = {
        "event_id": str(uuid.uuid4()),
        "ts": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        "video_id": video_id,
        "timestamp_s": timestamp_s,
        "mode": mode,
        "language": language,
        "question": question,
        "user_id": user_id,
        "latency_ms": latency_ms,
        "answer_helpful": answer_helpful,
    }
    _publisher.publish(topic, json.dumps(event).encode("utf-8"))
