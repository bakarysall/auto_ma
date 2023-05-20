import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests
import json
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report


#from pycaret.regression import setup as setup_reg
#from pycaret.regression import compare_models as compare_models_reg
#from pycaret.regression import save_model as save_model_reg
#from pycaret.regression import plot_model as plot_model_reg

#modèle de classification avec pycaret

#from pycaret.classification import setup as setup_class
#from pycaret.classification import compare_models as compare_models_class
#from pycaret.classification import save_model as save_model_class
#from pycaret.classification import plot_model as plot_model_class
@st.cache_data
def load_data(file):
    data = pd.read_csv(file, encoding='utf-8')
    return data
  
def lotti_vid(url :str):
  r= requests.get(url)
  if r.status_code!=200:
    return None
  return r.json()

  
def main():
    st.sidebar.write("[Auteur: Bakary SALL](%s)")
    
    st.sidebar.title("AutoML App")

    st.sidebar.markdown("Une application d'AutoML pour développer des modèles d'apprentissage automatique.")

    st.sidebar.header("Collecte des données")
    st.sidebar.markdown("Rassemblez les données pertinentes pour votre problème d'apprentissage automatique.")

    st.sidebar.header("Choix du modèle")
    st.sidebar.markdown("Choisissez un modèle regression ou classification.")

    st.sidebar.header("Configuration du problème")
    st.sidebar.markdown("Définissez le type de modèle et les métriques d'évaluation.")

    st.sidebar.header("Expérimentation avec l'AutoML")
    st.sidebar.markdown("Explorez différentes architectures, paramètres et techniques d'optimisation.")

    st.sidebar.header("Entraînement et évaluation")
    st.sidebar.markdown("Entraînez le modèle sur les données et évaluez ses performances.")

    st.sidebar.header("Déploiement de l'application")
    st.sidebar.markdown("Déployez le modèle pour une utilisation dans des scénarios réels.")

    st.sidebar.markdown("Bon travail  !")

    st.title("Bienvenue AutoML App SALL défall youffou niit nakk")
    st.write("Bonjour à tous, ou devrais-je dire 'bonjour' avec des guillemets géants")

    file = st.file_uploader("Importer un dataset. (csv,xlsx) et encoder en utf-8 please" , type=["csv","xlsx"])
    
    if file is not None:
        data = load_data(file)
        st.dataframe(data.head())
        
        profile = st.button("Rapport EDA")
        if profile:
            profile_df = data.profile_report()
            st_profile_report(profile_df)
         

        target = st.selectbox("Selectionner votre variable cible", data.columns)
        task = st.selectbox("Sélectionner votre modèle",["Regression","Classification"])
        data = data.dropna(subset=[target])
    
        #if task =="Regression":
            #if st.button("Choisir modèle"):
             #   exo_reg = setup_reg (data, target =target)
              #  model_reg = compare_models_reg()
              #  save_model_reg(model_reg, "Sauvegarde du modèle")
               # st.success("Le modèle de regression est bien créee ")
                
                #resultat
                
               # st.write("Résultat")
               # plot_model_reg(model_reg,'Résiduel', save=True)
                #st.image("Residuel.png")
                
              #  st.write ("Feature importance")
              #  plot_model_reg(model_reg, plot = 'feature', save = True)
              #  st.image("Feature importance.png")
                
                
              #  with open('best_reg_model.pkl', 'rb') as f:
              #      st.download_button('Télécharger le Pipeline model',f, file_name="best_reg_model.pkl")
        #if task =='Classification':
          # if st.button("Choisire modèle"):
            #   exo_class = setup_class(data, target = target)   
             #  model_class= compare_models_class()
             #  save_model_class(model_class,"Sauvegarder le modèle")
             #  st.success("Le modèle de regression est bien créee")  
               
              # #résultat
             #  col5, col6=st.columns(2)
               
             #  with col5:
             #      st.write("RDC Curve")
             #      plot_model_class(model_class, save=True)
              #     st.image("AUC.png")
                   
             #  with  col6 :
             #      st.write("Rapport de Classification")
              #     plot_model_class(model_class, plot='class report', save=True)
              #     st.image("Class report.png")
            #       
               #col7,col8 = st.columns(2)
               
              # with col7:
              #     st.write("Confusion Matrix")
             #      plot_model_class(model_class, plot ='confusion_matrix', save=True)
              #     st.image("Confusion matrix.png")
                   
             #  with col8 :
              #     st.write("Feature importance")
             #      plot_model_class(model_class, plot='feature', save=True)
              #     st.image("Feature importance.png")
             #  with open ('best_class_model.pkl', 'rb') as f :
               #    st.download_button("Télécharger le modèle", f, file_name="model_class.pkl")   
    else:
        #st.image("sal.jpg")
        lotti_= lotti_vid('https://assets3.lottiefiles.com/packages/lf20_fWd36IjnsR.json')
        st_lottie(lotti_, key ='hello')
        
        
        
        
        
    st.write("")
    st.write("")    
    st.write("Réalisé par Bakary SALL")
        
if __name__== '__main__':
    main()