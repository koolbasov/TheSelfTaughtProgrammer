# для записи английского текста encoding='utf-8' не нужна,
# а вот на русский текст ругается.
st = open('st.txt', 'w', encoding='utf-8')
st.write("Привет от Python!")
st.close()
