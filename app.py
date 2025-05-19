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
