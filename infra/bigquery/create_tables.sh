#!/usr/bin/env bash
# Usage: PROJECT_ID=my-project ./create_tables.sh
set -e
: "${PROJECT_ID:?set PROJECT_ID}"
bq --project_id="$PROJECT_ID" mk --dataset --location=US deepdive || true
bq --project_id="$PROJECT_ID" mk --table deepdive.interaction_events infra/bigquery/interaction_events.json || true
bq --project_id="$PROJECT_ID" mk --table deepdive.video_segments infra/bigquery/video_segments.json || true
sed "s/PROJECT_ID/$PROJECT_ID/g" infra/bigquery/confusion_by_segment.sql | bq --project_id="$PROJECT_ID" query --use_legacy_sql=false
# Then: create Pub/Sub topic "interaction-events" and a BigQuery subscription targeting deepdive.interaction_events
#   gcloud pubsub topics create interaction-events
#   gcloud pubsub subscriptions create interaction-events-bq --topic=interaction-events \
#     --bigquery-table=$PROJECT_ID:deepdive.interaction_events --use-table-schema
#   (grant the Pub/Sub service agent roles/bigquery.dataEditor on the dataset first)
