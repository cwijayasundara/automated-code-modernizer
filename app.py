import streamlit as st
from dotenv import load_dotenv

import utils

load_dotenv()

from chains import (business_logic_chain,
                    tech_design_chain,
                    refactor_chain,
                    code_improvement_chain,
                    unit_testing_chain)

st.title("Code-Modernizer")

programming_language = st.radio(
    "Select Language:",
    ["Java", "Java Spring Boot", "Go", "Kotlin", "Scala", "Rust", "NodeJS"])

request = st.text_area('Enter Your Code Here ! ', height=300)
app_name = st.text_input('Enter Your App Name ! ')

submit = st.button("submit", type="primary")

if submit and request and programming_language:
    dir_path = app_name + '/'

    business_logic = business_logic_chain.run({'programming_language': programming_language, 'input': request})
    business_logic_doc_path = dir_path + '/business_logic' + '/business_logic.txt'
    utils.safe_write(business_logic_doc_path, business_logic)
    st.markdown(""":blue[Extracted Business Logic :]""")
    st.write(business_logic)

    tech_design = tech_design_chain.run({'programming_language': programming_language, 'input': request})
    tech_design_doc_path = dir_path + '/tech_design' + '/tech_design.txt'
    utils.safe_write(tech_design_doc_path, tech_design)
    st.markdown(""":blue[Technical Design :]""")
    st.write(tech_design)

    refactor = refactor_chain.run({'programming_language': programming_language, 'input': request})
    refactor_doc_path = dir_path + '/refactor' + '/refactor.txt'
    utils.safe_write(refactor_doc_path, refactor)
    st.markdown(""":blue[Refactored Code :]""")
    st.write(refactor)

    improved_code = code_improvement_chain.run({'programming_language': programming_language, 'input': refactor})
    code_improvement_doc_path = dir_path + '/code_improvement' + '/code_improvement.txt'
    utils.safe_write(code_improvement_doc_path, improved_code)
    st.markdown(""":blue[Improved & Optimised Code :]""")
    st.write(improved_code)

    unit_testing = unit_testing_chain.run({'programming_language': programming_language, 'input': improved_code})
    unit_test_path = dir_path + '/unit_testing' + '/unit_testing.txt'
    utils.safe_write(unit_test_path, unit_testing)
    st.markdown(""":blue[Unit & Integration Tests :]""")
    st.write(unit_testing)
