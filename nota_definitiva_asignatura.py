# programa para saber las notas, usando la formulas  nd=0.3*nc+0.3*np+0.1*au+0.2*bi
# input
nc= int(input("digite el valor de nc:"))
np= int(input("digite el valor de np:"))
na= int(input("digite el valor de na:"))
au= int(input("digite el valor de au:"))
bi= int(input("digite el valor de bi:"))
# processing
nd=0.3 * nc + 0.3 * np + 0.1 *au + 0.2 * bi
#ouput
print("---RESULTADOS---")

print("la nota definitiva es " +str(nc) + " * " + str(np) + " * " + str(na) + " *" + str(au) + " *" +str(bi))