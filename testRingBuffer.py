import unittest
from RingBuffer import RingBuffer

class TestRingBuffer(unittest.TestCase):

    def test_set_and_get(self):
        # Инициализация буфера размером 3
        rb = RingBuffer(3)

        # Добавляем элементы
        rb.set(1)
        rb.set(2)
        rb.set(3)

        # Проверяем элементы в порядке добавления
        self.assertEqual(rb.get(), 1)
        self.assertEqual(rb.get(), 2)
        self.assertEqual(rb.get(), 3)

    def test_buffer_wrap_around(self):
        # Инициализация буфера размером 3
        rb = RingBuffer(3)

        # Добавляем элементы больше размера буфера
        rb.set(1)
        rb.set(2)
        rb.set(3)
        rb.set(4)  # Должен перезаписать элемент 1

        # Проверяем элементы
        self.assertEqual(rb.get(), 2)
        self.assertEqual(rb.get(), 3)
        self.assertEqual(rb.get(), 4)

    def test_get_empty_buffer(self):
        rb = RingBuffer(3)
        # Пытаемся получить элемент из пустого буфера
        self.assertIsNone(rb.get())

    def test_buffer_full_overwrite(self):
        # Инициализация буфера размером 2
        rb = RingBuffer(2)

        # Заполняем буфер
        rb.set(1)
        rb.set(2)

        # Переписываем элементы
        rb.set(3)  # Перезаписывает элемент 1
        rb.set(4)  # Перезаписывает элемент 2

        # Проверяем элементы
        self.assertEqual(rb.get(), 3)
        self.assertEqual(rb.get(), 4)
        self.assertIsNone(rb.get())  # Буфер должен быть пуст

    def test_get_size_ring_buffer(self):
        rb = RingBuffer(5)
        # Проверка корректности размера буфера
        self.assertEqual(rb.get_size_ring_buffer(), 5)


if __name__ == '__main__':
    unittest.main()
