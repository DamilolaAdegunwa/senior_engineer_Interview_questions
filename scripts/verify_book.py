#!/usr/bin/env python3
"""
Integrity and Verification Test Suite for:
10,000 Senior Engineer Interview Questions Textbook
"""

import os
import sys
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
VOLUMES_DIR = BASE_DIR / "volumes"
EXPLORER_DIR = BASE_DIR / "interactive_explorer"

def verify():
    print("==================================================")
    print("VERIFYING 10,000 SENIOR ENGINEER INTERVIEW QUESTIONS")
    print("==================================================")
    
    # 1. Check Volume Files
    volume_files = sorted(list(VOLUMES_DIR.glob("volume_*.md")))
    print(f"[*] Found {len(volume_files)} Volume Markdown files.")
    assert len(volume_files) == 10, f"Expected 10 volumes, got {len(volume_files)}"
    
    # 2. Check Questions in Volumes
    seen_ids = set()
    total_found = 0
    
    q_pattern = re.compile(r"^### Question (\d+): (.*)$", re.MULTILINE)
    
    for vf in volume_files:
        with open(vf, "r", encoding="utf-8") as f:
            content = f.read()
        
        matches = list(q_pattern.finditer(content))
        print(f"[*] {vf.name}: contains {len(matches)} questions.")
        assert len(matches) == 1000, f"Expected 1000 questions in {vf.name}, found {len(matches)}"
        
        for m in matches:
            qid = int(m.group(1))
            assert qid not in seen_ids, f"Duplicate Question ID detected: {qid}"
            seen_ids.add(qid)
            total_found += 1
            
    print(f"[*] Total unique questions parsed: {total_found}")
    assert total_found == 10000, f"Expected 10,000 questions, found {total_found}"
    
    # Verify sequence integrity [1..10000]
    expected_ids = set(range(1, 10001))
    missing = expected_ids - seen_ids
    assert len(missing) == 0, f"Missing questions: {sorted(list(missing))[:10]}"
    print("[*] Sequence check PASSED: Contiguous [00001 .. 10000] with zero gaps!")
    
    # 3. Check Search Index
    index_file = EXPLORER_DIR / "questions_index.json"
    assert index_file.exists(), "Missing questions_index.json"
    with open(index_file, "r", encoding="utf-8") as f:
        idx_data = json.load(f)
    print(f"[*] Search index contains {len(idx_data)} indexed questions.")
    assert len(idx_data) == 10000, f"Index length mismatch: {len(idx_data)} != 10000"
    
    # Verify index mapping matches
    assert idx_data[0]["id"] == 1
    assert idx_data[-1]["id"] == 10000
    print("[*] Index integrity PASSED!")
    
    print("==================================================")
    print("ALL VERIFICATION CHECKS PASSED SUCCESSFULLY (10,000 / 10,000)!")
    print("==================================================")

if __name__ == "__main__":
    verify()
