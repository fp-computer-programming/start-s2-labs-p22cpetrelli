#author CJP 03/09/2022
# Define function

def comes_after(st, letter):
    
#makes lowercase
    letter = letter.lower()

    return ''.join(b for a, b in zip(st.lower(), st[1:]) if a == letter and b.isalpha())
