import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_laptop.sav', 'rb'))

st.title('_ESTIMASI HARGA LAPTOP_')

#'processor_gnrtn', 'ram_gb', 'ssd', 'hdd', 'os_bit', 'graphic_card_gb', 'display_size', 'warranty', 'old_price', 'discount', 'star_rating', 'ratings', 'reviews'
processor_gnrtn = st.number_input('Input Processor Gen')
ram_gb = st.number_input('Input RAM (GB)')
ssd = st.number_input('Input SSD (GB)')
hdd = st.number_input('Input HDD (GB)')
os_bit = st.number_input('Input OS bit (32bit/64bit)')
graphic_card_gb = st.number_input('Input Jumlah VGA')
display_size = st.number_input('Input Ukuran Layar (inch)')
warranty = st.number_input('Input Lama Garansi')
old_price = st.number_input('Input Harga Lama (Rupee (IRR))')
discount = st.number_input('Input Discount')
star_rating = st.number_input('Input Rating_Bintang ⭐(1-5)')
ratings = st.number_input('Input Jumlah Rating')
reviews = st.number_input('Input Jumlah Ulasan')

predict = ''

if st.button('Estimasikan Harga Laptop'):
    predict = model.predict(
        [[processor_gnrtn, ram_gb, ssd, hdd, os_bit, graphic_card_gb, display_size, warranty, old_price, discount, star_rating, ratings, reviews]]
    )
    st.write ('Estimasi harga Laptop  dalam Rupee INR : ', predict)
    st.write ('Estimasi harga Laptop bekas dalam Rupiah IDR :', predict*180.95)