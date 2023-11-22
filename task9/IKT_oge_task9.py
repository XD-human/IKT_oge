from typing import Optional


class Vertex:
    def __init__(self, name):
        self.name = name
        self.to_neighbors = set()

    def add_neighbor(self, neighbor):
        """
        Добавить вершину графа, в которую можно добраться из этой вершины

        :param neighbor: Соседняя вершина графа.
        """
        self.to_neighbors.add(neighbor)
        return self

    def get_neighbors(self):
        """
        Вернуть вершины, в которые можно добраться из этой вершины
        """
        return self.to_neighbors

    def __repr__(self):
        return self.name


class Graph:
    def __init__(self, *vertexes):
        self.vertexes = {vertex.name: vertex for vertex in vertexes}

    def get_vertex(self, vertex_name) -> Vertex:
        """
        Вернуть вершины, входящие в граф
        """
        return self.vertexes[vertex_name]


class PathFinder:
    _paths = []

    def _find_paths(self, end, current_vertex, through_vertex: Vertex, not_through_vertex: Vertex, current_path):
        if current_vertex == end:
            if through_vertex and through_vertex not in current_path:
                return None
            
            if not_through_vertex and not_through_vertex in current_path:
                return None

            else:
                self._paths.append(current_path)
        else:
            neighbors = current_vertex.get_neighbors()
            for new_vertex in neighbors:
                if new_vertex in current_path:
                    continue
                new_path = current_path.copy() + [new_vertex]
                self._find_paths(end, new_vertex, through_vertex, not_through_vertex, new_path)

    def find_paths_from_a_to_b(self, start: Vertex, end: Vertex, through_vertex: Optional[Vertex] = None, not_through_vertex: Optional[Vertex] = None):
        """
        Найти все пути из одной вершины графа в другую.
        :param start: Вершина графа - начало искомого путь
        :param end: Вершина графа - конец искомого пути
        :param through_vertex: Вершина графа, через которую должен пройти путь 
        :param not_through_vertex: Вершина графа, через которую путь не должен пройти
        """
        self._paths = []
        self._find_paths(end, start, through_vertex, not_through_vertex, [start])
        return self._paths
    
    def print_paths(self):
        """
        Вывести найденные пути.
        """
        for path in self._paths:
            vertex_names = [vertex.name for vertex in path]
            print("".join(vertex_names))
            
if __name__ == "__main__":
    # Use case 1
    print("1 задача")

    vertices = [
        Vertex("А"),
        Vertex("Б"),
        Vertex("В"),
        Vertex("Г"),
        Vertex("Д"),
        Vertex("Е"),
        Vertex("Ж"),
        Vertex("К"),
        Vertex("Л"),
        Vertex("М"),
        Vertex("Н"),
        Vertex("П"),
        Vertex("Р"),
        Vertex("С"),
        Vertex("Т"),
    ]

    vertices_dict = {vertex.name: vertex for vertex in vertices}

    vertices_dict["А"] \
        .add_neighbor(vertices_dict["Б"]) \
        .add_neighbor(vertices_dict["Г"]) \
        .add_neighbor(vertices_dict["Д"]) \

    vertices_dict["Б"] \
        .add_neighbor(vertices_dict["В"]) \
        .add_neighbor(vertices_dict["Г"]) \

    vertices_dict["В"] \
        .add_neighbor(vertices_dict["Ж"]) \

    vertices_dict["Г"] \
        .add_neighbor(vertices_dict["В"]) \
        .add_neighbor(vertices_dict["Ж"]) \
        .add_neighbor(vertices_dict["Е"]) \

    vertices_dict["Д"] \
        .add_neighbor(vertices_dict["Е"]) \

    vertices_dict["Е"] \
        .add_neighbor(vertices_dict["Ж"]) \

    vertices_dict["Ж"] \
        .add_neighbor(vertices_dict["К"]) \
        .add_neighbor(vertices_dict["Л"]) \
        .add_neighbor(vertices_dict["М"]) \
        .add_neighbor(vertices_dict["Н"]) \

    vertices_dict["К"] \
        .add_neighbor(vertices_dict["Л"]) \
        .add_neighbor(vertices_dict["П"]) \

    vertices_dict["Л"] \
        .add_neighbor(vertices_dict["П"]) \

    vertices_dict["М"] \
        .add_neighbor(vertices_dict["Л"]) \
        .add_neighbor(vertices_dict["П"]) \

    vertices_dict["Н"] \
        .add_neighbor(vertices_dict["М"]) \

    vertices_dict["П"] \
        .add_neighbor(vertices_dict["Р"]) \
        .add_neighbor(vertices_dict["С"]) \

    vertices_dict["Р"] \
        .add_neighbor(vertices_dict["Т"]) \

    vertices_dict["С"] \
        .add_neighbor(vertices_dict["Т"]) \

    graph = Graph(*vertices)


    finder = PathFinder()
    paths = finder.find_paths_from_a_to_b(
        start = graph.get_vertex("А"),
        end = graph.get_vertex("Т"),
        through_vertex = graph.get_vertex("Л"),
    )
    finder.print_paths()
    print(f"Всего: {len(paths)}")
    print()

    # Use case 2: https://inf-oge.sdamgia.ru/problem?id=11027

    print("2 задача")
    vertices = [
        Vertex("А"),
        Vertex("Б"),
        Vertex("В"),
        Vertex("Г"),
        Vertex("Д"),
        Vertex("Е"),
        Vertex("Ж"),
        Vertex("З"),
        Vertex("И"),
        Vertex("К"),
        Vertex("Л"),
        Vertex("М"),
    ]

    vertices_dict = {vertex.name: vertex for vertex in vertices}

    vertices_dict["А"] \
        .add_neighbor(vertices_dict["Б"]) \
        .add_neighbor(vertices_dict["В"]) \
        .add_neighbor(vertices_dict["Г"]) \
        .add_neighbor(vertices_dict["Д"]) \

    vertices_dict["Б"] \
        .add_neighbor(vertices_dict["Е"]) \
        .add_neighbor(vertices_dict["В"]) \

    vertices_dict["В"] \
        .add_neighbor(vertices_dict["Е"]) \
        .add_neighbor(vertices_dict["Ж"]) \
        .add_neighbor(vertices_dict["З"]) \

    vertices_dict["Г"] \
        .add_neighbor(vertices_dict["В"]) \
        .add_neighbor(vertices_dict["З"]) \
        
    vertices_dict["Д"] \
        .add_neighbor(vertices_dict["Г"]) \
        .add_neighbor(vertices_dict["З"]) \

    vertices_dict["Е"] \
        .add_neighbor(vertices_dict["Ж"]) \
        .add_neighbor(vertices_dict["И"]) \

    vertices_dict["Ж"] \
        .add_neighbor(vertices_dict["И"]) \

    vertices_dict["З"] \
        .add_neighbor(vertices_dict["Ж"]) \
        .add_neighbor(vertices_dict["И"]) \

    vertices_dict["И"] \
        .add_neighbor(vertices_dict["К"]) \
        .add_neighbor(vertices_dict["Л"]) \

    vertices_dict["К"] \
        .add_neighbor(vertices_dict["М"]) \
        
    vertices_dict["Л"] \
        .add_neighbor(vertices_dict["М"]) \

    graph = Graph(*vertices)


    paths = finder.find_paths_from_a_to_b(
        start = vertices_dict["А"],
        end = vertices_dict["М"],
        through_vertex = vertices_dict["Л"],
        not_through_vertex = vertices_dict["Е"],
    )

    finder.print_paths()
    print(f"Всего: {len(paths)}")
