datos=datos.split()
datos=[float(x)for x in datos]
datos= [datos[x:x+4] for x in range(0, len(datos), 4)]
combinaciones=[]
for dato in datos:
    clase=''
    for numero in dato:
        if(numero<0.5):
            clase+='1-'
        else:
            clase+='2-'
    clase=clase[:-1]
    combinaciones.append(clase)
combinaciones.pop()
cuenta={}
for i in [1,2]:
        
    for j in [1,2]:
            
        for k in [1,2]:
                
            for l in [1,2]:
                cuenta[f'{i}-{j}-{k}-{l}']=0
for combi in combinaciones:
    # if combi in cuenta: 
        cuenta[combi]+=1

print(cuenta)
