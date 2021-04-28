import math
def ingresarMatriz(n):
    matriz=[] #Declaramos una lista vacía llamada Matriz
    for i in range(n): #Ahora con un ciclo FOR vamos a recorrer 
        matriz.append([]) #Vamos a insertar una lista a cada elemento de la lista 'matriz', esto provocará que esta se convierta en una matríz
        for j in range(n):
            valor= float(input(f"Ingrese el valor para la matriz en [{i},{j}] -> "))
            matriz[i].append(valor) #Aqui simplemente inyectamos el valor que nos proporciona el usuario por teclado en el índice de la matríz mostrado
    return matriz

def ingresarVector(n):
    vector=[] #Declaramos una lista vacía llamada vector
    for i in range(n): #Ahora con un ciclo FOR vamos a recorrer la lista
        valor= float(input(f"Ingrese el valor para el vector en [{i}] -> "))
        vector.append(valor) #Aqui simplemente inyectamos el valor que nos proporciona el usuario por teclado en el índice del vector mostrado
    return vector #Regresamos el vector que ingresamos por teclado

def sumaMatrices(matrizA,matrizB,n): #Aqui nos va a pedir siempre en este orden: MatrizA, MatrizB, tamaño de las matrices
    suma=[] #Declaramos una lista auxiliar 'suma'
    for i in range(n):
        suma.append([]) #A cada elemento de la lista le agregaremos una lista, haciendo asi una matriz
        for j in range(n):
            suma[i].append(matrizA[i][j]+matrizB[i][j])  #Tomamos cada elemento de la matriz y los sumamos
    return suma #Retornamos la matriz con los elementos ya sumados

def restaMatrices(matrizA,matrizB,n): #Aqui nos va a pedir siempre en este orden: MatrizA, MatrizB, tamaño de las matrices
    resta=[] #Declaramos una lista auxiliar 'resta'
    for i in range(n):
        resta.append([]) #A cada elemento de la lista le agregaremos una lista, haciendo asi una matriz
        for j in range(n):
            resta[i].append(matrizA[i][j]-matrizB[i][j])  #Tomamos cada elemento de la matriz y los restamos
    return resta #Retornamos la matriz con los elementos ya restados

def sumaVectores(vecA,vecB,n):
    suma=[] #Declaramos una lista auxiliar 'suma'
    for i in range(n):
        suma.append(vecA[i]+vecB[i]) #Sumamos cada elemento del vector y lo guardamos en suma[]
        #print("La suma será entre: ",vecA[i]," y ",vecB[i], " es ",suma[i])
    return suma #Retornamos el vector con los elementos ya sumados

def restaVectores(vecA,vecB,n):
    resta=[] #Declaramos una lista auxiliar 'resta'
    for i in range(n):
        resta.append(vecA[i]-vecB[i]) #Restamos cada elemento del vector y lo guardamos en resta[]
        #print("La resta será entre: ",vecA[i]," y ",vecB[i], " es ",resta[i])
    return resta #Retornamos el vector con los elementos ya restados

#En este pedazo de código imprimimos la matriz que creamos previamente, con un formato mas bonito  
def mostrarMatriz(matriz):
    print()
    for i in matriz:
        print("[", end=" ")
        for j in i:
            print("{:6.5f}".format(j), end= " ")
        print("]")
    print()

#En este pedazo de código imprimimos el vector que creamos previamente, con un formato mas bonito  
def mostrarVector(vector):
    print()
    print("[", end=" ")
    for i in vector:
        print("{:6.5f}".format(i),",", end= " ")
    print("]")
    print()

#algoritmo de producto punto que nos será muy util para este algoritmo. toma por parámetros 2 vectores y un entero, el vector A, el vector B y el tamaño de estos vectores, queda de mas decir que ambos deben de ser de igual tamaño
def productoPunto(vec1,vec2):
    pp=0  #Inicializamos una variable llamada pp, por ProductoPunto
    i=0   #Inicializamos una variable como contador para el ciclo
    while i<(len(vec1)):
        pp = float(pp + (vec1[i] * vec2[i])) #a la variable pp vamos a sumarle si mismo mas el producto de los vectores 1 y 2 en su respectivo indice y asi acumulandose
        #print("Resultado del Producto Punto es: ",pp)
        i=i+1 #Incrementamos el contador
    #print("El resultado a regresar es: ",pp)
    return pp #FUNCIONA

def proyeccion(u,v): #proy_u (v)
    proy=[] #Inicializamos una lista auxiliar que contendrá la proyeccion final
    escalar=(productoPunto(v,u))/(productoPunto(u,u)) #Debido a que la proyección es una division de 2 productos punto, al final termina siendo un escalar, el cual lo calculamos y este lo multiplicamos por cada elemento del vector u
    for i in range(len(u)):
        proy.append(escalar * u[i]) #Multiplicamos el escalar previamente calculado por cada elemento del vector u y lo añadimos a proy
    #print("Resultado de la proyeccion es",proy)
    return proy #FUNCIONA

