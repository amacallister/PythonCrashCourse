def make_album(artist_name, album_title, make_album = None):
    album = {'artist_name': artist_name, 'album_title': album_title}

    if make_album:
        album["make_album"] = make_album

    print(album)
    return album

make_album('Taylor Swift', 'Midnights')
make_album('Beyonce', 'Cowboy Carter')
make_album('Amanda MacAllister', 'Greatest Hits', 15)