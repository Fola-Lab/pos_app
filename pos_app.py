#IMPORT MODULE
import streamlit as st

# Date Input
import datetime 

the_time = datetime.datetime.now().strftime('%y-%m-%d %H:%M')

st.write(the_time)

from PIL import Image
img = Image.open("pos.PNG")

# display image using streamlit
st.image(img, width=700)

# give a title to our app
st.title('WELCOME TO BESTWAY TRANSACTS')
st.subheader('Your Money Transactions is safe with us')

st.sidebar.write('INSERT YOUR ATM CARD')

Account_details1 = {}
User_account_history = []

Account_details = {}
Account_history = []

st.sidebar.write('ACCOUNT DETAILS FOR TRANSACTIONS')
    
#st.write('\nEnter your 10 digit account number: ')
account_number = st.sidebar.text_input('Account Number')

try:
    len(account_number) == 10
except:
    st.write('\nInvalid Account Number')
    
#st.write('\nEnter your password: ') 
pwd = st.sidebar.text_input('Passcode')
try:
    int(len(pwd)) == 4
except:
    st.write('\nIncorrect Password')

Account_details1 = {'Account Number' : account_number, 'Pin': pwd}
User_account_history.append(Account_details1)

st.sidebar.button('Proceed to Transaction')


active = False

# Create a bank dropdown 
bank_name = st.selectbox("BANK NAME: ", 
                         [' ', 'GTBank', 'FirstBank', 'Sterling', 'Zenith', 'Wema'])
if bank_name == " ":
    st.error('Choose your bank')
    
num_of_withdrawal = st.number_input('Enter number of withdrawal to be made:\n ')
Amount_to_withdraw = st.number_input('Enter amount:\n ')    
Account_details = {'name': bank_name, 'num_of_withdrawal': num_of_withdrawal, 'Amount':Amount_to_withdraw}
Account_history.append(Account_details)

status = st.radio('Would you like to perform another Transaction? ',('Yes', 'No'))

# compare status value
if(status == 'Yes'):
    st.text_input('Select an option', bank_name)
           
elif(status == 'No'):
    st.write('Go to Total withdrawal')
    

Total_withdrawal = 0  

for key, account in enumerate(Account_history):
    account_total = account['num_of_withdrawal'] * account['Amount']
    Total_withdrawal = Total_withdrawal + account_total
       
if(st.button('Calculate Total Withdrawal')):
    st.text('Total_withdrawal : #%.2f' % Total_withdrawal)
    st.success('Success')
    st.write('Take your Cash')
        

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)