## vLLM Multi Model bench
This Repo's goal aims to benchmark LLM inference engines with multi model input by using this [dataset](https://huggingface.co/datasets/andynoodles/omnidoc-ocr-correction-bench).

The dataset consists 1.36k rows of prompt + images pairs, challenges inference engine's ability to decode images while prefill and decoding. Requires balance between CPU, GPU and target model's multimodel preprocess remote code.

## Get Started

#### Environment Setup

```bash 
uv venv 
source .venv/bin/activate
uv pip install -r requirements.txt
```

Benchmark Platform
```bash
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.71.05              Driver Version: 595.71.05      CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GB10                    On  |   0000000F:01:00.0 Off |                  N/A |
| N/A   35C    P8              4W /  N/A  | Not Supported          |      0%      Default |
+-----------------------------------------------------------------------------------------+
```

#### Dataset Download

```bash 
uv run download_dataset.py
```

#### Run Benchmark Scripts

The benchmark configurations are defined as Docker Compose files in the [`recipes/`](recipes/) directory.

```bash
sh ./bench.sh
```

## Results

Raw logs for all benchmarks can be found in the [`results/`](results/) directory.

| Benchmark | Throughput (tok/s) | Mean TTFT (ms) | Mean TPOT (ms) | Recipe |
|---|---|---|---|---|
| [eugr_vllm_FP8](results/eugr_vllm_FP8.txt) | 55.59 | 21897.79 | 242.17 | [eugr.FP8](recipes/docker-compose.eugr.FP8.yml) |
| [nv_vllm_FP8](results/nv_vllm_FP8.txt) | 52.36 | 27347.98 | 240.73 | [nv](recipes/docker-compose.nv.mtp.yml) |
| [nv_vllm_FP8_mtp](results/nv_vllm_FP8_mtp.txt) | 58.77 | 26274.58 | 212.47 | [nv](recipes/docker-compose.nv.yml) |
| [official_vllm_FP8c16](results/official_vllm_FP8c16.txt) | 60.05 | 14731.96 | 201.18 | [official.FP8](recipes/docker-compose.official.FP8.yml) |
| [official_vllm_FP8c20](results/official_vllm_FP8c20.txt) | 64.10 | 16279.92 | 216.03 | [official.FP8](recipes/docker-compose.official.FP8.yml) |
| [official_vllm_FP8c4](results/official_vllm_FP8c4.txt) | 37.86 | 10702.69 | 59.93 | [official.FP8](recipes/docker-compose.official.FP8.yml) |
| [official_vllm_FP8c8](results/official_vllm_FP8c8.txt) | 49.76 | 9400.06 | 115.42 | [official.FP8](recipes/docker-compose.official.FP8.yml) |
| [official_vllm_NVFP4c16](results/official_vllm_NVFP4c16.txt) | 66.35 | 14582.44 | 176.54 | [official.NVFP4](recipes/docker-compose.official.NVFP4.yml) |
| [official_vllm_NVFP4c20](results/official_vllm_NVFP4c20.txt) | 60.44 | 19053.13 | 227.82 | [official.NVFP4](recipes/docker-compose.official.NVFP4.yml) |
| [official_vllm_NVFP4c4](results/official_vllm_NVFP4c4.txt) | 42.45 | 6412.74 | 65.02 | [official.NVFP4](recipes/docker-compose.official.NVFP4.yml) |
| [official_vllm_NVFP4c8](results/official_vllm_NVFP4c8.txt) | 55.32 | 9790.24 | 98.43 | [official.NVFP4](recipes/docker-compose.official.NVFP4.yml) |