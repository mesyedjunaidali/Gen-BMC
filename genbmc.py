import openai
import streamlit as st
import pandas as pd

openai.api_key = "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"

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}
        ]
    )
    return completion.choices[0].message.content

st.title('Gen-BMC')
st.subheader('Business Model Canvas Generator')

name_of_industry = st.text_input("Enter the name of the industry:")
investment_amount = st.number_input("Enter the investment amount (INR):", min_value=0)

if name_of_industry and investment_amount:
    prompt = f"""You are an expert in generating business canvas models with more than 10 years of experience.
    I will provide you with the name of the industry and the investment amount I have to set up the industry.
    Expenditure breakdown (in tabulated format with 7 records) with the columns types of expense involved and amount,
    Cost split-up (in tabulated format with 6 records) containing one-time cost(industry setup cost),operation cost,funding cost,rent cost,digital infrastructure cost,insurance,employeepay,

    The industry is {name_of_industry} with an investment amount of {investment_amount} INR"""

    response = BasicGeneration(prompt)
    st.markdown(f"**Generated Business Model Canvas for {name_of_industry}**")
    st.write(response, unsafe_allow_html=True)

if name_of_industry and investment_amount:
    prompt = f"""You are an expert in generating business canvas models with more than 10 years of experience.
    I will provide you with the name of the industry and the investment amount I have to set up the industry.
    Definitely must present each section with bullet points except for the tabulated data which I would be asking.

    Average cost in each locality,
    Need for industry,
    Need for product with statistics,
    Expected reach after 1 year,
    Marketing strategy,
    Investment split-up strategy,
    Key Partners,
    Key Activities,
    Key Resources,
    Value Propositions,
    Customer Segments,
    Channels,
    Customer Relationships,
    Cost Structure,
    Revenue Streams,
    Profit Structure,
    Business Plan,
    Unique Selling Points,
    Key Metrics,
    SWOT Analysis,
    Unique possible names for the industry,
    Recommendations.

    The industry is {name_of_industry} with an investment amount of {investment_amount} INR"""

    response = BasicGeneration(prompt)
    st.write(response, unsafe_allow_html=True)
    
if name_of_industry and investment_amount:
    prompt = f"""You are an expert in generating business canvas models with more than 10 years of experience.
    I will provide you with the name of the industry and the investment amount I have to set up the industry.
    Present the tabulated data which I would be asking.

    Expected profit/loss and revenue for 6 years (in tabulated format) month-wise with the columns year,month,revenue,profit/loss,expense,cash flow statement(with 72 records)
    and the same table year-wise(with 6 records)after leaving a small space,
    

    The industry is {name_of_industry} with an investment amount of {investment_amount} INR"""

    response = BasicGeneration(prompt)
    st.write(response, unsafe_allow_html=True)