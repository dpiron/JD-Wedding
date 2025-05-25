import streamlit as st


def left_aligned(text, bold=False, caption=False):
    style = "text-align:left;"
    if caption:
        style += "font-size:0.8em; color:gray;"
    if bold:
        text = f"<b>{text}</b>"
    st.markdown(f'<div style="{style}">{text}</div>', unsafe_allow_html=True)

def right_aligned(text, bold=False, caption=False):
    style = "text-align:left;"
    if caption:
        style += "font-size:0.8em; color:gray;"
    if bold:
        text = f"<b>{text}</b>"
    st.markdown(f'<div style="{style}">{text}</div>', unsafe_allow_html=True)


st.set_page_config(page_title="Julia & Denis 💍", layout="centered")

st.title("🤍 Mariage de Julia & Denis")
st.subheader("Le 20 Juin 2025")
st.write("")

#col1, col2, col3 = st.columns(3)
#photos = ["images/vertical/1.jpeg",
#          "images/vertical/2.jpeg",
#          "images/vertical/3.jpeg",
#          ]
#for col, photo in zip([col1, col2, col3], photos):
#    col.image(photo, use_container_width=True, caption="")

st.image("images/vertical/3verticals.png")

st.write("")
st.write("")
st.header("11h 💒 Cérémonie à la maison communale")
col1, col2 = st.columns(2)
with col1:
    left_aligned("Nous vous attendons avec impatience pour partager ce moment unique.")
    left_aligned("Rendez-vous à 10h45 devant l'ancienne maison communale d'Uccle.")
    left_aligned("Code vestimentaire : Chic Décontracté.")
    left_aligned("Robes d’été, chemises, et tenues soignées mais confortables.", caption=True)
    left_aligned("")
with col2:
    right_aligned("We are excited to celebrate our wedding with you.")
    right_aligned("Please join us at 10:45am in front of the old town hall of Uccle.")
    right_aligned("Dress code: Nice Casual.")
    right_aligned("Sundresses and button-downs vibes.",caption=True)
    right_aligned("")

st.write("Adresse : Place Jean Vander Elst, 1180 Uccle")
uccle_map = """
<iframe 
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d477.73292704851684!2d4.333014309069847!3d50.803566576455076!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47c3c5faaadef3b5%3A0x2abf86386698f7fb!2sAncien%20b%C3%A2timent%20communal!5e0!3m2!1sen!2sbe!4v1748097365225!5m2!1sen!2sbe" 
  width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
"""
st.markdown(uccle_map, unsafe_allow_html=True)

st.write("")
st.write("")
st.header("12h 🥂 Verre de l'amitié chez nous")
col1, col2 = st.columns(2)
with col1:
    left_aligned("Après la cérémonie, rejoignez-nous pour un verre, des pizzas, des desserts et de la convivialité.")
    left_aligned("")
with col2:
    right_aligned("After the ceremony join us for drinks, pizzas and desserts.")
    right_aligned("")

st.write("Adresse : Rue Langeveld 125, 1180 Uccle")
uccle_map2 = """
<iframe 
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2521.346670440708!2d4.368210100000001!3d50.8062154!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47c3c4e27b6ba9f5%3A0x4e23a9c719e5dd38!2sRue%20Langeveld%20125%2C%201180%20Uccle!5e0!3m2!1sen!2sbe!4v1748097854588!5m2!1sen!2sbe" 
  width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
"""
st.markdown(uccle_map2, unsafe_allow_html=True)

st.write("")
st.write("")
st.header("🎁 Cadeaux")
col1, col2 = st.columns(2)
with col1:
    left_aligned("Auncun cadeau n'est nécessaire!")
    left_aligned("Si vous souhaitez quand même nous en faire un, une participation à notre voyage de noces nous ferait très plaisir.")
    left_aligned("IBAN: BE58 0019 0996 7079", caption=True)
    left_aligned("")
with col2:
    right_aligned("No gift is necessary!")
    right_aligned("If you'd still like to make a gift, a contribution to our honeymoon fund would be greatly appreciated.")
    right_aligned("Through Zelle: julia.boyaval@gmail.com", caption=True)
    right_aligned("")

st.write("")
st.write("")
st.write("")
#col1, col2, col3 = st.columns(3)
#photos2 = [
#    "images/square/2.jpeg",
#    "images/square/4.jpeg",
#    "images/square/6.jpeg"
#    ]
#photos3 = [
#    "images/square/1.jpeg",
#    "images/square/3.jpeg",
#    "images/square/4.jpeg"
#    ]
#for col, photo in zip([col1, col2, col3], photos2):
#    col.image(photo, use_container_width=True, caption="")
#for col, photo in zip([col1, col2, col3], photos3):
#    col.image(photo, use_container_width=True, caption="")

st.image("images/square/3squares.png")

col1, col2 = st.columns(2)
with col1:
    left_aligned("Merci à tous 💖", caption=True)
with col2:
    right_aligned("Thanks to all 💖", caption=True)