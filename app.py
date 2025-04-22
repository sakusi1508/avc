import streamlit as st

st.set_page_config(page_title="DからA, B, Cを計算", layout="centered")

# タイトル
st.title("DからA, B, Cを計算するツール")

# 説明テキスト
st.markdown("""
このツールは、Dの値からA, B, Cを計算します。  
計算式は以下のとおりです：

- A × 0.08 = B  
- A × 0.15 = C  
- A + B + C = D  
→ つまり **D = A × 1.23**
""")

# 注意書き
with st.expander("📌 使用上の注意"):
    st.warning("""
- Dの値は半角数字で入力してください。
- カンマ（,）や全角数字は使わないでください。
- 小数（例：123.45）も入力可能です。
    """)

# 入力フィールド
d_input = st.text_input("D の値を入力してください（例：123）", value="")

# 計算処理
if st.button("計算する"):
    try:
        d = float(d_input)
        a = d / 1.23
        b = a * 0.08
        c = a * 0.15

        st.success("✅ 計算結果")
        st.write(f"A = {a:.2f}")
        st.write(f"B = {b:.2f}")
        st.write(f"C = {c:.2f}")
    except ValueError:
        st.error("数値を正しく入力してください（例：123.45）")

# フッター
st.markdown("---")
st.caption("© 2025 ABC Calculator")
