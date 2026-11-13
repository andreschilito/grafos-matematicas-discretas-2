# Proyecto Grafos Matemáticas Discretas II

Implementación de grafos usando Python.

## Point 3: Undirected graph representation

### Elección de la representación

Inicialmente pensamos en utilizar una lista de aristas, ya que nos parecía la forma más sencilla de representar un grafo. Sin embargo, al revisar los siguientes puntos del proyecto, decidimos utilizar listas de adyacencia, porque consideramos que nos facilitarán la implementación de las funciones que debemos desarrollar después. También consideramos utilizar una matriz de adyacencia, pero esta opción nos pareció más extensa porque tendríamos que manejar filas, columnas y posiciones de los vértices. Por eso preferimos trabajar con listas de adyacencia, utilizando diccionarios y listas de Python.

### Implementación

La idea es utilizar un diccionario donde cada vértice tiene una lista con sus vecinos. Por lo que consideramos necesarias dos funciones:

- **`add_vertex(graph, vertex)`:** agrega un vértice al grafo si no existe y le asigna una lista vacía.
- **`add_edge(graph, vertex1, vertex2)`:** verifica que ambos vértices existan y los conecta en ambos sentidos.

## Point 4: Directed graph representation

### Elección de la representación

Para los grafos dirigidos decidimos continuar utilizando listas de adyacencia. Las razones son iguales a las del punto anterior y, de paso, podemos aprovechar la misma estructura. La diferencia es que las aristas ahora tienen una dirección específica, por lo que no es necesario guardar las conexiones en ambos sentidos.

En clase hubo alguien que dijo que pudo utilizar un mismo código para ambos tipos de grafos usando una línea de código adicional. Sinceramente, no sabemos cómo lo hicieron, pero intentamos replicarlo teniendo esa idea en mente.

### Implementación

Utilizamos la función `add_vertex()` del punto 3 y agregamos una nueva función:

- **`add_directed_edge(graph, source, target)`:** buscamos verificar que ambos vértices primero existan y luego agregar una arista desde el vértice de origen hacia el de destino.

## Point 5: Load a graph from a CSV file

### Implementación

Para este punto debemos crear una función que permita leer los archivos CSV proporcionados y construir un grafo a partir de sus valores. Comenzamos con:

- **`load_graph(file_path, directed=False)`:** recibe la ruta del archivo y permite indicar si el grafo es dirigido o no dirigido. Esto debe hacerse manualmente: si es dirigido, debemos cambiar el valor de `directed` a `True`; si no es dirigido, lo mantenemos en `False`.

La función abre el archivo, omite la primera línea y recorre las siguientes, separando los valores de `source`, `target` y `weight` mediante las comas.

Después utilizamos `add_edge()` o `add_directed_edge()`, dependiendo del valor de `directed`, para agregar las conexiones al grafo. Los pesos (`weights`) los almacenamos en un diccionario separado, ya que las funciones anteriores solo guardan los vecinos de cada vértice. De esta forma podemos reutilizar las implementaciones previas.

Finalmente, la función devuelve el grafo y sus pesos.

## Point 6: Graph connectivity

### Implementación

Para verificar si un grafo es conexo, buscamos recorrer sus vértices y comprobar si es posible llegar a todos ellos.

Para esto utilizamos dos listas: `visited`, que almacena los vértices ya visitados, y `pending`, que almacena los vértices pendientes por revisar.

- **`is_connected(graph, directed=False)`:** recorre el grafo y comprueba si todos sus vértices son alcanzables, retornando e imprimiendo `True` o `False`. Igual que en el punto anterior, si el grafo es dirigido o no dirigido depende del valor asignado a `directed`, por lo que debemos indicarlo manualmente.

En los grafos no dirigidos comenzamos el recorrido desde un solo vértice, mientras que en los dirigidos realizamos el recorrido desde cada vértice para verificar que todos puedan alcanzar a los demás y así garantizar que el grafo sea fuertemente conexo.

Luego, comparamos la cantidad de vértices visitados con la cantidad total de vértices del grafo para determinar el resultado.
