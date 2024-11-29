from abc import ABC, abstractmethod


# Target Interface (MediaPlayer)
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass


# Concrete Target (MP3Player)
class MP3Player(MediaPlayer):
    def play(self, audio_type: str, file_name: str):
        print(f"Playing MP3 file. Name: {file_name}")


# Adaptee (Legacy Media Player)
class MediaAdapter:
    def __init__(self, audio_type: str):
        self.audio_type = audio_type
        if audio_type == "mp4":
            self.player = MP4Player()
        elif audio_type == "vlc":
            self.player = VLCPlayer()

    def play(self, audio_type: str, file_name: str):
        if self.audio_type == "mp4":
            self.player.play_mp4(file_name)
        elif self.audio_type == "vlc":
            self.player.play_vlc(file_name)


# Adaptee 1 (MP4Player)
class MP4Player:
    def play_mp4(self, file_name: str):
        print(f"Playing MP4 file. Name: {file_name}")


# Adaptee 2 (VLCPlayer)
class VLCPlayer:
    def play_vlc(self, file_name: str):
        print(f"Playing VLC file. Name: {file_name}")


# Client Code
class AudioPlayer:
    def __init__(self):
        self.media_adapter = None

    def play(self, audio_type: str, file_name: str):
        if audio_type == "mp3":
            mp3_player = MP3Player()
            mp3_player.play(audio_type, file_name)
        elif audio_type in ["mp4", "vlc"]:
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, file_name)
        else:
            print("Invalid media format")


# Client Code Example
if __name__ == "__main__":
    audio_player = AudioPlayer()

    # Playing different types of media
    audio_player.play("mp3", "song1.mp3")  # Output: Playing MP3 file. Name: song1.mp3
    audio_player.play("mp4", "movie.mp4")  # Output: Playing MP4 file. Name: movie.mp4
    audio_player.play("vlc", "documentary.vlc")  # Output: Playing VLC file. Name: documentary.vlc
    audio_player.play("avi", "movie.avi")  # Output: Invalid media format
