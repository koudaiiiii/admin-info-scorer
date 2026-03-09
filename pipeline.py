import time
from datetime import datetime

def run_pipeline(sheet, articles, score_fn):
    headers_row = ["取得日時", "タイトル", "URL", "スコア", "カテゴリ", "要約"]
    
    existing = sheet.get_all_values()
    done_urls = set(row[2] for row in existing[1:] if len(row) > 2)
    remaining = [a for a in articles if a["url"] not in done_urls]
    
    print(f"完了済み: {len(done_urls)}件 / 残り: {len(remaining)}件")
    
    results = []
    for i, article in enumerate(remaining):
        print(f"[{i+1}/{len(remaining)}] スコアリング中: {article['title'][:30]}...")
        try:
            result = score_fn(article["title"])
            row = [
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                article["title"],
                article["url"],
                result["score"],
                result["category"],
                result["summary"]
            ]
            sheet.append_row(row)
            results.append({**article, **result})
            time.sleep(13)
        except Exception as e:
            print(f"  エラー: {e}")
            break
    
    print(f"\n完了: {len(results)}件追加")
    return results
