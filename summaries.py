from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["context"],
    template="""
    You are an expert summarizer. Read the content below and generate a professional, easy-to-understand summary.

    Guidelines:
    - Keep it concise and informative
    - Use clear language with proper structure
    - Focus on the most important insights
    - Use bullet points or paragraph form as appropriate

    Content:
    {context}
    """
)
