

corridas="""-
+
+
-
+
-
+
+
-
+
-
+
-
-
+
-
+
-
+
+
-
+
+
-
-
+
-
+
-
-
-
-
+
-
+
-
-
-
+
-
+
+
-
-
+
+
+
+
-
-
-
-
+
-
+
-
+
-
+
-
-
+
+
-
+
-
-
+
-
-
+
+
-
-
+
+
-
+
-
-
-
+
+
-
+
+
-
+
-
-"""
# corridas=corridas.split()
# print(corridas)
# cambios=0
# actual=corridas[0]
# for corrida in corridas[1:]:
    
#     if(actual!=corrida):
#         cambios+=1
#         actual=corrida
# print(cambios)
    
# for i in [1,2]:
        
#     for j in [1,2]:
            
#         for k in [1,2]:
                
#             for l in [1,2]:
#                 print(f'{i}-{j}-{k}-{l}')

datos="""0.3163
0.1319
0.7299
0.9208
0.2948
0.7113
0.0049
0.8394
0.9723
0.4438
0.6235
0.3847
0.7804
0.6049
0.5349
0.962
0.3062
0.9096
0.5747
0.6208
0.685
0.592
0.7617
0.8835
0.4767
0.1635
0.4579
0.1908
0.9173
0.9083
0.7126
0.5667
0.0349
0.9255
0.6599
0.8236
0.2829
0.2296
0.1024
0.8892
0.0706
0.3063
0.5806
0.4443
0.3435
0.6034
0.6305
0.7366
0.7757
0.4907
0.237
0.1856
0.0346
0.9882
0.2011
0.7348
0.2248
0.7795
0.0686
0.0985
0.0508
0.026
0.0777
0.6643
0.3657
0.7218
0.6775
0.4993
0.7607
0.4864
0.2889
0.6874
0.9016
0.425
0.2277
0.3438
0.7706
0.5853
0.7624
0.6681
0.3303
0.2913
0.52
0.6495
0.2234
0.591
0.9042
0.2841
0.764
0.5752"""
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

