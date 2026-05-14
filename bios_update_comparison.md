# Benchmark Performance Comparison (BIOS & Driver Updates)

This table compares the performance across three configurations:
1. **580 Driver (Original)**: Base performance before BIOS update.
2. **580 Driver (BIOS Update)**: Performance after BIOS update.
3. **595 Driver**: Performance with the updated NVIDIA 595 driver.

*(Note: For throughput, higher is better. For duration and latency, lower is better. Positive percentages indicate an improvement compared to the original 580 Driver).*

### Concurrency 16 (`officail_vllm_FP8c16.txt`)

| Metric | 580 Driver (Original) | 580 Driver (BIOS Update) | 595 Driver | Imprv. (BIOS vs Orig) | Imprv. (595 vs Orig) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Benchmark duration (s)** | 130.98 | 129.50 | 127.89 | **+ 1.13%** | **+ 2.36%** |
| **Total token throughput (tok/s)** | 806.29 | 815.45 | 825.73 | **+ 1.14%** | **+ 2.41%** |
| **Output token throughput (tok/s)** | 58.64 | 59.30 | 60.05 | **+ 1.13%** | **+ 2.40%** |
| **Mean TTFT (ms)** | 15462.13 | 16337.48 | 14731.96 | **- 5.66%** | **+ 4.72%** |
| **Mean TPOT (ms)** | 204.53 | 196.75 | 201.18 | **+ 3.80%** | **+ 1.64%** |
| **Mean ITL (ms)** | 203.86 | 196.14 | 200.40 | **+ 3.79%** | **+ 1.70%** |

---

### Concurrency 20 (`officail_vllm_FP8c20.txt`)

| Metric | 580 Driver (Original) | 580 Driver (BIOS Update) | 595 Driver | Imprv. (BIOS vs Orig) | Imprv. (595 vs Orig) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Benchmark duration (s)** | 134.42 | 128.53 | 119.82 | **+ 4.38%** | **+ 10.86%** |
| **Total token throughput (tok/s)** | 785.65 | 821.65 | 881.36 | **+ 4.58%** | **+ 12.18%** |
| **Output token throughput (tok/s)** | 57.14 | 59.75 | 64.10 | **+ 4.57%** | **+ 12.18%** |
| **Mean TTFT (ms)** | 18840.27 | 18070.67 | 16279.92 | **+ 4.08%** | **+ 13.59%** |
| **Mean TPOT (ms)** | 243.09 | 231.31 | 216.03 | **+ 4.85%** | **+ 11.13%** |
| **Mean ITL (ms)** | 242.14 | 230.50 | 215.27 | **+ 4.81%** | **+ 11.09%** |

### Summary
* **Driver 595 delivers the highest performance:** Across both concurrency levels, updating to the 595 driver yields the best results compared to the original setup.
* **Concurrency 16:** The 595 driver shows a solid ~2.4% bump in general throughput and a 4.7% improvement in TTFT.
* **Concurrency 20:** The 595 driver demonstrates significant gains over the original 580 driver, boosting throughput by **over 12%**, reducing duration by nearly **11%**, and slashing latency metrics (TTFT, TPOT, ITL) by **11-13%**. This heavily outperforms the standalone BIOS update, which maxed out around 4-5% improvements.
