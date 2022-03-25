
import webbrowser
import time
import json
import getpass
import os

#Splunk.doc es un programa que permite el facil acceso a la documentacion basica que un Ingeniero en Splunk debe tener a mano


#log -> adminitracion de los links y usuarios authorizados para utilizar el programa (Solo usuarios en admins tienen estos derechos
def log():
    print("BIENVENIDO A SPLUNK.DOC \n")
    user = input("Ingrese Splunk ID \n")
    password = getpass.getpass("Password \n")
    
    
    with open ("admins.txt","r") as AD:
        admins = json.load(AD)
    with open ("users.txt","r") as US:
        users = json.load(US)
        #Apertura de los documentos para tener acceso a nombres de usuarios 
        while True:
            if user in users and password == users[user] or user in admins and password == admins[user]: #Si el usuario existe en alguno de los documentos puede continuar 
               while True:
                   #Si el usuario esta en el documento admins puede agregar o eliminar usuarios ademas de agregar o mas links o eliminarlos ( Solo puede agregar usuarios al documento de usuarios)
                    if user in admins:
                        print("Bienvenido",user)
                        ans = input("1 Agregar - Eliminar Usuarios \n""2 Editar links \n")
                        if ans == "1":
                            ans = input('1 = REMOVER USER\n2 = AGREGAR USER\n')

                            if  ans == "1": #manejo de usuarios 
                                print("Lista de usuarios actuales")
                                for i in users: #loop para tener acceso a la lista de usuarios actuales 
                                    print(i)
                                user_del = input('Usuario que se va a eliminar \n')
                                if user_del in admins or user_del in users:
                                    users.pop(user_del)
                                    print("Usuario", user_del, " ha sido eliminado \n")
                                else:
                                    print(user_del,"No existe")
                            elif ans == "2":
                                print("Lista de usuarios actuales")
                                for i in users: #loop para tener acceso a la lista de usuarios actuales 
                                    print(i)
                                user_add = input("Ingrese nombre de usuario \n")
                                if user_add in users or user_add in admins or user_add == "":
                                    print("Este usuario ya existe o no valido")
                                else:
                                    new_pass = input('Nueva contrasena \n')
                                    users[user_add] = new_pass
                                    print('Nuevo usuario', user_add,"agregado")
                            
                       
                            with open ("users.txt","w") as US:
                                json.dump(users,US)

                      
                            
                                
                        elif ans == "2": #manejo de links
                            
                            pos_ans = ["1","2","3","y"]
                            while ans in pos_ans:
                                ans = input("Que diccionario desea editar \n1 = troubleshooting \n2 = doc \n3 = how  \n4 = Atras \n ")
                                if ans == "1":
                                    with open ("troubleshooting.txt","r") as TR:
                                        troubleshooting = json.load(TR)

                                        link_del = input("Ingrese el Key del diccionario \n")
                                        if link_del in troubleshooting:
                                            del troubleshooting[link_del]# se elimina el valor del diccionario
                                            print("Link",link_del,"fue removido")
                                            with open("troubleshooting.txt","w") as TR:
                                                json.dump(troubleshooting,TR)
                                        else:
                                            print("Valor no encontrado")
                                            
                                elif ans == "2":
                                    
                                    with open ("doc.txt","r") as DC:
                                        doc = json.load(DC)

                                        link_del = input("Ingrese el Key del diccionario \n")
                                        if link_del in doc:
                                            del doc[link_del]# se elimina el valor del diccionario
                                            print("Link",link_del,"fue removido")
                                            with open("doc.txt","w") as DC:
                                                json.dump(doc,DC)
                                        else:
                                            print("Valor no encontrado")
                                elif ans == "3":
                                    with open ("how.txt","r") as HW:
                                        how = json.load(HW)
                                        
                                        
                                        link_del = input("Ingrese el Key del diccionario \n")
                                        if link_del in how:
                                            del how[link_del]# se elimina el valor del diccionario
                                            print("Link",link_del,"fue removido")
                                            with open("how.txt","w") as HW:
                                                json.dump(how,HW)
                                        else:
                                            print("Valor no encontrado")
                                            
                                
                                else: 
                            #Si el valor no corresponde a la infomacion indicada por el programa se vuleve a solicitar un valor valido
                                    break
                    elif user in users and password == users[user]:#Si el ususario no es admin avanza directamente a la lista de documentacion disponible
                        main()
            else:
                print("You are not Splunker")
                break
                
                                
                    
