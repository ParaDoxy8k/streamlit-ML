import streamlit as st
from transformers import pipeline

# -------------------------
# Load Model (โหลดครั้งเดียว)
# -------------------------
@st.cache_resource
def load_model():
    qa_pipeline = pipeline(
        "question-answering",
        model="airesearch/wangchanberta-base-wiki-20210520-spm-finetune-qa"
    )
    return qa_pipeline

question_answerer = load_model()

# -------------------------
# Highlight Function
# -------------------------
def display_qa_highlight(context, result):

    start_index = result['start']
    end_index = result['end']

    before = context[:start_index]
    answer_text = context[start_index:end_index]
    after = context[end_index:]

    html_output = f"""
    <div style='border:1px solid #ddd;
                padding:15px;
                border-radius:10px;'>

        <p><b>คำถาม:</b> {result['question']}</p>

        <p>
        <b>คำตอบ:</b>
        <span style='color:red;font-weight:bold;'>
        {result['answer']}
        </span>
        (Score: {result['score']:.4f})
        </p>

        <hr>

        <p>
        {before}
        <mark style='background-color:yellow'>
        {answer_text}
        </mark>
        {after}
        </p>

    </div>
    """

    return html_output


# -------------------------
# UI Streamlit
# -------------------------
st.title("🤖 Thai Question Answering (HuggingFace)")
st.write("ถามคำถามจากบทความภาษาไทย")

context = st.text_area(
    "📄 ใส่บทความ",
    height=200
)

question = st.text_input("❓ คำถาม")

if st.button("ค้นหาคำตอบ 🔍"):

    if context and question:

        result = question_answerer(
            question=question,
            context=context
        )

        html_result = display_qa_highlight(
            context,
            {'question': question, **result}
        )

        st.markdown(html_result, unsafe_allow_html=True)

    else:
        st.warning("กรุณาใส่บทความและคำถาม")