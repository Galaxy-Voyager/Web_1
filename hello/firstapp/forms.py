from django import forms


class UserForm(forms.Form):
    """
    vyb = forms.NullBooleanField(label='Вы поедете в Сочи этим летом?')                                                  # Форма да/нет
    name = forms.CharField(label='Имя клиента')                                                                          # Форма поле отправить
    email = forms.EmailField(label='Электронный адрес', help_text='Обязательный символ - @')                             # Форма email
    ip_adres = forms.GenericIPAddressField(label='IP адрес', help_text='Пример формата 192.0.2.0')                       # Форма ввода IP адреса
    reg_text = forms.RegexField(label='Текст', regex='^[0-9][A-F][0=9]$')                                                # Хз ещё какая-то форма
    slug_text = forms.SlugField(label='Введите текст')                                                                   # И ещё...
    url_text = forms.URLField(label='Введите URL', help_text='Например http://www.google.com')                           # Поле ввода URL
    uuid_text = forms.UUIDField(label='Введите UUID', help_text='Формат хххххххх-хххх-хххх-хххх-хххххххххххх')           # Поле ввода UUID
    combo_text = forms.ComboField(label='Введите URL', fields=[forms.URLField(), forms.CharField(max_length=20)])        # Поле проверка заданных полей
    file_path = forms.FilePathField(label='Выберите файл',
                                    path='C:\Program Files\Python311',
                                    allow_files='True',
                                    allow_folders='True')                                                                # Поле для выбора файлов из списка по директории
    file = forms.FileField(label='Файл')                                                                                 # Поле для выбора файлов
    file = forms.ImageField(label='Изображение')                                                                         # Поле для выбора изображений
    file = forms.DateField(label='Введите дату')                                                                         # Поле для ввода даты
    time = forms.TimeField(label='Введите время')                                                                        # Поле для ввода времени
    date_time = forms.DateTimeField(label='Введите дату и время')                                                        # Поле для ввода даты и времени
    time_delta = forms.DurationField(label='Введите промежуток времени')                                                 # Поле для ввода промежутка времени
    date_time = forms.SplitDateTimeField(label='Введите дату и время')                                                   # Поле для раздельного ввода даты и времени
    num = forms.IntegerField(label='Введите целое число')                                                                # Поле для ввода целых чисел
    num = forms.DecimalField(label='Введите десятичное число', decimal_places=2)                                         # Поле для ввода десятичных чисел
    num = forms.FloatField(label='Введите число')                                                                        # Поле для ввода чисел с плавающей точкой
    ling = forms.ChoiceField(label='Выберите язык',
                             choices=((1, 'Английский'),
                                      (2, 'Немецкий'),
                                      (3, 'Французский')))                                                               # Поле для выбора данных из списка
    city = forms.TypedChoiceField(label='Выберите город',
                                  empty_value=None,
                                  choices=((1, 'Москва'),
                                           (2, 'Воронеж'),
                                           (3, 'Курск')))                                                                # Ещё одно поле для выбора данных из списка
    country = forms.MultipleChoiceField(label='Выберите страны',
                                        choices=((1, 'Англия'),
                                                 (2, 'Германия'),
                                                 (3, 'Испания'),
                                                 (4, 'Россия')))                                                         # Поле для множественного выбора данных из списка
    city = forms.TypedMultipleChoiceField(label='Выберите город',
                                          empty_value=None,
                                          choices=((1, 'Москва'),
                                                   (2, 'Воронеж'),
                                                   (3, 'Курск'),
                                                   (4, 'Томск')))                                                        # Ещё одно поле для выбора множественных данных
    """
    name = forms.CharField(label='Имя клиента', min_length=3)
    age = forms.IntegerField(label='Возраст клиента', min_value=1, max_value=100)
    required_css_class = 'field'
    error_css_class = 'error'