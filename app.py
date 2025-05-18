# streamlit UI

import streamlit as st
from sentence_transformers import SentenceTransformer

from vector_db import VectorDB

from utilis import generate_id , prepare_payload

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")



def main():
    st.title("Vector Search Demo")


    # iniatize model & vector db

    model = load_model()
    vector_db = VectorDB()

    tab1 , tab2 = st.tabs(['Add Text','Search'])
    with tab1:
        st.header('Add Vector To DB')
        new_text = st.text_input("Enter Word or Sentence")
        if st.button("Add to DB"):
            if new_text:
                embeddings = model.encode(new_text).tolist()
                text_id = generate_id(new_text)
                payload = prepare_payload(new_text)

                vector_db.insert_vectors(
                    vectors=[embeddings],
                    payloads=[payload],
                    ids=[text_id]
                )

                st.success(f"{new_text} Was Add Successfuly Into VectoreStore")
            else:
                st.warning("please Enter some text first")



    with tab2:
        st.header('Search similar words or senteces')
       
  




if __name__ == "__main__":
    main()
