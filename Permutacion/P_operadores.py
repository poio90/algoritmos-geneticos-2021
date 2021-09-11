import random
import numpy as np

"""
OPERADORES DE MUTACION
"""

def mutacion_intercambio_reciproco(self,individuo):
    """
    mutacion_intercambio_reciproco(self,individuo)

    Procedimiento:
    1. Seleccionar dos posiciones al azar del individuo pasado por parametro.
    2. Intercambia los valores correspondientes a esas posiciones.

    Parameters
    ----------
    self : objeto GeneticoPermutaciones
    individuo : array de tamaño n que representa un individuo 
    de la población.

    Returns
    -------
    None: Cambia internamente los individuos de la población.
    
    Example
    -------
    individuo=[1, 2, 3, 4, 5]
    posicion_1 = 1
    posicion_2 = 3
    resultado: 
        individuo=[1, 4, 3, 2, 5]

    """
    if random.uniform(0,1) < self.prob_muta:
        posicion_1 = random.randint(0,len(individuo)-1)
        while True:
            posicion_2 = random.randint(0,len(individuo)-1)
            if(posicion_2 != posicion_1):
                break
        aux = individuo[posicion_1]
        individuo[posicion_1] = individuo[posicion_2]
        individuo[posicion_2] = aux

def mutacion_inversion(self,individuo):
    """
    mutacion_inversion(self,individuo)

    Procedimiento:
    1. Seleccionar dos posiciones dentro de un cromosoma al azar.
    2. Invertir el substring entre estas dos posiciones

    Parameters
    ----------
    self : objeto GeneticoPermutaciones
    individuo : array de tamaño n que representa un individuo 
    de la población.

    Returns
    -------
    None: Cambia internamente los individuos de la población.
    
    Example
    -------
    individuo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    posicion_1 = 7
    posicion_2 = 3
    resultado: 
        individuo = [1, 2, 3, 8, 7, 6, 5, 4, 9]

    """
    if random.uniform(0,1) < self.prob_muta:
        posicion_1 = random.randint(0,len(individuo)-1)
        while True:
            posicion_2 = random.randint(0,len(individuo)-1)
            if(posicion_2 != posicion_1):
                break

        while True:
            aux1 = individuo[posicion_1]
            aux2 = individuo[posicion_2]
            individuo[posicion_1] = aux2
            individuo[posicion_2] = aux1
            if (posicion_1 > posicion_2):
                posicion_1 -= 1
                posicion_2 += 1
            else:
                posicion_1 += 1
                posicion_2 -= 1
            if(abs(posicion_1-posicion_2)<=1):
                break

def mutacion_insercion(self,individuo):
    """
    mutacion_insercion(self,individuo)

    Procedimiento:
    1. Seleccionar un gen al azar.
    2. Insertar dicho gen en una posición elegida aleatoriamente .

    Parameters
    ----------
    self : objeto GeneticoPermutaciones
    individuo : array de tamaño n que representa un individuo 
    de la población.

    Returns
    -------
    None: Cambia internamente los individuos de la población.
    
    Example
    -------
    individuo=[1, 2, 3, 4, 5]
    gen_al_azar = 5
    posicion_a_insertar = 2
    resultado: 
        individuo=[1, 4, 5, 3, 2]

    """
    if random.uniform(0,1) < self.prob_muta:
        gen_al_azar = random.randint(0,len(individuo)-1)
        posicion_a_insertar = random.randint(0,len(individuo)-1)
        individuo.remove(gen_al_azar)
        individuo.insert(posicion_a_insertar,gen_al_azar)

