class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Song:
    def __init__(self, song_id, duration, singer, title):
        self.song_id = song_id
        self.duration = duration
        self.singer = singer
        self.title = title

class PlayListSong:
    def __init__(self, song):
        self.song = song
        self.frequency = 0
        self.users = set()
    
    def added_by_user(self, user_id):
        if user_id not in self.users:
            self.users.add(user_id)
        

class Playlist:
    def __init__(self, playlist_id, name, owner):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.songs = {}

    def add_song(self, user_id, song):
        if song.song_id not in self.songs:
            self.songs[song.song_id] = PlayListSong(song)
        self.songs[song.song_id].frequency += 1
        self.songs[song.song_id].added_by_user(user_id)
    
    def get_playlist_by_frequency(self):
        return sorted(self.songs.values(), key=lambda ps:ps.frequency, reverse=True)

class MusicService:
    def __init__(self):
        self.songs = {}
        self.playlists = {}
    
    def create_user(self, user_id, name, email):
        user = User(user_id, name, email)
        return user

    def create_song(self, song_id, duration, singer, music_by):
        song = Song(song_id, duration, singer, music_by)
        self.songs[song_id] = song
    
    def create_playlist(self, playlist_id, name, owner):
        playlist = Playlist(playlist_id, name, owner)
        self.playlists[playlist_id] = playlist
        
    def add_song_to_playlist(self, play_list_id, user_id, song_id):
        if play_list_id not in self.playlists:
            return "Playlist is not created"
        if song_id not in self.songs:
            return "Song is not created yet"
        self.playlists[play_list_id].add_song(user_id, self.songs[song_id])
    
    def get_playlist_by_frequency(self, play_list_id):
        if play_list_id not in self.playlists:
            return "Playlist is not created"
        return self.playlists[play_list_id].get_playlist_by_frequency()

if __name__ == "__main__":
    service = MusicService()
    service.create_user("U1", "Mayur", "mayur@xyz.com")
    service.create_user("U2", "Kirtan", "kirtan@xyz.com")

    service.create_song("S1", "2.35", "Arijit Singh", "Kaho na pyaar hai")
    service.create_song("S2", "3.35", "KK", "Mithwa")
    service.create_song("S3", "4.35", "Mayur", "Night is Alone")

    service.create_playlist("P1", "Love Songs", "U2")
    service.add_song_to_playlist("P1", "U1", "S1")
    service.add_song_to_playlist("P1", "U1", "S2")
    service.add_song_to_playlist("P1", "U2", "S2")
    service.add_song_to_playlist("P1", "U2", "S3")

    for ps in service.get_playlist_by_frequency("P1"):
        print(f"{ps.song.title} by {ps.song.singer} - Added by {len(ps.users)} users")


