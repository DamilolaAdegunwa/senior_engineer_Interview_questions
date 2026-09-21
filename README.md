# 10,000 Senior Engineer Interview Questions

### *The Definitive Systems, Concurrency, and Infrastructure Engineering Field Manual*

<p align="center">
  <img src="https://img.shields.io/badge/Questions-10%2C000_Verified-blue?style=for-the-badge&logo=codeforces" alt="Questions Count">
  <img src="https://img.shields.io/badge/Volumes-10_Volumes-success?style=for-the-badge&logo=gitbook" alt="10 Volumes">
  <img src="https://img.shields.io/badge/Chapters-100_Chapters-orange?style=for-the-badge&logo=bookstack" alt="100 Chapters">
  <img src="https://img.shields.io/badge/Target_Level-Staff_%2F_Principal_%2F_L6%2B-purple?style=for-the-badge&logo=target" alt="Level Staff">
  <img src="https://img.shields.io/badge/Style-O'Reilly_Field_Manual-red?style=for-the-badge" alt="O'Reilly Style">
</p>

---

```
                       _.-""""-._
                     .'          `.
                    /   O      O   \
                   |    ___  ___    |
                   |   /   \/   \   |
                   \   \___/\___/   /
                    '.            .'
                      `'-......-'`
         [ The Honey Badger of Distributed Systems ]
   "It does not care about your network partitions or split brains."
```

---

## Overview

Welcome to **10,000 Senior Engineer Interview Questions**, the comprehensive, definitive systems and infrastructure engineering textbook modeled after classic O'Reilly technical field manuals. 

Most interview preparation repositories focus on standard junior/mid-level algorithmic puzzles (LeetCode medium/hard). This textbook focuses exclusively on **Staff, Principal, and Senior Infrastructure Engineering (L5/L6/L7+)**:
- **Hardware-level mechanical sympathy**: Cache lines (64 bytes), false sharing, MESI invalidations, NUMA node binding, acquire-release memory fences.
- **Lock-free & wait-free concurrency**: ABA mitigation, hazard pointers, Epoch-Based Reclamation (EBR), quiescent states, and seqlocks.
- **Distributed consensus & fault tolerance**: Raft joint consensus, Multi-Paxos phase 1/2 optimizations, Byzantine fault tolerance, Hybrid Logical Clocks (HLC), and CRDTs.
- **Storage engine internals**: LSM-tree write amplification, leveled vs tiered compaction, Blink-trees, ARC/Clock-Pro buffer pool management, ARIES WAL recovery, and HNSW vector indexing.
- **Kernel bypass & networking**: io_uring submission/completion rings, epoll edge-triggered semantics, zero-copy `splice()`, TCP BBR congestion control, and QUIC flow control.

Every single question is accompanied by **Starter Architectures**, **Invariants & Complexity Bounds**, **Subtle Edge Cases & Concurrency Traps**, **Chaos & Stress Testing Harnesses**, and **Staff-Level Trade-offs**.

---

## Curriculum Architecture (10 Volumes, 100 Chapters, 10,000 Questions)

The complete syllabus is organized into 10 structured Volumes of 1,000 questions each, subdivided into 100 dedicated technical chapters:

| Volume | Title & Focus | Question Range |
| :--- | :--- | :--- |
| **[Volume I](volumes/volume_01_concurrency_and_memory_models.md)** | **Concurrency, Memory Models, and Lock-Free Primitives**<br>*Hardware Atomics, Cache Coherence, Memory Reclamation, and Multi-Core Synchronization* | `Q00001 – Q01000` |
| **[Volume II](volumes/volume_02_distributed_systems_and_consensus.md)** | **Distributed Systems, Consensus, and Replication**<br>*Paxos, Raft, Byzantine Fault Tolerance, Distributed Clocks, and CRDTs* | `Q01001 – Q02000` |
| **[Volume III](volumes/volume_03_storage_engines_and_databases.md)** | **Storage Engines, Databases, and Indexing Internals**<br>*LSM-Trees, B-Trees, Buffer Pools, Write-Ahead Logs, MVCC, and Vector Search* | `Q02001 – Q03000` |
| **[Volume IV](volumes/volume_04_networking_protocols_and_io.md)** | **High-Performance Networking, Protocols, and I/O**<br>*Kernel Bypass, epoll, io_uring, Zero-Copy I/O, TCP Internals, and QUIC/HTTP3* | `Q03001 – Q04000` |
| **[Volume V](volumes/volume_05_streaming_and_event_architectures.md)** | **Distributed Streaming, Messaging, and Event Architectures**<br>*Commit Logs, Kafka/Pulsar Internals, Exactly-Once Semantics, and Temporal Joins* | `Q04001 – Q05000` |
| **[Volume VI](volumes/volume_06_operating_systems_and_runtimes.md)** | **Operating Systems, Memory Architecture, and Runtimes**<br>*Custom Allocators, Virtual Memory, Linux Kernel Internals, eBPF, and Garbage Collection* | `Q05001 – Q06000` |
| **[Volume VII](volumes/volume_07_algorithms_and_probabilistic_data.md)** | **Advanced Algorithms, Graph Systems, and Probabilistic Structures**<br>*Suffix Automata, Merkle Trees, Cuckoo Filters, HyperLogLog, and Dynamic Graphs* | `Q06001 – Q07000` |
| **[Volume VIII](volumes/volume_08_caching_and_rate_limiting.md)** | **Distributed Caching, Cache Coherence, and Rate Limiting**<br>*Cache Stampede, Lease Tokens, Sliding Window Rate Limiters, and Distributed Locks* | `Q07001 – Q08000` |
| **[Volume IX](volumes/volume_09_scalable_compute_and_schedulers.md)** | **Scalable Compute, DAG Orchestration, and Actor Runtimes**<br>*Work-Stealing Schedulers, Kubernetes Internals, Actor Models, and MicroVM Sandboxes* | `Q08001 – Q09000` |
| **[Volume X](volumes/volume_10_security_and_resilient_architectures.md)** | **Security, Cryptographic Protocols, and Resilient Architecture**<br>*KMS Envelope Encryption, SPIFFE/SPIRE mTLS, Zero-Knowledge, and Blast Radius Mitigation* | `Q09001 – Q10000` |

See **[BOOK.md](BOOK.md)** for the complete master syllabus, chapter-by-chapter breakdowns, and cross-volume topic indices.

---

## Anatomy of an O'Reilly Textbook Question

Every question in this textbook adheres to the following rigorous engineering template:

```markdown
### Question 00126: Implement a File-Backed LRU Cache with Crash Recovery

