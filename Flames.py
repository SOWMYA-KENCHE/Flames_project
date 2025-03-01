import streamlit as st

def flames_game(name1, name2):
    s = "FLAMES"
    name1 = list(name1)
    name2 = list(name2)

    for i in name1[:]:
        if i in name2:
            name1.remove(i)
            name2.remove(i)

    n = len(name1) + len(name2)

    while len(s) > 1:
        i = n % len(s) - 1
        if i == -1:
            s = s[:len(s)-1]
        else:
            s = s[i+1:] + s[:i]

    return s

# Streamlit UI
st.title("FLAMES Game 💖🔥")
name1 = st.text_input("Enter Name 1:")
name2 = st.text_input("Enter Name 2:")

if st.button("Find Relationship"):
    if name1 and name2:
        result = flames_game(name1, name2)
        relation = {
            "F": "Friends 👬",
            "L": "Lovers ❤️",
            "A": "Affection 💞",
            "M": "Marriage 💍",
            "E": "Enemies 😡",
            "S": "Siblings 👩‍👦"
        }
        st.success(f"The relationship is: **{relation[result]}**")
    else:
        st.error("Please enter both names!")

