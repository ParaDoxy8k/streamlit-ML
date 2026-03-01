import streamlit as st
from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="airesearch/wangchanberta-base-wiki-20210520-spm-finetune-qa"
)

st.title("Thai Question Answering App")

context = st.text_area("เนื้อหา")
question = st.text_input("คำถาม")

if st.button("หาคำตอบ"):
    result = qa_pipeline(
        question=question,
        context=context
    )

    st.success(f"คำตอบ: {result['answer']}")
    st.write(f"ความมั่นใจ: {result['score']:.2f}")