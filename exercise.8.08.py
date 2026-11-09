def make_album(artist, title, tracks=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


while True:
    print("\nEnter album information (type 'q' at any time to quit).")

    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Album title: ")
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(album)