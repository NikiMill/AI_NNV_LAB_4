#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# C помощью алгоритма поиска с ограничением глубины найдем минимальное расстояние между начальным и конечным пунктами
import itertools

def calculate_total_distance(route, distance_matrix):
    """Вычисление общей дистанции для данного маршрута."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    # Добавляем расстояние обратно к начальной точке
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def traveling_salesman(distance_matrix):
    """Решение задачи коммивояжера методом полного перебора."""
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_route = None
    # Генерация всех возможных маршрутов
    for route in itertools.permutations(cities):
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
    return best_route, min_distance

# Пример использования
if __name__ == "__main__":
    # Матрица расстояний между городами для 10 узлов
    distance_matrix = [
        [0, 634, 246, 420, 98, 181, 853, 462, 457, 199],
        [634, 0, 719, 545, 732, 815, 1487, 1096, 983, 833],
        [246, 719, 0, 174, 183, 100, 938, 708, 703, 284],
        [420, 545, 174, 0, 357, 274, 1112, 882, 877, 458],
        [98, 732, 183, 357, 0, 83, 755, 560, 555, 101],
        [181, 815, 100, 274, 83, 0, 838, 643, 638, 184],
        [853, 1487, 938, 1112, 755, 838, 0, 462, 674, 654],
        [462, 1096, 708, 882, 560, 643, 462, 0, 212, 661],
        [457, 983, 703, 877, 555, 638, 674, 212, 0, 656],
        [199, 833, 284, 458, 101, 184, 654, 661, 656, 0],
    ]

    best_route, min_distance = traveling_salesman(distance_matrix)
    print(f"Лучший маршрут: {best_route}")
    print(f"Минимальное расстояние: {min_distance}")
