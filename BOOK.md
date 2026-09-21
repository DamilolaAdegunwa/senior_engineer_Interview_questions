# 10,000 Senior Engineer Interview Questions
## *The Definitive Systems, Concurrency, and Infrastructure Engineering Field Manual*
### An O'Reilly-Style Production Textbook

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

## Master Table of Contents & Curriculum Map

This textbook contains **10,000 sequentially numbered, high-complexity engineering interview questions** designed specifically for Staff, Principal, and Senior Infrastructure Engineers at Tier-1 technology companies.

The curriculum is divided into **10 Volumes**, each comprising **10 specialized Chapters** (100 chapters total), with **100 deep questions per chapter** ($10 \times 10 \times 100 = 10,000$).

---

### [Volume I: Concurrency, Memory Models, and Lock-Free Primitives](volumes/volume_01_concurrency_and_memory_models.md)
*Hardware Atomics, Cache Coherence, Memory Reclamation, and Multi-Core Synchronization*  
**Questions 00001 – 01000**

- **[Chapter 1](volumes/volume_01_concurrency_and_memory_models.md#chapter-1-lock-free--wait-free-queues-stacks-and-deques)** (Q00001 – Q00100): Lock-Free & Wait-Free Queues, Stacks, and Deques (includes foundational reference questions Q1–Q25)
- **[Chapter 2](volumes/volume_01_concurrency_and_memory_models.md#chapter-2-concurrent-hash-tables-sets-and-skip-lists)** (Q00101 – Q00200): Concurrent Hash Tables, Sets, and Skip Lists (includes foundational reference questions Q26–Q200)
- **[Chapter 3](volumes/volume_01_concurrency_and_memory_models.md#chapter-3-memory-reclamation-hazard-pointers-ebr-and-qsbr)** (Q00201 – Q00300): Memory Reclamation: Hazard Pointers, EBR, and QSBR
- **[Chapter 4](volumes/volume_01_concurrency_and_memory_models.md#chapter-4-read-copy-update-rcu-seqlocks-and-asymmetric-synchronization)** (Q00301 – Q00400): Read-Copy-Update (RCU), Seqlocks, and Asymmetric Synchronization
- **[Chapter 5](volumes/volume_01_concurrency_and_memory_models.md#chapter-5-memory-models-cache-coherence-and-mesi-protocols)** (Q00401 – Q00500): Memory Models (C++11/Rust/Java), Cache Coherence, and MESI/MOESI Protocols
- **[Chapter 6](volumes/volume_01_concurrency_and_memory_models.md#chapter-6-atomic-hardware-primitives-cas-llsc-and-memory-fences)** (Q00501 – Q00600): Atomic Hardware Primitives: CAS, LL/SC, Memory Fences, and DWCAS
- **[Chapter 7](volumes/volume_01_concurrency_and_memory_models.md#chapter-7-high-contention-locking-mcs-clh-flat-combining-and-ticket-locks)** (Q00601 – Q00700): High-Contention Locking: MCS, CLH, Flat Combining, and Ticket Locks
- **[Chapter 8](volumes/volume_01_concurrency_and_memory_models.md#chapter-8-software-transactional-memory-stm--optimistic-concurrency)** (Q00701 – Q00800): Software Transactional Memory (STM) & Optimistic Concurrency
- **[Chapter 9](volumes/volume_01_concurrency_and_memory_models.md#chapter-9-work-stealing-task-schedulers-chase-lev-deques-and-fiber-runtimes)** (Q00801 – Q00900): Work-Stealing Task Schedulers, Chase-Lev Deques, and Fiber Runtimes
- **[Chapter 10](volumes/volume_01_concurrency_and_memory_models.md#chapter-10-asynchronous-event-loops-green-threads-and-coroutine-runtimes)** (Q00901 – Q01000): Asynchronous Event Loops, Green Threads, and Coroutine Schedulers

---

### [Volume II: Distributed Systems, Consensus, and Replication](volumes/volume_02_distributed_systems_and_consensus.md)
*Paxos, Raft, Byzantine Fault Tolerance, Distributed Clocks, and CRDTs*  
**Questions 01001 – 02000**

- **Chapter 11** (Q01001 – Q01100): Consensus Protocols: Multi-Paxos, Flexible Paxos, and Fast Paxos
- **Chapter 12** (Q01101 – Q01200): Raft Consensus: Log Replication, Joint Consensus, and Pre-Vote
- **Chapter 13** (Q01201 – Q01300): Viewstamped Replication Revisited and ZooKeeper Atomic Broadcast (Zab)
- **Chapter 14** (Q01301 – Q01400): Byzantine Fault Tolerance: PBFT, Tendermint, and HotStuff
- **Chapter 15** (Q01401 – Q01500): Distributed Time, Vector Clocks, Hybrid Logical Clocks, and TrueTime
- **Chapter 16** (Q01501 – Q01600): Conflict-Free Replicated Data Types (CRDTs): State-Based & Op-Based
- **Chapter 17** (Q01601 – Q01700): Distributed Transactions: Two-Phase Commit (2PC), Sagas, and Percolator
- **Chapter 18** (Q01701 – Q01800): Partitioning, Consistent Hashing Rings, and Sharding Topologies
- **Chapter 19** (Q01801 – Q01900): Cluster Membership & Gossip Protocols: SWIM and Failure Detectors
- **Chapter 20** (Q01901 – Q02000): Quorum Systems, Leader Leases, Fencing Tokens, and Split-Brain Defense

---

### [Volume III: Storage Engines, Databases, and Indexing Internals](volumes/volume_03_storage_engines_and_databases.md)
*LSM-Trees, B-Trees, Buffer Pools, Write-Ahead Logs, MVCC, and Vector Search*  
**Questions 02001 – 03000**

- **Chapter 21** (Q02001 – Q02100): Log-Structured Merge (LSM) Trees: Memtable, Commit Log, and SSTable
- **Chapter 22** (Q02101 – Q02200): SSTable Compaction Dynamics: Leveled, Tiered, and Space Amplification
- **Chapter 23** (Q02201 – Q02300): Classical B+ Trees, Blink-Trees, and Cache-Conscious CSS-Trees
- **Chapter 24** (Q02301 – Q02400): Buffer Pool Architecture: 2Q, ARC, Clock-Pro, and Page Eviction
- **Chapter 25** (Q02401 – Q02500): Multi-Version Concurrency Control (MVCC) and Vacuuming Mechanics
- **Chapter 26** (Q02501 – Q02600): Write-Ahead Logging (WAL), ARIES Recovery, and Group Commit
- **Chapter 27** (Q02601 – Q02700): Relational Query Optimization: Cost-Based Planners and Join Ordering
- **Chapter 28** (Q02701 – Q02800): Columnar Storage Formats: Parquet, ORC, and Vectorized Execution
- **Chapter 29** (Q02801 – Q02900): High-Dimensional Vector Search: HNSW Graphs and Product Quantization
- **Chapter 30** (Q02901 – Q03000): Distributed Storage: Chunk Servers, Metadata Catalogs, and Erasure Coding

---

### [Volume IV: High-Performance Networking, Protocols, and I/O](volumes/volume_04_networking_protocols_and_io.md)
*Kernel Bypass, epoll, io_uring, Zero-Copy I/O, TCP Internals, and QUIC/HTTP3*  
**Questions 03001 – 04000**

- **Chapter 31** (Q03001 – Q03100): Async I/O Multiplexing: epoll (Edge vs Level Triggered), kqueue, io_uring
- **Chapter 32** (Q03101 – Q03200): Zero-Copy Networking: splice(), sendfile(), and AF_XDP Kernel Bypass
- **Chapter 33** (Q03201 – Q03300): TCP Stack Engineering: Congestion Control (BBR, CUBIC), Window Scaling
- **Chapter 34** (Q03301 – Q03400): HTTP/2 & HTTP/3: Multiplexing, Flow Control, HPACK/QPACK, and HOL Blocking
- **Chapter 35** (Q03401 – Q03500): High-Performance RPC & Wire Protocols: Protobuf, FlatBuffers, Cap'n Proto
- **Chapter 36** (Q03501 – Q03600): WebSocket & Bidirectional Streaming Gateways: Heartbeats and Multiplexing
- **Chapter 37** (Q03601 – Q03700): DNS Resolution, Anycast BGP Routing, and CDN Origin Shielding
- **Chapter 38** (Q03701 – Q03800): TLS 1.3 Optimization: 0-RTT Early Data, Resumption, and Certificate Chains
- **Chapter 39** (Q03801 – Q03900): Network Backpressure, TCP Socket Buffers, and Dropping Policies
- **Chapter 40** (Q03901 – Q04000): Distributed Load Balancing: Maglev Consistent Hashing, Power of Two Choices

---

### [Volume V: Distributed Streaming, Messaging, and Event Architectures](volumes/volume_05_streaming_and_event_architectures.md)
*Commit Logs, Kafka/Pulsar Internals, Exactly-Once Semantics, and Temporal Joins*  
**Questions 04001 – 05000**

- **Chapter 41** (Q04001 – Q04100): Commit Log Messaging: Kafka & Apache Pulsar Broker Architecture
- **Chapter 42** (Q04101 – Q04200): Partition Rebalancing, Group Coordinators, and Cooperative Assignors
- **Chapter 43** (Q04201 – Q04300): Exactly-Once Processing (EOS): Idempotent Producers and Two-Phase Log Commits
- **Chapter 44** (Q04301 – Q04400): Stream Temporal Joins, Watermarks, Event Time vs Ingestion Time
- **Chapter 45** (Q04401 – Q04500): Stream State Stores: Embedded RocksDB, Changelog Compaction, and Standbys
- **Chapter 46** (Q04501 – Q04600): Priority, Delayed, and Dead-Letter Queue Architectures
- **Chapter 47** (Q04601 – Q04700): High-Throughput Stream Deduplication: Bloom-Assisted vs Exact Window Filters
- **Chapter 48** (Q04701 – Q04800): Backpressure Propagation across Distributed Pipeline Stages
- **Chapter 49** (Q04801 – Q04900): Change Data Capture (CDC): Transaction Log Mining, Snapshotting, and Debezium
- **Chapter 50** (Q04901 – Q05000): Event-Sourcing & CQRS: Event Stores, Projection Engines, and Replays

---

### [Volume VI: Operating Systems, Memory Architecture, and Runtimes](volumes/volume_06_operating_systems_and_runtimes.md)
*Custom Allocators, Virtual Memory, Linux Kernel Internals, eBPF, and Garbage Collection*  
**Questions 05001 – 06000**

- **Chapter 51** (Q05001 – Q05100): Custom Memory Allocators: Slab, Buddy System, Arena, and TLSF
- **Chapter 52** (Q05101 – Q05200): Virtual Memory Internals: Multi-Level Page Tables, Hugepages, and TLB Shootdowns
- **Chapter 53** (Q05201 – Q05300): Linux Kernel Architecture: System Call Path, VFS, Inodes, and Page Cache
- **Chapter 54** (Q05301 – Q05400): eBPF Programs: XDP Packet Filters, kprobes, tracepoints, and Ring Buffers
- **Chapter 55** (Q05401 – Q05500): Garbage Collection Internals: Generational Hypothesis, Card Tables, ZGC/Shenandoah
- **Chapter 56** (Q05501 – Q05600): JIT Compilation Runtimes: Tiered Compilation, On-Stack Replacement, Deopt
- **Chapter 57** (Q05601 – Q05700): Inter-Process Communication (IPC): Shared Memory Rings, Unix Domain Sockets, futex
- **Chapter 58** (Q05701 – Q05800): Linux Containers & Isolation: cgroups v2, Namespaces, seccomp, and rootfs
- **Chapter 59** (Q05801 – Q05900): Signal Handling, Async-Signal Safety, Thread Cancellation, and Core Dumps
- **Chapter 60** (Q05901 – Q06000): Memory-Mapped I/O (mmap), MAP_SHARED vs MAP_PRIVATE, and Page Eviction

---

### [Volume VII: Advanced Algorithms, Graph Systems, and Probabilistic Structures](volumes/volume_07_algorithms_and_probabilistic_data.md)
*Suffix Automata, Merkle Trees, Cuckoo Filters, HyperLogLog, and Dynamic Graphs*  
**Questions 06001 – 07000**

- **Chapter 61** (Q06001 – Q06100): Compressed Text Indexing: Suffix Automata, Suffix Trees, and FM-Index
- **Chapter 62** (Q06101 – Q06200): Merkle Trees, Verkle Trees, and Polynomial Commitment Schemes
- **Chapter 63** (Q06201 – Q06300): Probabilistic Membership: Scalable Bloom Filters, Cuckoo Filters, Quotient Filters
- **Chapter 64** (Q06301 – Q06400): Cardinality & Frequency Sketches: HyperLogLog++, Count-Min Sketch, Top-K Heavy Hitters
- **Chapter 65** (Q06401 – Q06500): Roaring Bitmaps, BitSliced Indices, and High-Throughput Set Operations
- **Chapter 66** (Q06501 – Q06600): Dynamic Graph Algorithms: Dynamic Connectivity, Tarjan SCC, Maximum Flow
- **Chapter 67** (Q06601 – Q06700): Spatial Indexing: R*-Trees, Geohash Bounding Boxes, and Uber H3 Hexagonal Grids
- **Chapter 68** (Q06701 – Q06800): Persistent & Functional Data Structures: Finger Trees, Bagwell HAMT, Treaps
- **Chapter 69** (Q06801 – Q06900): Network Flow & Bipartite Matching: Dinic Algorithm, Push-Relabel, Hopcroft-Karp
- **Chapter 70** (Q06901 – Q07000): Distributed Graph Processing: Bulk Synchronous Parallel (BSP), Pregel, Partitioning

---

### [Volume VIII: Distributed Caching, Cache Coherence, and Rate Limiting](volumes/volume_08_caching_and_rate_limiting.md)
*Cache Stampede, Lease Tokens, Sliding Window Rate Limiters, and Distributed Locks*  
**Questions 07001 – 08000**

- **Chapter 71** (Q07001 – Q07100): Distributed Cache Topologies: Cache-Aside, Write-Through, Write-Behind, Near-Cache
- **Chapter 72** (Q07101 – Q07200): Cache Invalidation Mechanics: Lease Tokens, Invalidation Buses, and Version Vectors
- **Chapter 73** (Q07201 – Q07300): Thundering Herd & Cache Stampede: Mutex Locking, Probabilistic Early Expiration
- **Chapter 74** (Q07301 – Q07400): Distributed Rate Limiting: Token Bucket, Leaky Bucket, Sliding Window Counter
- **Chapter 75** (Q07401 – Q07500): Hierarchical & Tiered Rate Limiting: Local Token Borrowing and Global Sync
- **Chapter 76** (Q07501 – Q07600): Cache Memory Layout: Slab Allocators in Memcached/Redis, Fragmentation Mitigation
- **Chapter 77** (Q07601 – Q07700): Multi-Region CDN Caching: Origin Shielding, Tiered Purging, Stale-While-Revalidate
- **Chapter 78** (Q07701 – Q07800): Distributed Locks: Redlock Validation, Chubby Locks, and ZooKeeper Fencing Tokens
- **Chapter 79** (Q07801 – Q07900): Distributed Session State: Sticky Sessions vs Replicated Encrypted Cookies
- **Chapter 80** (Q07901 – Q08000): In-Memory Key-Value Stores: Thread-per-Core Architecture (Dragonfly, Redis 7+)

---

### [Volume IX: Scalable Compute, DAG Orchestration, and Actor Runtimes](volumes/volume_09_scalable_compute_and_schedulers.md)
*Work-Stealing Schedulers, Kubernetes Internals, Actor Models, and MicroVM Sandboxes*  
**Questions 08001 – 09000**

- **Chapter 81** (Q08001 – Q08100): Work-Stealing DAG Task Schedulers: Dynamic Task Graphs and Barrier Synchronization
- **Chapter 82** (Q08101 – Q08200): Cluster Schedulers: Kubernetes kube-scheduler, Borg Priority Preemption, DRF
- **Chapter 83** (Q08201 – Q08300): Actor Model Runtimes: Akka/Orleans Virtual Actors, Supervision Trees, Mailboxes
- **Chapter 84** (Q08301 – Q08400): Large-Scale Distributed Shuffle: External Sorting, MapReduce Partitions, Spill-to-Disk
- **Chapter 85** (Q08401 – Q08500): Heterogeneous Compute: GPU Kernel Offloading, Host-Device Memory Pipelining
- **Chapter 86** (Q08501 – Q08600): Durable Workflow Engines: Temporal, Cadence, Event History Replay, and Activities
- **Chapter 87** (Q08601 – Q08700): Resilient Worker Pools: Dynamic Autoscaling, Graceful Draining, and Spot Preemption
- **Chapter 88** (Q08701 – Q08800): Distributed Batch Processing: Straggler Mitigation, Speculative Execution
- **Chapter 89** (Q08801 – Q08900): Serverless Sandboxes: Firecracker microVM Bootstrapping, Snapshot-Resume
- **Chapter 90** (Q08901 – Q09000): Distributed Query Plan Compilation: Codegen, Volcano Iterator vs Vectorized Engine

---

### [Volume X: Security, Cryptographic Protocols, and Resilient Architecture](volumes/volume_10_security_and_resilient_architectures.md)
*KMS Envelope Encryption, SPIFFE/SPIRE mTLS, Zero-Knowledge, and Blast Radius Mitigation*  
**Questions 09001 – 10000**

- **Chapter 91** (Q09001 – Q09100): Distributed Key Management & Envelope Encryption: KMS, HSM, Key Rotation
- **Chapter 92** (Q09101 – Q09200): Mutual TLS (mTLS) & Workload Identity: SPIFFE/SPIRE, Envoy Sidecars, X.509 SVIDs
- **Chapter 93** (Q09201 – Q09300): Zero-Knowledge Verification: Groth16, PLONK, Non-Interactive Proofs in Systems
- **Chapter 94** (Q09301 – Q09400): Cryptographic Primitives in Infrastructure: Shamir Secret Sharing, Multi-Party Auth
- **Chapter 95** (Q09401 – Q09500): Modern Token Authentication: PASETO, Macaroons with Caveats, Scoped Delegations
- **Chapter 96** (Q09501 – Q09600): DDoS Mitigation at Scale: SYN Flood Cookies, BGP Flowspec, Anycast Scrubbing
- **Chapter 97** (Q09601 – Q09700): Blast Radius Isolation: Cell-Based Architectures, Shuffled Sharding, Bulkheads
- **Chapter 98** (Q09701 – Q09800): Canary Deployments & Automated Rollbacks: Metric Anomaly Detection, Traffic Shifting
- **Chapter 99** (Q09801 – Q09900): High-Availability Failover: Split-Brain Mitigation, Quorum Loss Bootstrapping
- **Chapter 100** (Q09901 – Q10000): Staff & Principal Architecture Defense: Technical RFCs, Failure Mode Effects Analysis

---

## The Staff & Principal Assessment Rubric

Candidates in senior live-coding and infrastructure architecture rounds are evaluated against four non-negotiable vectors:

1. **Mechanical Sympathy & Cache Invariants**: Does the candidate reason about cache lines (64 bytes), false sharing, NUMA locality, memory fences, instruction pipelines, and CPU branch prediction?
2. **Linearizability & Correctness Proofs**: Can the candidate locate the precise linearization point of an operation, defend against ABA hazards, and write stress harnesses that surface lost wakeups?
3. **Failure Isolation & Blast Radius**: What happens when a disk fsync stalls for 30 seconds? When a network partition drops 50% of heartbeats? Does the system degrade gracefully or suffer a cascading collapse?
4. **Staff-Level Trade-offs**: Senior engineers choose algorithms that work; Staff and Principal engineers understand when *not* to use lock-freedom, when simplicity outweighs asymptotic gains, and how the operational footprint impacts on-call engineers.
