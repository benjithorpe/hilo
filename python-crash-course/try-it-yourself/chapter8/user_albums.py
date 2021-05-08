def make_album(artist_name, album_title, number_of_songs=None):
    album = {"artist": artist_name.title(), "album": album_title.title()}

    if not number_of_songs:
        return album
    else:
        album["number_of_song"] = number_of_songs
        return album

while True:
    print("\nEnter 'q' to quit")

    album = input("Enter artist name: ")
    if album == 'q':
        break

    title = input("Enter album title: ")
    if title == 'q':
        break

    print(make_album(album, title))
