# My19-TrendTeller-AI
Gen Ai

Here’s a **new AI + Fashion project** topic with full code and instructions, suitable for **VS Code** and **GitHub deployment**.

---

## 🧠 Project Title: **TrendTeller AI - Fashion Trend Predictor**

### 🎯 Objective:

Use AI to analyze fashion-related keywords and predict current or upcoming fashion trends. Perfect for influencers, bloggers, or fashion brands to stay ahead of the curve.

---

## 💡 Features:

* Input any fashion-related keywords (e.g., “baggy jeans”, “cottagecore”)
* AI predicts whether the trend is:

  * **Rising** 📈
  * **Falling** 📉
  * **Stable** ➖
* Suggests related trends and future styles
* Generates a blog-style explanation and hashtags

---

## 🛠️ Stack:

* Python
* Streamlit
* LangChain with Ollama (TinyLLaMA or any local model)

---

## 📁 Folder Structure:

```
TrendTeller-AI/
├── app.py
├── requirements.txt
├── README.md
```

---

## 📦 `requirements.txt`

```txt
streamlit
langchain
transformers
sentence-transformers
torch
```

---

## 🧠 `app.py` (Full Code)

```python
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

# Setup
st.set_page_config(page_title="📊 TrendTeller AI", layout="centered")
st.title("👠 TrendTeller AI")
st.subheader("Predict the Rise & Fall of Fashion Trends")

# Input
keyword = st.text_input("🔍 Enter a fashion trend or keyword:", placeholder="e.g. baggy jeans, Barbiecore, cargo pants")

if keyword:
    llm = Ollama(model="tinyllama")

    # Prompt for trend prediction
    trend_prompt = PromptTemplate(
        input_variables=["keyword"],
        template=(
            "Analyze the fashion trend '{keyword}' and predict whether it's rising, falling, or stable. "
            "Provide reasoning based on recent popularity, celebrity influence, seasonal appeal, and social media presence. "
            "Also suggest 2 similar or emerging trends."
        )
    )
    trend_chain = LLMChain(llm=llm, prompt=trend_prompt)

    # Prompt for blog-style explanation
    blog_prompt = PromptTemplate(
        input_variables=["keyword"],
        template=(
            "Write a short blog-style paragraph about the fashion trend '{keyword}', its evolution, appeal, and when to wear it. "
            "Include 3 hashtags."
        )
    )
    blog_chain = LLMChain(llm=llm, prompt=blog_prompt)

    if st.button("📈 Predict Trend"):
        with st.spinner("Analyzing trend..."):
            trend_output = trend_chain.run(keyword=keyword)
            blog_output = blog_chain.run(keyword=keyword)

        st.markdown("### 🔮 Trend Analysis:")
        st.success(trend_output)

        st.markdown("### 📝 Blog & Hashtags:")
        st.info(blog_output)
```

---

## 📖 `README.md`

````markdown
# 👠 TrendTeller AI

**TrendTeller AI** is a fashion trend analyzer powered by local LLMs. Enter a fashion keyword and the model will predict if it's rising or falling in popularity, with supporting insights.

---

## 🚀 Features
- Predict the current status of fashion trends
- Discover similar or related upcoming styles
- Generate blog-style explanation and hashtags

---

## 📦 Tech Stack
- Python
- Streamlit
- LangChain
- Ollama (TinyLLaMA or compatible LLM)

---

## 🖥️ How to Run Locally

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/TrendTeller-AI.git
cd TrendTeller-AI
````

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run Ollama and a supported model**:

```bash
ollama run tinyllama
```

4. **Launch the app**:

```bash
streamlit run app.py
```

---

## 🧪 Sample Inputs

* cargo pants
* coquette aesthetic
* denim-on-denim
* techwear

---

## 📬 Contact

Made by [Your Name](https://github.com/yourusername)

```

---

Would you like to add:
- Real-time Google Trends or Instagram tag integration?
- Optional image upload to detect and analyze fashion trends from photos?

Let me know, and I’ll extend the project!
```
