import os
import pygame

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = self.load_music()
        self.current_index = 0
        self.is_playing = False
        self.track_length = 0

    def load_music(self):
        files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".mp3") or file.endswith(".wav"):
                files.append(file)
        return files
    
    def play(self):
        if not self.playlist:
            return
        
        track_path = os.path.join(self.music_folder, self.playlist[self.current_index])

        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()

        sound = pygame.mixer.Sound(track_path)
        self.track_length = sound.get_length()

        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return

        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        if not self.playlist:
            return
        
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        if not self.playlist:
            return "No track"
        return self.playlist[self.current_index]
    
    def get_position(self):
        pos = pygame.mixer.music.get_pos()
        return max(0, pos / 1000) #seconds
    
    def get_progress(self):
        if self.track_length == 0:
            return 0
        return self.get_position() / self.track_length
        
        