def norma(vector):
    N=0
    i=0
    while i<len(vector):
        N=N+(vector[i]**2)
        i=i+1
    N=math.sqrt(N)
    return N

def Normalizar(vector):
    vectorNormalizado=[]
    N=norma(vector)
    i=0
    while i<len(vector):
        vectorNormalizado.append(vector[i]/N)
        i=i+1
    return vectorNormalizado
    
def Transpuesta(matriz):
    T=[]
    for i in range(len(matriz)):
        T.append([])
        for j in range(len(matriz)):
            T[i].append(matriz[j][i])
    return T

def gramSchmidt(matrizX):
    matrizV=[]
    matrizE=[]
    n=len(matrizX)
    i=0
    
    while i<n:
        if i==0:
            # V_1 = X_1
            matrizV.append(matrizX[i])
            print("MatrizV: ",matrizV)
        else:
            #print("Iteración ",i,"De Gram Schmidt")
            #Hacemos la resta del vector X_i - Combinación Lineal, calculada en auxGS
            matrizV.append(restaVectores(matrizX[i],auxGS(matrizX,matrizV,i),n))
        #print("V_",i+1,": ",matrizV[i])
        matrizE.append(Normalizar(matrizV[i])) #Ahora vamos a normalizar el vector que acabamos de calcular, dividiendolo sobre su norma
        i=i+1
    #print("La resta final del algoritmo de Gram Schmidt es: ",matrizV)
    return Transpuesta(matrizE) #Devuelve la matriz ORTONORMALIZADA
    #return Transpuesta(matrizV) #Devuelve la matriz ORTOGONALIZADA
    

    #Calculamos la combinación lineal para las proyecciones, la cual va a ser restada de el vector X en gramSchmidt
def auxGS(matrizX,matrizV,tope):
    #print(matrizV)
    aux=[0]*len(matrizX) #Declaramos un vector auxiliar para ir guardando el vector sumado
    i,j,n=0,0,len(matrizX) #Declaro las variables que van a ser utiles
    #print("Fuera del while de auxGS")
    while i<tope: #Aqui se va a ciclar un while desde 0 hasta n-1, el cual este va a ser el indice k del vector V_k de la combinación lineal de Gram Schmidt
        #print("Dentro del while de auxGS")
        while j<n: #Vamos a ciclar el programa, para guardar cada una de las componentes del vector sumado, de la combinación lineal realizada
            """
            Aqui vamos a calcular la combinación lineal, de la suma de Riemman con k=1 hasta i-1

                    <X_i ° V_k>
                    ----------- V_k
                    <V_k ° V_k>

            """
            aux[j]=sumaVectores(aux,proyeccion(matrizV[i],matrizX[tope]),n)[j]
            j=j+1
        i = i+1
        #print("Vector auxiliar: ",aux)
        j=0
    #print("La suma de la combinación lineal de Gram Schmidt es: ",aux)
    return aux #Retornamos la combinación lineal ya sumada

def productoMatrices(A,B):
    n=len(A)
    C=[]
    for i in range(n):
        C.append([])
        for j in range(n):
            valor = 0
            C[i].append(valor)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]=C[i][j]+(A[i][k]*B[k][j])
    return C

def algoritmoQR(A):
    i=0
    A_1=A
    while i<100:
        A0=A_1
        Q=gramSchmidt(Transpuesta(A0))
        R=productoMatrices(Transpuesta(Q),A0)
        A_1=productoMatrices(R,Q)
        print("Q ", Q)
        print("R ", R)
        print("Matriz A_",i+1)
        mostrarMatriz(A_1)
        i=i+1
    return A0

def mostrarEV(QR):
    i,n=0,len(QR)
    while i<n:
        print("Eigenvalor ",i+1,": ",QR[i][i])
        i=i+1

#------------------------------------------SIEMPRE DEJAR ESTO AL FINAL-----------------------------------
def main():
    n=int(input("Ingrese el tamaño de la matriz cuadrada ->"))
    A=ingresarMatriz(n)
    #Nota: Mando la matriz transpuesta que ingresamos, para asi poder trabajar los vectores columna, como vectores fila, haciendo asi mas facil el hacer las operaciones. Y dado que nos retorna la transpuesta de la matriz X ortonormalizada, no hay diferencia a simple vista, solo es para trabajar mas cómodamente las matrices.
    Q=gramSchmidt(Transpuesta(A))
    mostrarMatriz(Q)
    R=productoMatrices(Transpuesta(Q),A)
    QR=algoritmoQR(A)
    mostrarMatriz(QR)
    print("Los Eigenvalores son: ")
    mostrarEV(QR)
main()