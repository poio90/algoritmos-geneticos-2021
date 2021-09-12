import random
"""
OPERADORES DE MUTACION
"""
def mutacion_swap(self,individuo):
    """
    mutacion_swap(self,individuo)

    Swapea 0 o más genes de un individuo según prob_muta.
<
    Parameters
    ----------
    self : objeto GeneticoBinario
    individuo : array de tamaño n que representa un individuo 
    de la población.

    Returns
    -------
    None: Cambia internamente los individuos de la población.
    
    Example
    -------
    individuo=[1,0,0,0,0]
    resultado: 
        individuo=[0,1,0,0,0]

    """
    for i in range(len(individuo)):
        if random.uniform(0,1) < self.prob_muta:
            if i == 1: 
                individuo[i] = 0
            else:
                individuo[i] = 1

"""
OPERADORES DE CRUCE
"""
def cruza_single_point(self,cadena1,cadena2):
    """
    cruza_single_point(self,cadena1,cadena2)

    Genera un hijo por medio del cruce de dos individuos.
    El cruce es single point y comienza desde un valor
    random representado por la variable corte.

    Parameters
    ----------
    self : objeto GeneticoBinario
    cadena1 : array de tamaño n que representa un padre.
    cadena2: array de tamaño n que representa un padre.

    Returns
    -------
    hijo: array de tamaño n que representa un hijo resultado
        del cruce de dos padres.
    
    Example
    -------
    cadena1=[1,0,0,0,0]
    cadena2=[0,0,0,1,1]
    corte=2
    resultado: 
        hijo=[1,0,0,1,1]

    """
    corte = random.randint(0,self.problema.n-1)
    hijo = cadena1[:]
    i=0
    for i in range(corte):
        hijo[i] = cadena1[i]
    for corte in range(i+1,self.problema.n):
        hijo[corte] = cadena2[corte]
    return hijo

def cruza_n_point(self,cadena1,cadena2,cantidad_puntos):
    """
    cruza_n_point(self,cadena1,cadena2,n)

    Genera un hijo por medio del cruce de dos individuos.
    El cruce es de multipoint y los cortes se dan por un
    valor random representado por la variable corte. la
    cantidad de cortes es representada por la variable
    cantidad_puntos

    Parameters
    ----------
    self : objeto GeneticoBinario
    cadena1 : array de tamaño n que representa un padre.
    cadena2: array de tamaño n que representa un padre.
    cantidad_puntos: Entero que representa la cantidad
    de cortes.

    Returns
    -------
    hijo: array de tamaño n que representa un hijo resultado
        del cruce de dos padres.
    
    Example
    -------
    cadena1=[1,1,1,1,1,1,1,1,1,1,1]
    cadena2=[0,0,0,0,0,0,0,0,0,0,0]
    cantidad_puntos = 3
    resultado: 
        hijo=[1,1,1,0,0,0,1,1,0]

    """
    if cantidad_puntos%2 != 0:
        hijo = cadena2[:]
    else:
        hijo = cadena1[:]
    swap=1
    limite = 0
    for _ in range(cantidad_puntos):
        i=limite
        corte = random.randint(limite,self.problema.n-1)
        limite=corte
        if swap==1:
            for i in range(i,corte):
                hijo[i] = cadena1[i]
                swap=2
        else:
            for i in range(i,corte):
                hijo[i] = cadena2[i]
                swap=1
    return hijo

