# 📧 Cold Mail Generator

## Overview

The Cold Mail Generator is tool designed for service-oriented companies to streamline their outreach efforts. Utilizing Groq, Langchain, and Streamlit, this application simplifies the process of crafting personalized cold emails. Users can input the URL of a company's careers page, and the tool automatically extracts job listings from that page. Based on these job descriptions, it generates customized cold emails that include relevant portfolio links from a vector database.

## How It Works

1. **Input Job Listings**: Enter the URL of the target company's careers page into the application.
2. **Extract Job Information**: The tool parses the page to extract detailed job listings, including role, experience, skills, and description.
3. **Generate Personalized Emails**: For each job listing, the tool crafts a personalized cold email. These emails highlight your company’s capabilities and include links to relevant projects and case studies, tailored to the job requirements.

## Use Case Scenario

Imagine Infosys, a global leader in IT consulting and services, is looking to establish a new partnership with a company specializing in innovative technologies. They have identified a potential client, XYZ Innovations, which is at the forefront of developing cutting-edge solutions in the tech industry.

Infosys aims to reach out to XYZ Innovations with a proposal for a strategic partnership. To craft a compelling and personalized cold email, Infosys uses the Cold Mail Generator.

Here’s how the process works:

1. **Input the URL**: Infosys enters the URL of XYZ Innovations’s careers page into the Cold Mail Generator.
2. **Extract Job Listings**: The tool extracts job postings from XYZ Innovations’s careers page, including details about roles, required skills, and job descriptions.
3. **Generate Personalized Email**: The application generates a customized cold email for Infosys to send to XYZ Innovations. This email highlights Infosys's expertise in IT consulting and AI-driven solutions, specifically addressing how their services can complement XYZ Innovations’s needs and goals. It also includes links to relevant case studies and successful projects from Infosys’s portfolio, demonstrating their capabilities and alignment with XYZ Innovations’s objectives.

By using the Cold Mail Generator, Infosys can ensure their outreach to XYZ Innovations is targeted, relevant, and showcases how their solutions can bring value to the potential client.

## Features

- **Automatic Job Extraction**: Extracts job postings from company careers pages.
- **Personalized Email Generation**: Creates tailored emails based on job descriptions.
- **Portfolio Integration**: Includes links to relevant projects and case studies from a vector database.
- **Streamlined User Interface**: Easy-to-use interface built with Streamlit.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/cold-email-generator-tool.git
cd cold-email-generator-tool
pip install -r requirements.txt
```

## Usage

1. **Run the Streamlit App**:
   ```bash
   streamlit run app/main.py
   ```
2. Enter the URL of the company's careers page into the provided input field.
3. Click "Submit" to extract job information and generate personalized cold emails.
4. Review Generated Emails: The tool will display the cold emails based on the job descriptions extracted from the careers page.

## Dependencies

- [Groq](https://www.groq.com) - For integrating large language models to process and generate content.
- [Langchain](https://www.langchain.com) - For chaining and managing prompts and outputs.
- [Streamlit](https://streamlit.io) - For building the web application interface.
- [pysqlite3-binary](https://pypi.org/project/pysqlite3-binary/) - Provides a binary distribution of SQLite for compatibility with various environments.
