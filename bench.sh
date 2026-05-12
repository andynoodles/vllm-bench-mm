#!/bin/bash
MODEL_SOURCE="RedHatAI/Qwen3.6-35B-A3B-NVFP4"
BASE_URL="http://localhost:8000"
CONCURRENCY=20
DATASET="omnidoc_vllm.jsonl"


TOTAL_LINES=$(wc -l < "$DATASET")

echo "Running vLLM benchmark with model: $MODEL_NAME on $TOTAL_LINES prompts"
uv run vllm bench serve \
    --backend openai-chat \
    --trust-remote-code \
    --model "$MODEL_SOURCE" \
    --dataset-path "$DATASET" \
    --dataset-name custom_mm \
    --base-url "$BASE_URL" \
    --endpoint /v1/chat/completions \
    --max-concurrency $CONCURRENCY \
    --num-prompts "$TOTAL_LINES" \
    --temperature 0.7 \
    --top-p 0.80 \
    --top-k 16 \
    --min-p 0.0 \
    --presence-penalty 1.5 \
    --repetition-penalty 1.0