**Tags**: `[Vol 1] [Chapter 2] [Staff/Principal Engineering]` | **Target Level**: `Senior / Staff / Principal Infrastructure Engineer`

#### Problem Statement & System Constraints
- Maintain an in-memory key-to-value index backed by append-only segment logs on non-volatile storage.
- Support dynamic segment compaction while concurrently serving reads with p99 latency < 100μs.
- Guarantee crash consistency: on sudden power failure or ungraceful shutdown, replay the write-ahead log and discard partial tail records.

#### Starter Architecture & Algorithmic Design
- Decompose into an in-memory hash map index pointing to disk segment offsets plus an append-only WAL.
- Eviction runs asynchronously when segment file count exceeds threshold: write new compacted segments, atomic rename, and swap in-memory pointers.

#### Invariants & Complexity Guarantees
- Time Complexity: O(1) reads and amortized O(1) writes.
- Space Complexity: O(N) index memory, bounded disk amplification factor < 2.5x.
- Crash Recovery Bound: MTTR < 500ms for journals up to 1GB.

#### Subtle Edge Cases & Concurrency Traps
- Crash occurs mid-append leaving a torn, partially written record.
- Background compaction races with eviction, deleting a segment referenced by an in-flight read.
- Duplicate journal entries generated when retried writes succeed before failover acknowledgment.

#### Verification, Stress Testing & Chaos Harness
- Automated kill-injection: Terminate process with SIGKILL at randomized byte offsets during heavy write bursts.
- Concurrency fuzzing: Run thread sanitizers asserting zero read-write races on in-flight segment file descriptors.

#### Staff-Level Trade-offs & Deep Discussion
- The trade-off between write amplification and space reclamation frequency.
- Staff engineers explain why pure in-place updates fail on modern NVMe drives due to flash translation layer (FTL) block wear, justifying append-only segment models.
```

---

## Interactive Exploration Tools

### 1. Terminal Search CLI (`search_cli.py`)
Quickly search across all 10,000 questions, filter by volume, chapter, or keyword, and view full question breakdowns directly in your terminal:

```bash
# Search for topics related to Raft consensus
python3 interactive_explorer/search_cli.py --query "Raft" --limit 10

# Filter by Volume (e.g. Volume 3: Storage Engines)
python3 interactive_explorer/search_cli.py --volume 3 --query "LSM"

# Display full question breakdown by ID
python3 interactive_explorer/search_cli.py --id 126
```

### 2. Standalone Web Viewer (`web_viewer.html`)
An offline-first, zero-dependency interactive browser app with instant search, volume filtering, pagination, and direct links to volume markdown files:

```bash
# Open directly in your browser:
open interactive_explorer/web_viewer.html

# Or serve via local HTTP:
python3 -m http.server 8000
# Visit: http://localhost:8000/interactive_explorer/web_viewer.html
```

---

## Verification & Integrity Test Suite

The integrity of this textbook is verified via automated property tests confirming:
- Exactly 10,000 questions exist with zero duplicate IDs or titles.
- Contiguous sequence spanning `00001` through `10000` without gaps.
- All 10 Volume files contain exactly 1,000 questions each.
- Search index maps 10,000 valid questions.

Run the verification test suite locally:
```bash
python3 scripts/verify_book.py
```

---

## The Staff+ Interview Rubric

When evaluating candidates on these questions, interviewers at top-tier companies measure four core competencies:

1. **Mechanical Sympathy**: Candidate understands CPU cache lines, store buffers, TLB misses, context-switch overhead, and memory alignment.
2. **Formal Linearizability**: Candidate defines the exact linearization point of atomic operations and identifies subtle ABA or memory reordering bugs.
3. **Resilience & Blast Radius**: Candidate isolates failures, prevents cascading retries, enforces backpressure, and guarantees bounded recovery times.
4. **Staff-Level Pragmatism**: Candidate articulates the trade-offs between simplicity and asymptotic optimization, factoring in operational debuggability and on-call cognitive load.

---

## License

This textbook and repository are open source and licensed under the [MIT License](LICENSE).
