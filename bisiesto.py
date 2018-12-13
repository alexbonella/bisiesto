#-------------------------------------------------------------
#Programa que devuelve al usuario si el año es bisiesto o no .
#Creado por Alexander Bolaño
# e-mail =alexbonella2806@gmail.com
#Fecha= Dic 12/2018
#-------------------------------------------------------------
def bis(year):
    # Write your logic here
    comprobar=True
    test1=(year/40).is_integer()
    test2=(year/100).is_integer()
    test3=(year/400).is_integer()
    if test3==False and test2==True:
        return False
        if test2==False:
            return False
    elif test1==True and test3==True :
        return True
    elif test1==True and test3==False :
        return True
    else :
        return False
#--------------------------------------
year = int(input('Digita un año a partir de 1990 : '))
print(bis(year))
