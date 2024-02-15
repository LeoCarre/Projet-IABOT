import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS

# Personnalisez les propriétés de la page
st.set_page_config(
    page_title="Spé Bot",
    page_icon="🤖",  # Ajoutez une icône personnalisée si nécessaire
    layout="wide",
    initial_sidebar_state="expanded",
)

user_api_key = "Your API Key"

# Chargement direct du fichier sans demander à l'utilisateur
default_csv_path = "all_job_data_with_specialties_and_series.csv"
data = CSVLoader(file_path=default_csv_path, encoding="utf-8", csv_args={'delimiter': ','}).load()


embeddings = OpenAIEmbeddings(openai_api_key=user_api_key)
vectorstore = FAISS.from_documents(data, embeddings)

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(temperature=0.0, model_name='gpt-3.5-turbo', openai_api_key=user_api_key),
    retriever=vectorstore.as_retriever()
)

def conversational_chat(query):
    result = chain({"question": query, "chat_history": st.session_state['history']})
    st.session_state['history'].append((query, result["answer"]))
    return result["answer"]

if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Salut à toi ! Pas de stress, le choix de ta spécialisation ne scelle pas ton destin. Dis-moi juste le métier qui te plaît, et on trouvera ensemble le parcours idéal pour y arriver. Let's go ! 🚀"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Hey ! 👋"]

# Container pour l'historique du chat
response_container = st.container()
# Container pour la saisie texte de l'utilisateur
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input("Message:", placeholder="Parle moi du métier que tu aimerais faire", key='input')
        submit_button = st.form_submit_button(label='Envoyer')

    if submit_button and user_input:
        output = conversational_chat(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
