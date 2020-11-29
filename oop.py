import time
class MelodyNote(object):
	"""docstring for MelodyNote"""
	def __init__(self):
		print("Тетрадь создана\nopen - открыть тетрадь\nexit - выйти из программы\n")
		self.songs = [];
	def open(self):
		print("1 - добавить песню\n2 - прослушать песню\n3 - удалить песню\n\nимеющиеся песни:")
		n = 0
		for i in self.songs:
			n += 1
			print(n, " - ", i.name)
		print("\n")
	def add(self):
		print("Введите название песни")
		name = input()
		son = Song(name)
		son.add()
		self.songs.append(son);
	def listen(self):
		print("Введите индекс песни")
		index = int(input()) - 1
		son = self.songs[index]
		print("1 - минор\n2 - мажор")
		x = input()
		if '1' == x:
			for i in son.notes:
				i.MusicalMood('minor') 
		if '2' == x:
			for i in son.notes:
				i.MusicalMood('major') 
		son.open()

	def delete(self):
		print("Введите индекс песни")
		index = int(input()) - 1
		del self.songs[index]
		pass
note = MelodyNote();

class Song(object):
	def __init__(self, name):
		self.name = name
		self.notes = []
		pass
	def open(self):
		for i in self.notes:
			print(i.value)
		print("кол-во нот - ", self.quantity)
		print("\n")
	def add(self):
		print("Введите ноты")
		text = input() 
		for i in text.split(','):
			note = Note(i)
			self.notes.append(note)
		pass
		self.quantity = len(text)

class Note(object):
	def __init__(self, value):
		self.value = value
	def	MusicalMood(self, mod):
		if (mod == 'major'):
			self.value = self.value.upper()
		if (mod == 'minor'):
			self.value = self.value.lower()
		
while 1:
	inp = input()
	if inp == 'open':
		note.open()
	elif inp == 'exit':
		break
	elif inp == '1':
		note.add()
	elif inp == '2':
		note.listen()
	elif inp == '3':
		note.delete() 