def cruza_uniform(self,cadena1,cadena2):
    """
    cruza_uniform(self,cadena1,cadena2)

    Genera un hijo por medio del cruce de dos individuos.
    El cruce es uniforme, es decir, se utiliza una máscara
    por el cual se selecciona uno por uno los genes
    que van a quedar en el hijo.

    Parameters
    ----------
    self : objeto GeneticoBinario
    cadena1 : array de tamaño n que representa un padre.
    cadena2: array de tamaño n que representa un padre.

    Returns
    -------
    hijo: array de tamaño n que representa un hijo resultado
        del cruce de dos padres.
    
    Example
    -------
    cadena1=[1,1,1,1,1,1,1,1,1,1,1]
    cadena2=[0,0,0,0,0,0,0,0,0,0,0]
    mask = [0,1,1,0,1,1,1,1,0,1,1]

    resultado: 
        hijo=[0,1,1,0,1,1,1,1,0,1,1]

    """
    mask = [random.randint(0,1) for _ in range(len(cadena1))]
    hijo = cadena1[:]
    for i in range(len(mask)-1):
        if (mask[i] == 1):
            hijo[i] = cadena1[i]
        else: 
            hijo[i] = cadena2[i]
    return hijo

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
    individuos = [(self.adaptación(individuo), individuo)
                    for individuo in individuos]

    poblacion_auxiliar = self.poblacion + individuos

    poblacion_temp = []
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


    """if (self.tipo_operador_seleccion_para_reemplazo == 0):
        #seleccion para reemplazo torneo binario
        for _ in range(self.n_poblacion):
            n_random_1 = random.randint(0,self.n_poblacion + len(individuos) - 2)
            n_random_2 = random.randint(0,self.n_poblacion + len(individuos) - 2)

            if(n_random_1 > self.n_poblacion - 1):
                n_random_1 = random.randint(0,len(individuos) - 1)

                if(n_random_2 > self.n_poblacion - 1):
                    n_random_2 = random.randint(0,len(individuos) - 1)
                    poblacion_temp.append (individuos[n_random_1]
                        if individuos[n_random_1][0] > individuos[n_random_2][0]
                        else individuos[n_random_2])
                else:
                    poblacion_temp.append (individuos[n_random_1]
                        if individuos[n_random_1][0] > self.poblacion[n_random_2][0]
                        else self.poblacion[n_random_2])

            elif(n_random_2 > self.n_poblacion - 1):
                n_random_2 = random.randint(0,len(individuos) - 1)
                poblacion_temp.append (self.poblacion[n_random_1]
                        if self.poblacion[n_random_1][0] > individuos[n_random_2][0]
                        else individuos[n_random_2])
            else:
                poblacion_temp.append (self.poblacion[n_random_1]
                        if self.poblacion[n_random_1][0] > self.poblacion[n_random_2][0]
                        else self.poblacion[n_random_2])

        self.poblacion =  poblacion_temp"""


    if (self.tipo_operador_seleccion_para_reemplazo == 1):
        #seleccion para el reemplazo ruleta
        for i in range(n_poblacion_aux - 1):
            pos_ind = seleccion_ruleta(poblacion_auxiliar,fitness_relativo)
            self.poblacion[i] = poblacion_auxiliar[pos_ind]

    if (self.tipo_operador_seleccion_para_reemplazo == 2):
        #Seleccion para el reemplazo sus
        pos_ind = seleccion_SUS(poblacion_auxiliar,n_poblacion_aux - 1, fitness_relativo)
        i=0
        for p_ind in pos_ind:
            self.poblacion[i] = poblacion_auxiliar[p_ind]
            i+=1

    if (self.tipo_operador_seleccion_para_reemplazo == 3):
        #Seleccion para el reemplazo mu mejores
        for i in range(n_poblacion_aux - 1):
            pos_ind = poblacion_auxiliar.index(max(poblacion_auxiliar))
            self.poblacion[i] = poblacion_auxiliar.pop(pos_ind)


    #Elitismo
    if (self.posicion_mejor_individuo != -1):
        self.posicion_mejor_individuo =  self.poblacion.index(max(self.poblacion))

def reemplazo_mu_lambda(self, individuos):
    """
    reemplazo_mu_lambda(self,individuos)

    Dada una serie de individuos, modifica la población actual
    realizando el reemplazo mu, lambda teniendo en cuenta si se elige elitismo 
    y el operador de seleccion en la configuracion inicial.

    """

    individuos = [(self.adaptación(individuo), individuo)
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
        #Seleccion para el reemplazo mu mejores
        for i in range(n_poblacion_aux - 1):
            pos_ind = individuos.index(max(individuos))
            self.poblacion[i] = individuos.pop(pos_ind)

    #Elitismo
    if (self.posicion_mejor_individuo != -1):
        self.posicion_mejor_individuo =  self.poblacion.index(max(self.poblacion))


def reemplazo_generacional(self,individuos):

    """
    reemplazo_generacional(self,individuos)

    Dada una serie de individuos, modifica la población actual
    realizando el reemplazo generacional teniendo en cuenta si se elige elitismo.

    """

    individuos = [(self.adaptación(individuo), individuo)
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
        self.posicion_mejor_individuo =  self.poblacion.index(max(self.poblacion))


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
    self : objeto GeneticoBinario

    Returns
    -------
    posición donde se encuentra el individuo elegido del array
    población.
    
    """
    n_random_1 = random.randint(0,longitud_poblacion-1)
    n_random_2 = random.randint(0,longitud_poblacion-1)
    return (n_random_1
            if poblacion[n_random_1][0] > poblacion[n_random_2][0]
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
    poblacion del objeto GeneticoBinario
    fitness_relativo: es el fitness relativo de cada individuo de 
    la poblacion segun el fitness total.
    Returns
    -------
    posición donde se encuentra el individuo elegido del array
    población.

    """
    aleatorio = random.uniform(0,1)
    acumulado = 0
    suma_aptitudes = 1.0 * sum([x[0] for x in poblacion])
    for i in range(len(poblacion)):
        acumulado+= fitness_relativo[i]
        if aleatorio <= acumulado:
            return i
    raise ValueError("No debe pasar esto")

def seleccion_SUS(poblacion,nro_padres,fitness_relativo):

    """
    seleccion_SUS(poblacion,nro_padres,fitness_relativo):

    De toda la población, selecciona "nro_padres" individuos aleatorios
    de una ruleta donde están distribuida proporcionalmente las aptitudes de los 
    individuos.

    Parameters
    ----------
    poblacion : Array que representa la
    poblacion del objeto GeneticoBinario
    nro_padres: es la cantidad de padres que se van a seleccionar de la ruleta.
    fitness_relativo: es el fitness relativo de cada individuo de 
    la poblacion segun el fitness total.

    Returns
    -------
    posiciones donde se encuentran los individuos elegidos del array de
    población.

    """
    ruleta=makeWheel(poblacion,fitness_relativo)
    indice_padres=select(ruleta, nro_padres)
    
    return indice_padres


"""Métodos auxiliares"""

def makeWheel(population,relative_fitness):
    wheel = []
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

