import random
import matplotlib.pyplot as plt


def generate_random_numbers():
    random_numbers = [random.randint(30, 100) for _ in range(6)]

    even_count = sum(1 for num in random_numbers if num % 2 == 0)
    odd_count = len(random_numbers) - even_count

    print("Сгенерированные числа:", random_numbers)
    print("Количество четных чисел:", even_count)
    print("Количество нечетных чисел:", odd_count)

    labels = ['Четные', 'Нечетные']
    counts = [even_count, odd_count]

    fig, ax = plt.subplots(figsize=(8, 6))

    wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90,
                                      colors=['blue', 'orange'])

    plt.setp(autotexts, size=12, weight="bold", color="white")
    ax.set_title('Соотношение четных и нечетных чисел', fontsize=14)

    plt.figtext(0.8, 0.5, f"Сгенерированные числа:\n{random_numbers}", fontsize=12, ha='center',
                bbox=dict(facecolor='lightgrey', alpha=0.5))

    plt.axis('equal')
    plt.show()

generate_random_numbers()
