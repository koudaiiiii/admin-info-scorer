import json
import re
from google import genai

def score_article(client, title):
    prompt = f"""
あなたは沖縄県在住の市民として、行政情報の生活への影響度を判定してください。
判定基準:
- 90〜100: 緊急・生命（断水、停電、避難勧告）
- 70〜89:  経済的利益（給付金、助成金、税減免）
- 40〜69:  生活・インフラ（施設休館、ゴミ収集変更）
- 0〜39:   一般広報（市長挨拶、統計報告）
タイトル: {title}
JSON形式のみで回答: {{"score": 数値, "category": "カテゴリ名", "summary": "50文字以内の要約"}}
"""
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt)
    match = re.search(r'\{{.*\}}', response.text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return {"score": 0, "category": "不明", "summary": "解析失敗"}
