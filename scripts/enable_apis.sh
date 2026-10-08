#!/usr/bin/env bash
gcloud services enable \
  aiplatform.googleapis.com run.googleapis.com storage.googleapis.com \
  firestore.googleapis.com pubsub.googleapis.com workflows.googleapis.com \
  speech.googleapis.com texttospeech.googleapis.com videointelligence.googleapis.com \
  documentai.googleapis.com transcoder.googleapis.com artifactregistry.googleapis.com \
  cloudbuild.googleapis.com secretmanager.googleapis.com \
  translate.googleapis.com bigquery.googleapis.com
