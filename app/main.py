import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def set_custom_css():
    st.markdown(
        """
        <style>
        .stTextArea textarea {
            width: 100% !important;
            height: 400px !important;
            resize: none;
        }
        .section-header {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #2C3E50;
        }
        .section-content {
            font-size: 16px;
            background-color: #F9F9F9;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 15px;
            color: #34495E;
        }
        .footer {
            font-size: 14px;
            color: #7F8C8D;
            text-align: center;
            margin-top: 30px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

def cold_email_app(llm, portfolio, clean_text_fn):
    st.markdown(
        """
        <div style='text-align:center;'>
            <h1>AI-Powered Cold Email Assistant</h1>
            <p style='text-align:center;'>Generate personalized outreach emails based on job descriptions from web pages.</p>
        </div>
        """, unsafe_allow_html=True
    )

    set_custom_css()

    url_input = st.text_input(
        label="🔗 Paste the Job URL:",
        placeholder="e.g., https://company.com/job/12345",
    )
    submit_button = st.button("Generate Email")

    st.markdown("---")

    if submit_button and url_input:
        with st.spinner("Fetching job details..."):
            try:
                loader = WebBaseLoader([url_input])
                page_content = loader.load().pop().page_content

                clean_data = clean_text_fn(page_content)

                jobs = llm.extract_jobs(clean_data)

                st.empty()

                if jobs:
                    for i, job in enumerate(jobs, start=1):
                        job_title = job.get('title', 'Job Title Not Found')

                        st.markdown(f"<div class='section-header'>📄 Job Title: {job_title}</div>", unsafe_allow_html=True)

                        description = job.get('description', 'No description available.')
                        st.markdown(f"<div class='section-header'>Description:</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='section-content'>{description}</div>", unsafe_allow_html=True)

                        skills = job.get('skills', [])
                        skills_text = ', '.join(skills) if skills else 'Not specified.'
                        st.markdown(f"<div class='section-header'>Skills Required:</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='section-content'>{skills_text}</div>", unsafe_allow_html=True)

                        links = portfolio.query_links(skills)

                        email = llm.write_mail(job, links)
                        st.empty()

                        st.markdown(f"<div class='section-header'>Generated Email:</div>", unsafe_allow_html=True)
                        st.text_area("Cold Email", email)
                        
                else:
                    st.warning("No jobs found on the provided page. Please ensure the URL contains a job description.")

            except Exception as e:
                st.error(f"⚠️ An error occurred while processing the URL: {e}")
    elif submit_button:
        st.warning("Please enter a valid URL before submitting.")

    st.markdown(
        """
        <div class='footer'>
            Made with ❤️ by <a href="https://mayankbohra.netlify.app/" target="_blank">Mayank</a>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="centered", page_title="AI Cold Email Generator")
    cold_email_app(chain, portfolio, clean_text)