def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Если левый потомок больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок больше наибольшего элемента
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
        heapify(arr, n, largest)  # Рекурсивно heapify

def create_heap(arr):
    n = len(arr)
    # Начинаем с последнего нелистового узла и движемся к корню
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


lst = [4, 10, 3, 5, 1, 2, 12]
create_heap(lst)
print("Куча:", lst)