#Menentukan tipe huruf vokal atau konsonan

huruf = input('Masukkan Huruf : ')
vokal = " merupakan huruf vokal"
konsonan = " merupakan huruf konsonan"

if(huruf == 'a') or (huruf == 'A') :
  print(vokal)
elif(huruf == 'i') or (huruf == 'I') :
  print(vokal)
elif(huruf == 'u') or (huruf == 'U') :
  print(vokal)
elif(huruf == 'e') or (huruf == 'E') :
  print(vokal)
elif(huruf == 'o') or (huruf == 'O') :
  print(vokal)
else :
  print(konsonan)
