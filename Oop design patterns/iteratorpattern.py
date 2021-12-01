from abc import ABC,abstractmethod

class SongIter(ABC):
	@abstractmethod
	def create_iterator(self):
		pass
	

class EngSong(SongIter):
	def __init__(self):
		self.max = 0
		self.album = []
		
	def add_song(self,song):
		self.album.append(song)
		self.max +=1
		
	def create_iterator(self):
		def decrement():
			if self.max>0:
				self.max-=1
				return self.album[self.max]
		return decrement
			
		
				
class Mix:
	def __init__(self,song_list):
		self.song_list = song_list
	
	def get_song(self):
		song= self.song_list.create_iterator()
		return song()
		
		
		
		
eng = EngSong()
eng.add_song('Baby')
eng.add_song('Waka Waka')
eng.add_song('Dance Monkey')		
mix = Mix(eng)
for j in range(3):
	song=mix.get_song()
	print(song)


		
	