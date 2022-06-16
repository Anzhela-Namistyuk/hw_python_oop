# Модуль фитнес-трекера

## Краткое описание проекта.
Модуль для фитнес-трекера рассчитывает и отображает результаты для трех  видов 
тренировок: бег, спортивная ходьба и плавание.

Информационное сообщение включает такую информацию:
- тип тренировки (бег, ходьба или плавание);
- длительность тренировки
- дистанция, которую преодолел пользователь, в километрах;
- среднюю скорость на дистанции, в км/ч;
- расход энергии, в килокалориях.

### Технологии.
```
Python 3
```
### Как запустить проект.

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
- Запустить проект командой:
```
python homework.py
```

### Тестовые данные.
```
if __name__ == '__main__':
    packages = [        
        ('SWM', [628, 1, 80, 25, 40]),
        ('RUN', [12200, 1, 75]),
        ('WLK', [8900, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training) 
```


### Автор.
Анжела Намистюк


