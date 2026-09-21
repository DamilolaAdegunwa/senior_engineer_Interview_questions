#!/usr/bin/env python3
"""
Interactive Terminal Search & Explorer for:
10,000 Senior Engineer Interview Questions
"""

import os
import sys
import json
import argparse
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = BASE_DIR / "interactive_explorer" / "questions_index.json"

# ANSI Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

def load_index():
    if not INDEX_FILE.exists():
        print(f"Index file not found: {INDEX_FILE}")
        sys.exit(1)
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def show_question(qid):
    index = load_index()
    match = next((item for item in index if item["id"] == qid), None)
    if not match:
        print(f"{YELLOW}Question #{qid} not found in index.{RESET}")
        return
    
    vol_path = BASE_DIR / match["file"]
    if not vol_path.exists():
        print(f"Volume file missing: {vol_path}")
        return
        
    with open(vol_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    pattern = re.compile(rf"(### Question {qid:05d}:.*?)(?=### Question|\Z)", re.DOTALL)
    m = pattern.search(content)
    if m:
        q_content = m.group(1).strip()
        print(f"\n{CYAN}{'=' * 75}{RESET}")
        print(f"{BOLD}{match['volume_title']}{RESET} | {DIM}{match['chapter_title']}{RESET}")
        print(f"{CYAN}{'=' * 75}{RESET}\n")
        print(q_content)
        print(f"\n{CYAN}{'=' * 75}{RESET}\n")
    else:
        print(f"Failed to extract question text for #{qid}.")

def search_questions(query=None, volume=None, chapter=None, limit=20):
    index = load_index()
    results = []
    
    q_lower = query.lower() if query else None
    
    for item in index:
        if volume and item["volume"] != volume:
            continue
        if chapter and item["chapter"] != chapter:
            continue
        if q_lower:
            searchable = f"{item['title']} {item['tags']} {item['chapter_title']}".lower()
            if q_lower not in searchable:
                continue
        results.append(item)
        
    print(f"\n{BOLD}Found {len(results)} questions matching criteria{RESET}")
    if query:
        print(f"Query: {GREEN}{query}{RESET}")
    if volume:
        print(f"Volume: {CYAN}{volume}{RESET}")
    print(f"{'-' * 75}")
    
    for item in results[:limit]:
        print(f"{BOLD}#{item['id']:05d}{RESET} [{CYAN}Vol {item['volume']}{RESET} Ch{item['chapter']:02d}] {item['title']}")
        print(f"       {DIM}Tags: {item['tags']}{RESET}")
        
    if len(results) > limit:
        print(f"\n{DIM}... and {len(results) - limit} more questions. Use --limit to see more or query by specific ID using --id.{RESET}")
    print()

def main():
    parser = argparse.ArgumentParser(
        description="Search and browse 10,000 Senior Engineer Interview Questions"
    )
    parser.add_argument("--query", "-q", help="Search keyword or phrase across questions")
    parser.add_argument("--id", type=int, help="Display full text for specific Question ID (1..10000)")
    parser.add_argument("--volume", "-v", type=int, choices=range(1, 11), help="Filter by Volume (1..10)")
    parser.add_argument("--chapter", "-c", type=int, choices=range(1, 101), help="Filter by Chapter (1..100)")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Maximum search results to display (default: 20)")
    
    args = parser.parse_args()
    
    if args.id:
        show_question(args.id)
    elif args.query or args.volume or args.chapter:
        search_questions(args.query, args.volume, args.chapter, args.limit)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
