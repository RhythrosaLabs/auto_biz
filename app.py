import streamlit as st
from typing import Dict, Any, List
import openai


def get_section_from_llm(api_key: str, prompt: str) -> str:
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert business plan writer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        st.error(f"Error calling OpenAI API: {str(e)}")
        return ""

def validate_section(section: str, criteria: List[str]) -> Dict[str, Any]:
    validation = {criterion: criterion.lower() in section.lower() for criterion in criteria}
    return {
        "is_valid": all(validation.values()),
        "feedback": {k: "Present" if v else "Missing" for k, v in validation.items()}
    }

def create_feedback_prompt(section_name: str, validation_result: Dict[str, Any], current_section: str) -> str:
    if not validation_result["is_valid"]:
        missing_criteria = [k for k, v in validation_result["feedback"].items() if v == "Missing"]
        return f"""
The current {section_name} section needs improvement:
Missing criteria: {', '.join(missing_criteria)}

Current section:
{current_section}

Please revise the {section_name} section to address these missing points. 
Provide only the revised section without any explanations.
"""
    return "The section meets all criteria."

def generate_business_plan(api_key: str, progress_bar, status_text):
    sections = {
        "Executive Summary": ["business concept", "financial features", "financial requirements"],
        "Company Description": ["company goals", "target market", "competitive advantage"],
        "Market Analysis": ["industry description", "target market", "market test results"],
        "Organization & Management": ["organizational structure", "management team", "board of advisors"],
        "Product Line": ["product description", "competitive comparison", "sales literature"],
        "Marketing & Sales": ["marketing strategy", "sales force", "sales activities"],
        "Funding Request": ["current funding requirement", "future funding requirements", "use of funds"],
        "Financial Projections": ["income statements", "cash flow statements", "balance sheets"]
    }

    business_plan = {}
    total_sections = len(sections)

    for i, (section_name, criteria) in enumerate(sections.items()):
        status_text.text(f"Generating {section_name}...")
        progress_bar.progress((i + 1) / total_sections)
        
        initial_prompt = f"Write a {section_name} section for a business plan. Include information about: {', '.join(criteria)}."
        
        current_section = get_section_from_llm(api_key, initial_prompt)
        
        max_iterations = 3
        for j in range(max_iterations):
            validation_result = validate_section(current_section, criteria)
            
            if validation_result["is_valid"]:
                status_text.text(f"{section_name} meets all criteria!")
                break
            
            status_text.text(f"Improving {section_name} (Iteration {j+1}/{max_iterations})...")
            feedback_prompt = create_feedback_prompt(section_name, validation_result, current_section)
            current_section = get_section_from_llm(api_key, feedback_prompt)
        else:
            status_text.text(f"Warning: {section_name} may not meet all criteria after {max_iterations} iterations.")
        
        business_plan[section_name] = current_section

    return business_plan

def main():
    st.title("AI-Powered Business Plan Generator (using GPT-4o-mini)")

    st.write("""
    This app uses GPT-4o-mini to generate a comprehensive business plan. 
    It automatically iterates on each section to ensure all key points are covered.
    Please enter your OpenAI API key to begin.
    """)

    api_key = st.text_input("Enter your OpenAI API key", type="password")

    if api_key:
        if st.button("Generate Business Plan"):
            progress_bar = st.progress(0)
            status_text = st.empty()

            try:
                business_plan = generate_business_plan(api_key, progress_bar, status_text)
                
                st.success("Business Plan Generated Successfully!")
                
                for section, content in business_plan.items():
                    with st.expander(f"{section}"):
                        st.write(content)
                
                # Option to download the business plan
                st.download_button(
                    label="Download Business Plan",
                    data=str(business_plan),
                    file_name="business_plan.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter your OpenAI API key to use this app.")

    st.write("""
    **Disclaimer**: This business plan is generated by AI (GPT-4o-mini) and should be used as a starting point only. 
    The app automatically iterates on each section to improve content, but human review and customization are essential.
    Please review, modify, and expand upon this plan to ensure it accurately reflects your specific business idea and goals.
    """)

if __name__ == "__main__":
    main()
