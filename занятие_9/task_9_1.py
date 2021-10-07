violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
sum_of_songs = violator_songs_dict.get('Sweetest Perfection') + violator_songs_dict.get(
    'Policy of Truth') + violator_songs_dict.get('Blue Dress')
print(f' общее время звучание трех песен: {round(sum_of_songs, 2)}')
print(f' общее время звучания песен: {sum(violator_songs_dict.values())}')
