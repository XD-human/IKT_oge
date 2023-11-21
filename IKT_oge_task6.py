class Solver:
    def __init__(self, condition):
        '''
        Инициализировать конкретную задачу типа B6 из ОГЭ по информатике

        :param condition: Условие, которое будет проверяться в задании. Является функцией-предикатом, которая принимает несколько аргументов и возвращает True или False
        '''
        self.condition = lambda iterable: condition(*iterable)
    
    def solve_problem(self, inputs):
        result = filter(self.condition, inputs)

        return list(result)


# use case
solver = Solver(lambda s, t: not (s > 8 or t > 8))
inputs = ((8, 8), (9, 6), (4, 7), (6, 6), (-9, -2), (-5, 9), (-10, 10), (6, 9), (10, 6))
result = solver.solve_problem(inputs)
print(result)           # [(8, 8), (4, 7), (6, 6), (-9, -2)]
print(len(result))      # 4
