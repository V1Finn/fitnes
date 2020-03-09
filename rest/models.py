from django.db import models


class Coach(models.Model):
	short_name = models.CharField(max_length=30, verbose_name='Имя')
	name = models.CharField(primary_key=True, max_length=90, verbose_name='ФИО')
	position = models.CharField(max_length=150, verbose_name='Квалификация')
	imageUrl = models.URLField(verbose_name='Фото')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тренер'
		verbose_name_plural = 'Тренеры'


class School(models.Model):
	NAME = (
		(None, 'Выберете вид занятия'),
		('Yoga', 'Yoga'),
		('Stretch', 'Stretch'),
		('Stretch1', 'Stretch1')
	)
	COLOR = (
		(None, 'Выберете сложность'),
		('#ff0000', 'Red'),
		('#008000', 'Green'),
		('#ffff00', 'Yellow')
	)
	PLACE = (
		(None, 'Выберете зал'),
		('Студия 1', 'Студия 1'),
		('Студия 2', 'Студия 2'),
		('Студия 3', 'Студия 3')
	)
	WEEKDAY = (
		(None, 'Выберете день'),
		('1', 'Понедельник'),
		('2', 'Вторник'),
		('3', 'Среда'),
	)
	SERVICE_ID = (
		(None, 'Выберете вид тренировки'),
		('1', 'Групповая'),
		('2', 'Индивидуальная'),
	)

	name = models.CharField(max_length=20, choices=NAME, verbose_name='Тренировка')
	description = models.TextField(max_length=1000, verbose_name='Описание')
	place = models.CharField(max_length=20, choices=PLACE, verbose_name='Место проведения')
	startTime = models.TimeField(verbose_name='Начало занятия')
	endTime = models.TimeField(verbose_name='Окончание занятия')
	weekDay = models.CharField(max_length=1, choices=WEEKDAY, verbose_name='День недели')
	servise_id = models.CharField(max_length=20, choices=SERVICE_ID, verbose_name='Вид тренировки')
	teacher_v2 = models.ForeignKey(Coach,on_delete=models.CASCADE, related_name='teachers', verbose_name='ФИО')
	color = models.CharField(max_length=10, choices=COLOR, verbose_name='Сложность')
	teacher = models.CharField(max_length=90,)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Дисциплина'
		verbose_name_plural = 'Дисциплины'
		unique_together = ('place', 'startTime', 'weekDay')


