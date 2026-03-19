import yfinance as yf
import pandas as pd
import datetime
import sys

def start_integrated_analysis_v8():
    # --- 1. 智慧輸入判斷 ---
    # 支援 GitHub Actions 傳入參數，或手動執行時輸入
    if len(sys.argv) > 1:
        sid = sys.argv[1].strip()
    else:
        sid = input("📊 請輸入要分析的台股代號 (例如 2367 或 2485): ").strip()

    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticker_id = f"{sid}.TW"
    stock = yf.Ticker(ticker_id)
    
    # --- 2. 自動化數據抓取 (yfinance 引擎) ---
    try:
        info = stock.fast_info
        current_price = info.last_price
        prev_close = info.previous_close
        change_pct = ((current_price - prev_close) / prev_close) * 100
        
        # 抓取 60 日資料計算季線 (MA60)
        hist = stock.history(period="60d")
        ma60 = hist['Close'].mean()
    except Exception as e:
        print(f"❌ 錯誤：無法獲取代號 {sid} 的資料，請確認代號是否正確。")
        return

    print(f"{'='*65}")
    print(f"🚀 AI 分析旗艦 V8.0 | 智慧通用掃描器")
    print(f"🎯 監控目標：{sid} (目前價格：{current_price:.2f} | 漲跌：{change_pct:+.2f}%)")
    print(f"⏰ 執行時間：{now_time}")
    print(f"{'='*65}")

    # --- 3. 深度分析連結 ---
    print(f"🔍 [ 深度分析連結 (點擊直達) ]")
    print(f"  ● 💎 大戶比例：https://goodinfo.tw/tw/EquityDistributionChart.asp?STOCK_ID={sid}")
    print(f"  ● 💎 籌碼集中：https://www.wantgoo.com/stock/{sid}/major-investors/concentration")
    print(f"  ● 🏛️ 八大公股：https://www.wantgoo.com/public-bank/buy-sell?stockno={sid}")

    # --- 4. 大戶行為自動診斷 ---
    print(f"\n🚨 [ 大戶行為模擬診斷 ]")
    if current_price > ma60:
        print(f"  [ 🟢 趨勢強勁 ] 價格 ({current_price:.2f}) 高於季線成本 ({ma60:.2f})，老闆還在場子裡！")
    else:
        print(f"  [ 🔴 趨勢轉弱 ] 價格 ({current_price:.2f}) 跌破季線成本 ({ma60:.2f})，注意大戶撤資。")

    # --- 5. 戰略點評 (字典式管理，方便擴充) ---
    print(f"\n📝 [ 生意經戰略點評 ]")
    
    strategies = {
        "2485": [
            f"兆赫 1.8GHz 轉機點，目前 {current_price:.2f} 元主要反應轉虧為盈。",
            "⚠️ 3/18 爆天量 16 萬張，73 元為外資生死線。",
            "低軌衛星訂單若正式公告，才是破百動能。"
        ],
        "2367": [
            "燿華為衛星/車用 PCB 龍頭，基本面較為紮實。",
            f"目前價格 {current_price:.2f}，守住 74.4 元支撐為首要任務。",
            "400張大戶比例若 > 35%，是衝關 100 元的關鍵。"
        ],
        "2330": [
            "台積電：全球 AI 戰略核心，買的是地緣政治溢價。",
            "觀察 2nm 進度與法說會對 AI 需求之指引。"
        ]
    }

    # 取得對應策略，若代號未註冊則顯示通用建議
    current_strategy = strategies.get(sid, [
        "請點擊上方連結比對籌碼集中度是否與股價同步。",
        f"今日大盤重挫 375.4 點，此股若抗跌，代表主力意志堅定。",
        "遵循保命原則：破季線即考慮收攤止損。"
    ])

    for i, s in enumerate(current_strategy, 1):
        print(f"  {i}. {s}")

    # --- 6. DCF 估值參考 ---
    print(f"\n💎 [ DCF 估值公式參考 ]")
    print(f"  ● Fair Value = EPS * (1 + Growth) * PE")
    print(f"  ● 建議 PE：衛星/AI (25-35x) | 傳統產業 (12-15x)")
    
    print("-" * 65)
    print(f"💡 提示：今日大盤下跌 375.4 點，請嚴格執行止損，數據延遲 15 分鐘。")
    print("="*65)

if __name__ == "__main__":
    start_integrated_analysis_v8()
