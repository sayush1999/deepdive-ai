-- Replace PROJECT_ID before running. Powers the creator "confusion heatmap".
CREATE OR REPLACE VIEW `PROJECT_ID.deepdive.confusion_by_segment` AS
SELECT
  video_id,
  CAST(FLOOR(timestamp_s / 30) * 30 AS INT64) AS segment_start_s,
  COUNT(*) AS questions,
  COUNT(DISTINCT user_id) AS learners,
  COUNTIF(answer_helpful = FALSE) AS unhelpful_answers,
  APPROX_TOP_COUNT(mode, 1)[OFFSET(0)].value AS top_mode
FROM `PROJECT_ID.deepdive.interaction_events`
GROUP BY video_id, segment_start_s;
