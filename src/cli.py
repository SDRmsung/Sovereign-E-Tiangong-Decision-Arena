"""
Sovereign-E-Tiangong-Decision-Arena CLI
提供給評審與終端開發者的一鍵命令列工具
"""

import argparse
import sys
from pathlib import Path

# Windows CJK/Emoji stdout 守衛
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# 將父目錄加入 sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.engine import ArenaEngine

def main():
    parser = argparse.ArgumentParser(description="天工企業決策競技場 CLI 工具")
    parser.add_argument("--list", action="store_true", help="列出所有測試基準題目")
    parser.add_argument("--eval", type=str, help="評測指定案例 (例如: CASE_HR_001)")
    
    args = parser.parse_args()
    engine = ArenaEngine()
    
    if args.list:
        cases = engine.list_cases()
        print(f"📋 載入競技場測試題庫 (共 {len(cases)} 題)：")
        for c in cases:
            print(f"  [{c['id']}] ({c['domain']}) {c['title']}")
        return 0
        
    if args.eval:
        res = engine.evaluate_case(args.eval)
        if not res:
            print(f"❌ 找不到題目代號: {args.eval}")
            return 1
        print("=" * 60)
        print(f"🎯 案例評測: [{res['case_id']}] {res['title']}")
        print("=" * 60)
        print(f"⚡ 天工雙核 SAT: {res['sat_result']['status']} | {res['sat_result']['summary']}")
        print(f"🤖 傳統 LLM 方案: {res['llm_result']['status']} | {res['llm_result']['summary']}")
        print("=" * 60)
        return 0

    parser.print_help()
    return 0

if __name__ == "__main__":
    sys.exit(main())
