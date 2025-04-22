import streamlit as st

st.set_page_config(page_title="安全対策費などを計算", layout="centered")

# タイトル
st.title("安全対策費などを計算するツール")

# 説明テキスト
st.markdown("""
このツールは、本体金額計(円)から安全対策費と法定福利費など計算するツール 

計算式は以下のとおりです：

- 作業名、品名 × 0.08 = 安全対策費
- 作業名、品名 × 0.15 = 法定福利費
- 本体金額計(円) = 作業名、品名 + 安全対策費 + 法定福利費
""")

# 注意書き
with st.expander("📌 使用上の注意"):
    st.warning("""
- 本体金額計の値は半角数字で入力してください。
- カンマ（,）や全角数字は使わないでください。
- 小数（例：123.45）も入力可能です。
    """)

# 入力フィールド
d_input = st.text_input("本体金額計(円)の値を入力してください（例：123）", value="")

# 計算処理
if st.button("計算する"):
    try:
        d = float(d_input)
        a = d / 1.23
        b = a * 0.08
        c = a * 0.15

        st.success("✅ 計算結果")
        st.write(f"品名 = {a:.2f}")
        st.write(f"安全対策費 = {b:.2f}")
        st.write(f"法定福利費 = {c:.2f}")
    except ValueError:
        st.error("数値を正しく入力してください（例：123.45）")

# フッター
st.markdown("---")
st.caption("© 2025 ABC Calculator")
