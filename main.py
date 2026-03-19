import yfinance as yf
import pandas as pd
import datetime

# --- 核心設定：修改此處代號即可 ---
STOCK_ID = "2485"  # 兆赫。若要看燿華請改 "2367"

def start_integrated_analysis_v7(sid):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticker_id = f"{sid}.TW"
    stock = yf.Ticker(ticker_id)
    
    # --- A. 自動化數據抓取 (yfinance 引擎) ---
    try:
        info = stock.fast_info
        current_price = info.last_price
        prev_close = info.previous_close
        change_pct = ((current_price - prev_close) / prev_close) * 100
    except:
        current_price, change_pct = 0, 0

    print(f"{'='*65}")
    print(f"🚀 全能台股 AI 分析旗艦 V7.0 | 自動化報價 & 大戶診斷")
    print(f"🎯 監控目標：{sid} (目前價格：{current_price:.2f} | 漲跌：{change_pct:+.2f}%)")
    print(f"⏰ 系統執行時間：{now_time}")
    print(f"{'='*65}")

    # --- 第一部分：宏觀環境 ---
    print(f"📊 [ 第一部分：宏觀環境 ]")
    print(f"  ● 國發會_景氣燈號：https://index.ndc.gov.tw")
    print(f"  ● M平方_全球總經  ：https://www.macromicro.me")
    
    # --- 第二部分：個股深度分析連結 ---
    print(f"\n🔍 [ 第二部分：個股深度分析 (點擊直達) ]")
    print(f"  ● 1. 💎 大戶比例：https://goodinfo.tw/tw/EquityDistributionChart.asp?STOCK_ID={sid}")
    print(f"  ● 2. 💎 籌碼集中：https://www.wantgoo.com/stock/{sid}/major-investors/concentration")
    print(f"  ● 3. ⚠️ 家數差指標：https://www.wantgoo.com/stock/{sid}/major-investors/main-trend")
    print(f"  ● 4. 🏛️ 八大公股：https://www.wantgoo.com/public-bank/buy-sell?stockno={sid}")

    # --- 第三部分：自動化警報診斷 ---
    print(f"\n🚨 [ 第三部分：大戶行為模擬診斷 ]")
    hist = stock.history(period="60d")
    ma60 = hist['Close'].mean()
    
    if current_price > ma60:
        print(f"  [ 🟢 趨勢強勁 ] 目前價格 ({current_price:.2f}) 高於季線平均成本 ({ma60:.2f})。")
    else:
        print(f"  [ 🔴 趨勢轉弱 ] 目前價格 ({current_price:.2f}) 跌破季線 ({ma60:.2f})，大戶可能在撤資！")

    # --- 第四部分：生意經戰略點評 (動態切換) ---
    print(f"\n📝 [ 第四部分：生意經戰略點評 ]")
    if sid == "2485":
        strategy = [
            f"兆赫 1.8GHz 轉機點已現，目前 {current_price:.2f} 元是反應轉虧為盈。",
            "⚠️ 3/18 爆天量 16 萬張，若跌破 73 元外資成本防線必須撤退。",
            "若低軌衛星 RF Switch 訂單正式公告，估值才有機會破百。"
        ]
    elif sid == "2367":
        strategy = [
            "燿華為低軌衛星/車用 PCB 龍頭，注意 74.4 元支撐。",
            "大戶持股比例若衝破 35%，目標價 100 元更有把握。"
        ]
    else:
        strategy = ["請手動輸入個股邏輯。", "觀察營收 YoY 是否持續成長。"]
        
    for i, s in enumerate(strategy, 1):
        print(f"  {i}. {s}")

    # --- 第五部分：DCF 估值參考 ---
    print(f"\n💎 [ 第五部分：DCF 估值公式參考 ]")
    print(f"  ● Fair Value = EPS * (1 + Growth) * PE")
    print(f"  ● 建議 PE：衛星/AI (25-35x) | 傳統產業 (12-15x)")
    
    print("-" * 65)
    print(f"💡 提示：今日大盤下跌 375.4 點，請嚴格執行止損，數據延遲 15 分鐘。")
    print("="*65)

if __name__ == "__main__":
    start_integrated_analysis_v7(STOCK_ID)
