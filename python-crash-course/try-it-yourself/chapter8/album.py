def make_album(artist_name, album_title, number_of_songs=None):
    album = {"artist": artist_name.title(), "album": album_title.title()}

    if not number_of_songs:
        return album
    else:
        album["number_of_song"] = number_of_songs
        return album


print(make_album('shawn mendes', 'cool one'))
print(make_album('harry styles', 'sugar', 20))
print(make_album('john legend', 'future', 5))
print(make_album('tatiana manaois', 'like you'))
