from Intermediate.curso_Moure.docx import Document #imporatndo la  libreria de word

#1 creamos una instancia de word
doc=Document()
#2 agregamos un totulo inicial
doc.add_heading('LISTA DE SALUDO AUTOMATICO',0)
#3crear una lista de nombres
nombres=["juan","felipe","valentina","mariana","luciana","elena"]
#4 iniciamos variblea s para el ciclo mientras
indice=0
cantidad_nombres=len(nombres)
#5iniciamos ciclo para recorrer la lista
while indice<cantidad_nombres:
    nombre_actual=nombres[indice]

    #escribir #hola seguido del nombre en el documento
    texto_linea=f"HOLA,{nombre_actual}....."
    doc.add_paragraph(texto_linea)

    print(f"AGREGAMOS A WORD: {texto_linea}")#feedback

    #incrementar el indice
    indice+=1
#guardamos el archivo final 
nombre_archivo="SALUDO_AUTOMATICO.docx"
doc.save(nombre_archivo)

print(f" ARCHIVO {nombre_archivo} CREADO CON EXITO")