def mutacion_desplazamiento(self,individuo):
    """
    mutacion_desplazamiento(self,individuo)

    Procedimiento:
    1. Seleccionar un substring al azar.
    2. Insertar dicho substring en una posición elegida aleatoriamente .

    Parameters
    ----------
    self : objeto GeneticoPermutaciones
    individuo : array de tamaño n que representa un individuo 
    de la población.

    Returns
    -------
    None: Cambia internamente los individuos de la población.
    
    Example
    -------
    individuo=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    posicion_1 = 3
    posicion_2 = 7 
    posicion_a_insertar=1
    resultado: 
        individuo=[1, 4, 5, 6, 7, 2, 3, 8, 9]

    """
    if random.uniform(0,1) < self.prob_muta:
        posicion_1 = random.randint(0,len(individuo)-1)
        while True:
            posicion_2 = random.randint(0,len(individuo)-1)
            if(posicion_2 != posicion_1):
                break
        posicion_a_insertar = random.randint(0,len(individuo)-1)
        if(posicion_1 > posicion_2):
            aux = posicion_2
            posicion_2 = posicion_1
            posicion_1 = aux

        for i in range(posicion_1, posicion_2):
            ind=individuo.pop(i)
            individuo.insert(posicion_a_insertar,ind)
            posicion_a_insertar+=1

"""
OPERADORES DE CRUCE
"""