def main(): #Provee acceso al los documentos con los links de docuemtacion oficial de Splunk (algunos necesitan ser abiertos desde Amazon Work Spaces)
    print("""
1 = Formulario de Troubleshooting
2 = Formulario de Documentacion
3 = How to?
4 = Topics 
""")
    ans_list = ["1", "2","3","4"]
    
    ans = input("Seleccione una opcion \n")
    while ans in ans_list:
        
        links = []
        if ans == "1":
            with open("troubleshooting.txt","r") as tr:
                troubleshooting = json.load(tr)

                line_count = 0

                for i in troubleshooting:#contador en caso de que el usuario ingrese un numero de index que no existe, permitiendo al programa volver a un directorio anterior
                    print("------------------------------")
                
                    line_count = (line_count + 1)
                    print(i)#lista de links disponibles 
                    
                    links.append(i)
                print("Precione 0 para volver al menu anterior ")
                
            ans = input("Seleccione una opcion \n")
            ansnum = int(ans)

            if ans == "0" or ansnum > line_count:
                break
                
            value_index =(links[int(ans)-1])
            print(value_index)
            webbrowser.open(troubleshooting[value_index])
            break
        elif ans == "2":
            with open("doc.txt","r") as dc:
                doc = json.load(dc)
                line_count = 0

                for i in doc:#contador en caso de que el usuario ingrese un numero de index que no existe, permitiendo al programa volver a un directorio anterior
                    print("------------------------------")
                    print(i)#lista de links disponibles 
                    line_count = (line_count + 1)
                    
                    links.append(i)
                print("Precione 0 para volver al menu anterior ")
                
            ans = input("Seleccione una opcion \n")
            ansnum = int(ans)
            

            if ans == "0" or ansnum > line_count:
                print(line_count)
                break
                
                
            value_index =(links[int(ans)-1])
            print(value_index)
            webbrowser.open(doc[value_index])
            break
        elif ans == "3":
            with open("how.txt","r")as h_to:
                how = json.load(h_to)
                line_count = 0
                for i in how:#contador en caso de que el usuario ingrese un numero de index que no existe, permitiendo al programa volver a un directorio anterior
                    print("------------------------------")
                    line_count = (line_count + 1)
                    print(i)#lista de links disponibles 
                    links.append(i)
                print("Precione 0 para volver al menu anterior ")
                
            ans = input("Seleccione una opcion \n")
            ansnum = int(ans)

            if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                break
                
            value_index =(links[int(ans)-1])
            print(value_index)
            webbrowser.open(how[value_index])
            break
        elif ans == "4":
            
            print(
            """"
            Available topics
1: SSL
2: WMI
3: Indexing 
4: Performance
5: Indexer Cluster
6: Search Head Cluster
7: Kv Store
8: SmartStore
        """)
            anstop = input("Select one option \n")
            if anstop == "1":
                with open("SSL.txt","r")as top:
                    SSL = json.load(top)
                    line_count = 0
                    for i in SSL:
                        print("------------------------------")
                        line_count = (line_count + 1)
                        print(i)#lista de links disponibles 
                        links.append(i)
                    print("Precione 0 para volver al menu anterior ")

                    ans = input("Seleccione una opcion \n")
                ansnum = int(ans)

                if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                    break
                    
                value_index =(links[int(ans)-1])
                print(value_index)
                webbrowser.open(SSL[value_index])
                break
            
            elif anstop == "2":
                with open("WMI.txt","r")as MI:
                    WMI = json.load(MI)
                    line_count = 0
                    for i in WMI:
                        print("------------------------------")
                        line_count = (line_count + 1)
                        print(i)#lista de links disponibles 
                        links.append(i)
                    print("Precione 0 para volver al menu anterior ")

                    ans = input("Seleccione una opcion \n")
                ansnum = int(ans)

                if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                        break
                    
                value_index =(links[int(ans)-1])
                print(value_index)
                webbrowser.open(WMI[value_index])
                break
            elif anstop == "3":
                with open("INDEXING.txt","r")as IDX:
                    INDEXING = json.load(IDX)
                    line_count = 0
                    for i in INDEXING:
                        print("------------------------------")
                        line_count = (line_count + 1)
                        print(i)#lista de links disponibles 
                        links.append(i)
                    print("Precione 0 para volver al menu anterior ")

                    ans = input("Seleccione una opcion \n")
                ansnum = int(ans)

                if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                        break
                    
                value_index =(links[int(ans)-1])
                print(value_index)
                webbrowser.open(INDEXING[value_index])
                break
            elif anstop == "4":
                with open("PERFORMANCE.txt","r")as per:
                    PERFORMANCE = json.load(per)
                    line_count = 0
                    for i in PERFORMANCE:
                        print("------------------------------")
                        line_count = (line_count + 1)
                        print(i)#lista de links disponibles 
                        links.append(i)
                    print("Precione 0 para volver al menu anterior ")

                    ans = input("Seleccione una opcion \n")
                ansnum = int(ans)

                if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                        break
                    
                value_index =(links[int(ans)-1])
                print(value_index)
                webbrowser.open(PERFORMANCE[value_index])
                break
            elif anstop == "5":
                with open("CLUSTER.txt","r")as CLUS:
                    CLUSTER = json.load(CLUS)
                    line_count = 0
                    for i in CLUSTER:
                        print("------------------------------")
                        line_count = (line_count + 1)
                        print(i)#lista de links disponibles 
                        links.append(i)
                    print("Precione 0 para volver al menu anterior ")

                    ans = input("Seleccione una opcion \n")
                ansnum = int(ans)

                if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                        break
                    
                value_index =(links[int(ans)-1])
                print(value_index)
                webbrowser.open(CLUSTER[value_index])
                break
            elif anstop == "6":
                with open("SHC.txt","r")as SH:
                    SHC = json.load(SH)
                    line_count = 0
                    for i in SHC:
                        print("------------------------------")
                        line_count = (line_count + 1)
                        print(i)#lista de links disponibles 
                        links.append(i)
                    print("Precione 0 para volver al menu anterior ")

                    ans = input("Seleccione una opcion \n")
                ansnum = int(ans)

                if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                        break
                    
                value_index =(links[int(ans)-1])
                print(value_index)
                webbrowser.open(SHC[value_index])
                break
            elif anstop == "7":
                with open("KVSTORE.txt","r")as KV:
                    KVSTORE = json.load(KV)
                    line_count = 0
                    for i in KVSTORE:
                        print("------------------------------")
                        line_count = (line_count + 1)
                        print(i)#lista de links disponibles 
                        links.append(i)
                    print("Precione 0 para volver al menu anterior ")

                    ans = input("Seleccione una opcion \n")
                ansnum = int(ans)
                if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                        break
                    
                value_index =(links[int(ans)-1])
                print(value_index)
                webbrowser.open(KVSTORE[value_index])
                break
            
            elif anstop == "8":
                with open("smartstore.txt","r")as SMRT:
                    smartstore = json.load(SMRT)
                    line_count = 0
                    for i in smartstore:
                        print("------------------------------")
                        line_count = (line_count + 1)
                        print(i)#lista de links disponibles 
                        links.append(i)
                    print("Precione 0 para volver al menu anterior ")

                    ans = input("Seleccione una opcion \n")
                ansnum = int(ans)

                if ans == "0" or ansnum > line_count:#condicional si el usuario ingresa un valor diferente al especificado en el index
                        break
                    
                value_index =(links[int(ans)-1])
                print(value_index)
                webbrowser.open(smartstore[value_index])
                break



              


            else:
                print("Invalid action \n")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")            
print("""! This documentation provides important information about how to face different situations  !
! in Splunk Support, if you are not sure about the suggestion found here request assistance !
! from the Senior Engineers team                                                            !""")  
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 

time.sleep(3)
while True: #codigo principal            
    main()
    #log()
    
