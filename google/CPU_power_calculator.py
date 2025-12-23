import time

def measure_speed():
    iterations = 10_000_000  # 10 миллионов операций
    print(f"Запуск теста на {iterations} операций...")
    
    start_time = time.perf_counter() # Самый точный замер времени
    
    # Пустой цикл — проверяем чистую скорость перебора
    for i in range(iterations):
        pass 
        
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    # Считаем, сколько времени заняла ОДНА итерация (в наносекундах)
    one_op = (total_time / iterations) * 1_000_000_000
    
    print("-" * 30)
    print(f"Общее время: {total_time:.4f} сек")
    print(f"Одна операция: {one_op:.2f} наносекунд")
    print("-" * 30)
    
    if one_op < 50:
        print("Статус: У тебя мощное ядро! Идеально для брутфорса.")
    else:
        print("Статус: Обычная скорость. Придется оптимизировать код!")

measure_speed()