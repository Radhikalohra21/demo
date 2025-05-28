import streamlit as st
import wikipedia

# Function to search Wikipedia for the given query
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        return f"Multiple results found. Try to be more specific. Options: {options}"
    except wikipedia.exceptions.PageError:
        return "No matching page found on Wikipedia."

# Streamlit UI
def main():
    st.title("Wikipedia Chatbot")
    st.write("Ask me anything!")

    user_input = st.text_input("Enter your question:")
    if user_input:
        answer = search_wikipedia(user_input)
        st.write("### Answer:")
        st.write(answer)

if __name__ == "__main__":
    main()