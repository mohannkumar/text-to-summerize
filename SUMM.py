import streamlit as st
import cohere

# Initialize Cohere API
API_KEY = "esvyqN8GgSr5ghtUl3wi5miArwlVwW2qVkErm9BD"  # Replace with your Cohere API key
co = cohere.Client(API_KEY)

# Streamlit app
def main():
    st.title("Text Summarization with Cohere")
    st.write("Enter a long text and get a concise summary.")

    # Input text
    input_text = st.text_area("Enter the text to summarize", height=300)
    
    # Set maximum summary length
    max_summary_length = st.slider("Maximum length of the summary (in characters)", 50, 300, 100)
    
    if st.button("Summarize"):
        if not input_text.strip():
            st.warning("Please enter some text to summarize.")
        else:
            with st.spinner("Generating summary..."):
                try:
                    response = co.generate(
                        model='summarize-xlarge',
                        prompt=input_text,
                        max_tokens=max_summary_length,
                        temperature=0.7,
                    )
                    summary = response.generations[0].text.strip()
                    st.subheader("Summary")
                    st.write(summary)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