def cruza_PMX(self,parent1,parent2):
    """
    cruza_PMX(self,parent1,parent2)

    Codigo obtenido de: https://stackoverflow.com/questions/53254449/how-to-perform-partial-mapped-crossover-in-python3
    
    Genera dos hijo por medio del cruce de dos individuos.

    El cruce es Partial Mapped Crossover: 
    1. Elegir un substring al azar
    2. Intercambiar los substrings entre los padres
    3. Establecer la relación de mapping
    4. Legalizar los offsprings con las relaciones de mapping

    Parameters
    ----------
    self : objeto GeneticoPermutaciones
    parent1 : array de tamaño n que representa un padre.
    parent2: array de tamaño n que representa un padre.

    Returns
    -------
    child1: lista de tamaño n que representa un hijo resultado
        del cruce de dos padres.
    child2: lista de tamaño n que representa un hijo resultado
        del cruce de dos padres.
    
    Example
    -------
    parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    parent2 = [5, 4, 6, 9, 2, 1, 7, 8, 3]
    firstCrossPoint = 2
    secondCrossPoint = 6
    resultado: 
        child1 = [3, 5, 6, 9, 2, 1, 7, 8, 4]
        child2 = [2, 9, 3, 4, 5, 6, 7, 8, 1]
    """

    firstCrossPoint = np.random.randint(0,len(parent1)-2)
    secondCrossPoint = np.random.randint(firstCrossPoint+1,len(parent1)-1)

    parent1MiddleCross = parent1[firstCrossPoint:secondCrossPoint]
    parent2MiddleCross = parent2[firstCrossPoint:secondCrossPoint]

    temp_child1 = parent1[:firstCrossPoint] + parent2MiddleCross + parent1[secondCrossPoint:]

    temp_child2 = parent2[:firstCrossPoint] + parent1MiddleCross + parent2[secondCrossPoint:]

    relations = []
    for i in range(len(parent1MiddleCross)):
        relations.append([parent2MiddleCross[i], parent1MiddleCross[i]])


    def recursion1 (temp_child , firstCrossPoint , secondCrossPoint , parent1MiddleCross , parent2MiddleCross) :
        child = np.array([0 for i in range(len(parent1))])
        for i,j in enumerate(temp_child[:firstCrossPoint]):
            c=0
            for x in relations:
                if j == x[0]:
                    child[i]=x[1]
                    c=1
                    break
            if c==0:
                child[i]=j
        j=0
        for i in range(firstCrossPoint,secondCrossPoint):
            child[i]=parent2MiddleCross[j]
            j+=1

        for i,j in enumerate(temp_child[secondCrossPoint:]):
            c=0
            for x in relations:
                if j == x[0]:
                    child[i+secondCrossPoint]=x[1]
                    c=1
                    break
            if c==0:
                child[i+secondCrossPoint]=j
        child_unique=np.unique(child)
        if len(child)>len(child_unique):
            child=recursion1(child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
        return(child)

    def recursion2(temp_child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross):
        child = np.array([0 for i in range(len(parent1))])
        for i,j in enumerate(temp_child[:firstCrossPoint]):
            c=0
            for x in relations:
                if j == x[1]:
                    child[i]=x[0]
                    c=1
                    break
            if c==0:
                child[i]=j
        j=0
        for i in range(firstCrossPoint,secondCrossPoint):
            child[i]=parent1MiddleCross[j]
            j+=1

        for i,j in enumerate(temp_child[secondCrossPoint:]):
            c=0
            for x in relations:
                if j == x[1]:
                    child[i+secondCrossPoint]=x[0]
                    c=1
                    break
            if c==0:
                child[i+secondCrossPoint]=j
        child_unique=np.unique(child)
        if len(child)>len(child_unique):
            child=recursion2(child,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
        return(child)

    child1=recursion1(temp_child1,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)
    child2=recursion2(temp_child2,firstCrossPoint,secondCrossPoint,parent1MiddleCross,parent2MiddleCross)

    return child1.tolist(), child2.tolist()

def cruza_OX(self, padre1, padre2):
    """
    cruza_OX(self,padre1,padre2)

    Genera un hijo por medio del cruce de dos individuos.
    El cruce es Order Crossover: 
    1. Seleccionar un substring aleatorio del primer padre.
    2. Copiar el substring en el hijo.
    3. Copiar los elementos restantes en el padre 2, al hijo, en el orden de aparición

    Parameters
    ----------
    self : objeto GeneticoPermutaciones
    padre1 : array de tamaño n que representa un padre.
    padre2: array de tamaño n que representa un padre.

    Returns
    -------
    hijo: array de tamaño n que representa un hijo resultado
        del cruce de dos padres.
    
    Example
    -------
    padre1=[1, 2, 3, 4, 5, 6]
    padre2=[6, 5, 4, 3, 2, 1]
    limite_inferior=1
    limite_superior=3
    resultado: 
        hijo=[6, 2, 3, 5, 4, 1]
    """
    hijo = [-1] * len(padre1)
    limite_inferior = random.randint(0,len(padre1)-1)
    limite_superior = random.randint(limite_inferior,len(padre1)-1)
    for lim in range(limite_inferior, limite_superior):
        hijo[lim] = padre1[lim]
    pointer=0
    for i in range(len(padre1)):
        if (padre2[i] not in hijo):
            if(pointer==limite_inferior):
                pointer=limite_superior
            hijo[pointer] = padre2[i]
            pointer+=1
    return hijo

def cruza_CX(self,padre1,padre2):
    """
    cruza_CX(self,padre1,padre2)

    Genera un hijo por medio del cruce de dos individuos.
    El cruce es Cycle Crossover:
    
    Procedimiento: 
    1. Hallar el ciclo definido por las posiciones correspondientes a los genes dentro de los
    padres.
    2. Copiar las ciudades del ciclo al hijo en las posiciones correspondientes a uno de los
    padres.
    3. Determinar las ciudades restantes del hijo al borrar aquellas ciudades que están en el ciclo
    desde el otro padre.
    4. Rellenar el hijo con los genes restantes.

    Parameters
    ----------
    self : objeto GeneticoPermutaciones
    padre1 : array de tamaño n que representa un padre.
    padre2: array de tamaño n que representa un padre.

    Returns
    -------
    hijo: array de tamaño n que representa un hijo resultado
        del cruce de dos padres.
    
    Example
    -------
    padre1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    padre2 = [5, 4, 6, 9, 2, 3, 7, 8, 1]
    resultado: 
        hijo = [1, 2, 6, 4, 5, 3, 7, 8, 9]
    """
    hijo = padre1[:]
    indice = 0
    ciclo=[]
    cantidad = 0
    ciclo.append(padre1[indice])
    while cantidad < len(padre1)-1:
        if (padre1[indice]!=padre2[indice] and padre2[indice] not in ciclo):
            ciclo.append(padre2[indice])
            indice = padre1.index(padre2[indice])
            cantidad+=1
        else:
            break
    i = 0
    for gen in padre2:
        if gen not in ciclo:
            hijo[i] = padre2[i]
        i+=1
    return hijo

def cruza_ER(self,cadena1,cadena2):
    raise NotImplementedError("Falta desarrollar el metodo")

"""
OPERADORES DE REEMPLAZO
"""

def reemplazo_mu_mas_lambda(self,individuos):
    """
    reemplazo_mu_mas_lambda(self,individuos)

    Dada una serie de individuos, modifica la población actual
    realizando el reemplazo mu mas lambda teniendo en cuenta si se elige elitismo 
    y el operador de seleccion en la configuracion inicial.

    """
    individuos = [(self.adaptacion(individuo), individuo)
                    for individuo in individuos]

    poblacion_auxiliar = self.poblacion + individuos

    n_poblacion_aux = self.n_poblacion 

    #Suma de Aptitudes de la Nueva Población
    suma_aptitudes=1.0*sum(p[0] for p in poblacion_auxiliar)
    #Fitness Relativo de cada individuo en poblacion_auxiliar
    fitness_relativo=[(p[0]/suma_aptitudes) for p in poblacion_auxiliar]

    #Elitismo
    if(self.posicion_mejor_individuo != -1):
        mejor_indiviudo = self.poblacion[self.posicion_mejor_individuo]
        n_poblacion_aux -= 1
        self.poblacion[n_poblacion_aux] = mejor_indiviudo

    if (self.tipo_operador_seleccion_para_reemplazo == 0):
        #seleccion para reemplazo torneo binario
        for i in range(n_poblacion_aux - 1):
            pos_ind = seleccion_torneo_binario(poblacion_auxiliar, len(poblacion_auxiliar))
            self.poblacion[i] = poblacion_auxiliar[pos_ind]

    if (self.tipo_operador_seleccion_para_reemplazo == 1):
        #seleccion para el reemplazo ruleta
        for i in range(n_poblacion_aux - 1):
            pos_ind = seleccion_ruleta(poblacion_auxiliar, fitness_relativo)
            self.poblacion[i] = poblacion_auxiliar[pos_ind]

    if (self.tipo_operador_seleccion_para_reemplazo == 2):
        #Seleccion para el reemplazo sus
        pos_ind = seleccion_SUS(poblacion_auxiliar,n_poblacion_aux - 1, fitness_relativo)
        i=0
        for p_ind in pos_ind:
            self.poblacion[i] = poblacion_auxiliar[p_ind]
            i+=1

    if (self.tipo_operador_seleccion_para_reemplazo == 3):
        #Seleccion para el reemplazo sus
        raise NotImplementedError("Falta desarrollar el metodo mu mejores")

    #Elitismo
    if (self.posicion_mejor_individuo != -1):
        self.posicion_mejor_individuo =  self.poblacion.index(min(self.poblacion))

def reemplazo_mu_lambda(self, individuos):

    """
    reemplazo_mu_lambda(self,individuos)

    Dada una serie de individuos, modifica la población actual
    realizando el reemplazo mu, lambda teniendo en cuenta si se elige elitismo 
    y el operador de seleccion en la configuracion inicial.

    """

    individuos = [(self.adaptacion(individuo), individuo)
                    for individuo in individuos]

    n_poblacion_aux = self.n_poblacion

    #Suma de aptitudes de los individuos
    suma_aptitudes=1.0*sum(ind[0] for ind in individuos)
    #Fitness Relativo de los individuos
    fitness_relativo=[(ind[0]/suma_aptitudes) for ind in individuos]
    
    #Elitismo
    if(self.posicion_mejor_individuo != -1):
        mejor_indiviudo = self.poblacion[self.posicion_mejor_individuo]
        n_poblacion_aux -=1
        self.poblacion[n_poblacion_aux] = mejor_indiviudo

    if (self.tipo_operador_seleccion_para_reemplazo == 0):
        #seleccion para reemplazo torneo binario
        for i in range(n_poblacion_aux - 1):
            pos_ind = seleccion_torneo_binario(individuos, len(individuos))
            self.poblacion[i] = individuos[pos_ind]

    if (self.tipo_operador_seleccion_para_reemplazo == 1):
        #seleccion para reemplazo ruleta
        for i in range(n_poblacion_aux - 1):
            pos_ind = seleccion_ruleta(individuos, fitness_relativo)
            self.poblacion[i] = individuos[pos_ind]

    if (self.tipo_operador_seleccion_para_reemplazo == 2):
        #seleccion para reemplazo sus
        pos_individuos_seleccionados=seleccion_SUS(individuos,n_poblacion_aux-1, fitness_relativo)
        i=0
        for pos_ind in pos_individuos_seleccionados:
            self.poblacion[i] = individuos[pos_ind]
            i+=1

    if (self.tipo_operador_seleccion_para_reemplazo == 3):
        raise NotImplementedError("Falta desarrollar el método mu mejores")
        #seleccion para mu mejores

    #Elitismo
    if (self.posicion_mejor_individuo != -1):
        self.posicion_mejor_individuo =  self.poblacion.index(min(self.poblacion))

def reemplazo_generacional(self,individuos):
    
    """
    reemplazo_generacional(self,individuos)

    Dada una serie de individuos, modifica la población actual
    realizando el reemplazo generacional teniendo en cuenta si se elige elitismo.

    """

    individuos = [(self.adaptacion(individuo), individuo)
                    for individuo in individuos]

    n_poblacion_aux = self.n_poblacion

    i = 0
    j = 0
    #Elitismo
    if(self.posicion_mejor_individuo != -1):
        mejor_indiviudo = self.poblacion[self.posicion_mejor_individuo]
        n_poblacion_aux -=1
    if (len(individuos) < n_poblacion_aux -1):
        while(j < len(individuos) and j < n_poblacion_aux -1 and i < n_poblacion_aux -1):
            if( i != self.posicion_mejor_individuo):
                self.poblacion[i] = individuos[j]
                j+=1
            i+=1
        j=0

    if (self.posicion_mejor_individuo != -1):
        self.posicion_mejor_individuo =  self.poblacion.index(min(self.poblacion))

"""
OPERADORES DE SELECCIÓN
"""

def seleccion_torneo_binario(poblacion, longitud_poblacion):
    """
    seleccion_torneo_binario(self)

    De toda la población, selecciona 2 individuos aleatorios
    y se queda con el que tiene mejor fitness de ellos.

    Parameters
    ----------
    self : objeto GeneticoPermutaciones

    Returns
    -------
    posición donde se encuentra el individuo elegido del array
    población.
    
    """
    n_random_1 = random.randint(0,longitud_poblacion-1)
    n_random_2 = random.randint(0,longitud_poblacion-1)
    return (n_random_1
            if poblacion[n_random_1][0] < poblacion[n_random_2][0]
            else n_random_2)

def seleccion_ruleta(poblacion,fitness_relativo):
    """
    seleccion_ruleta(poblacion)

    De toda la población, selecciona un individuo aleatorio
    elegido aleatoriamente de una ruleta donde está 
    distribuida proporcionalmente las aptitudes de los 
    individuos.

    Parameters
    ----------
    poblacion : Array que representa la
    poblacion del objeto GeneticoPermutaciones

    Returns
    -------
    posición donde se encuentra el individuo elegido del array
    población.

    """
    aleatorio = random.uniform(0,1)
    acumulado = 0
    for i in range(len(poblacion)):
        acumulado+= fitness_relativo[i]
        if aleatorio <= acumulado:
            return i
    raise ValueError("No debe pasar esto")

def seleccion_SUS(poblacion,nro_padres,fitness_relativo):

    ruleta=makeWheel(poblacion,fitness_relativo)
    indice_padres=select(ruleta, nro_padres)
    
    return indice_padres

"""
Métodos auxiliares
"""

def makeWheel(population,relative_fitness):
    wheel = []
    total = sum(1/p[0] for p in population)
    top = 0
    pos=0
    for p in range(len(population)):
        f = relative_fitness[p]
        wheel.append((top, top+f, population[p], pos))
        top += f
        pos+=1

    return wheel

def binSearch(wheel, num):
    mid = len(wheel)//2
    low, high, answer, pos = wheel[mid]
    if low<=num<=high:
        return pos
    elif high < num:
        return binSearch(wheel[mid+1:], num)
    else:
        return binSearch(wheel[:mid], num)

def select(wheel, N):
    stepSize = 1.0/N
    answer = []
    r = random.uniform(0,1)
    answer.append(binSearch(wheel, r))
    while len(answer) < N:
        r += stepSize
        if r>1:
            r %= 1
        answer.append(binSearch(wheel, r))
    return answer

