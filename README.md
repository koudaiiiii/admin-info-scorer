# Admin-Info Scorer

沖縄県の行政情報をAIで自動スコアリングするシステム。

## 機能
- 南城市公式サイトから最新情報を自動取得（38件）
- Gemini APIで住民への重要度を0-100でスコアリング
- Google Sheetsに自動書き込み

## スコア基準
| スコア | カテゴリ |
|--------|----------|
| 90-100 | 緊急・生命に関わる情報 |
| 70-89  | 経済的利益に直結（給付金・補助金等）|
| 40-69  | 生活・インフラに関わる情報 |
| 0-39   | 一般広報・イベント情報 |

## 技術スタック
- Python / Google Colab
- BeautifulSoup4（スクレイピング）
- Google Gemini API（スコアリング）
- Google Sheets API / gspread（データ保存）

## Session進捗
- ✅ Session 1: スクレイピング・スコアリング基盤構築
- ✅ Session 2: Google Sheets出力パイプライン完成
