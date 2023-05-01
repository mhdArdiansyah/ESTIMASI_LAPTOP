import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_laptop.sav', 'rb'))

st.title('_ESTIMASI HARGA LAPTOP_')

#graphic_card_gb','warranty','old_price','discount','star_rating',  'ratings:1185', 'reviews:141'
graphic_card_gb = st.number_input('Input Jumlah VGA')
warranty = st.number_input('Input Lama Garansi')
old_price = st.number_input('Input Harga Lama (Rupee (IRR))')
discount = st.number_input('Input Discount')
star_rating = st.number_input('Input Rating_Bintang ⭐(1-5)')
ratings = st.number_input('Input Jumlah Rating')
reviews = st.number_input('Input Jumlah Ulasan')

predict = ''

if st.button('Estimasikan Harga Laptop'):
    predict = model.predict(
        [[graphic_card_gb,warranty,old_price,discount,star_rating, ratings, reviews]]
    )
    st.write ('Estimasi harga Laptop  dalam Rupee INR : ', predict)
    st.write ('Estimasi harga Laptop bekas dalam Rupiah IDR :', predict*180.95)