import time
import streamlit as st
import streamlit.components.v1 as components
#components.html('''<html><body><img src="upchat_technologies_logo.jpg"></body><html>''')
#st.image("upchat_technologies_logo.jpg")
flag=0
components.html('''<style> body{padding:20px;}</style><body bgcolor = "powderblue"><h1><center><b>Caesar Cipher</h1></body>''')
import streamlit as st
#st.markdown("""<style>body { background-image: url('upchat_technologies_logo.jpg'); background-size: cover;}</style>""", unsafe_allow_html=True)

#st.header("Caesar Cipher")
st.subheader("Internship project")
st1 = st.file_uploader("Click here to upload file",type="txt")
if st1 is not None:
    f_open = st1.read()
    f_open = f_open.decode('utf-8')
    inp = f_open


st.markdown("### OR")
st.subheader("Enter the text")
if st1 is None:
   inp = st.text_input("Text")
opt = st.selectbox("Select the operation",("Encrypt","Decrypt"))

if opt == "Decrypt":
    val1= st.selectbox("Choose the value to decrypt",(-1,-2,-3,-4,-5))
    btn = st.button("Click to decrypt")
    if btn == True:
       flag = 1
elif opt== "Encrypt":
     val = st.selectbox("Choose the Value to Encrypt",(1,2,3,4,5))
     btn = st.button("Click to Encrypt")
     if btn == True:
        flag =2
if flag== 2:
   with st.spinner(text="Please Wait",cache=True):
        time.sleep(2)
   with st.status("Encrypting data"):
           time.sleep(2)
           st.write("Encryption done")
   pg = st.progress(0)
   for i in range(101):
       pg.progress(i)
       time.sleep(0.01)


   st.success("Encryption done :smiley:")
   enstr = ""
   for i in inp:
        order = ord(i)
        order = order+val
        enstr +=chr(order)
   st.code(enstr)

   st.download_button(
           label="Download Encrypted File :open_file_folder:",
           data=enstr,
           file_name="Encrypted.txt", help="Click to download")
elif flag==1:
    with st.spinner(text="Please Wait", cache=True):
        time.sleep(2)
    with st.status("Decrypting data"):
        time.sleep(2)
        st.write("Decryption done")
    pg = st.progress(0)
    for i in range(101):
        pg.progress(i)
        time.sleep(0.01)
    st.success("Decryption done :smiley:")
    enstr = ""
    for i in inp:
        order = ord(i)
        order = order + val1
        enstr += chr(order)
    st.code(enstr)
    st.download_button(label="Download Decrypted File", data= enstr, help="Click here to download",file_name="Decrypted.txt")
