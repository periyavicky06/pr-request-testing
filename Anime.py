# Anime Recommendation System
# Created by Numan 😊

def recommend_anime(genre):
    anime_list = {
        "action": ["Attack on Titan", "One Punch Man", "Naruto", "My Hero Academia"],
        "romance": ["Your Name", "Toradora", "Clannad", "Kaguya-sama: Love is War"],
        "comedy": ["Gintama", "Konosuba", "The Disastrous Life of Saiki K", "Ouran High School Host Club"],
        "fantasy": ["Fullmetal Alchemist: Brotherhood", "Re:Zero", "Demon Slayer", "The Rising of the Shield Hero"],
        "mystery": ["Death Note", "Steins;Gate", "Erased", "The Promised Neverland"],
        "slice of life": ["Barakamon", "March Comes in Like a Lion", "Fruits Basket", "Your Lie in April"]
    }

    genre = genre.lower()
    if genre in anime_list:
        print(f"\n🎬 Recommended {genre.capitalize()} Anime:")
        for anime in anime_list[genre]:
            print(f" - {anime}")
    else:
        print("\n😅 Sorry, I don't have recommendations for that genre yet!")


print("🌸 Welcome to the Anime Recommendation System 🌸")
print("Available genres: Action, Romance, Comedy, Fantasy, Mystery, Slice of Life")

user_genre = input("\nEnter your favorite anime genre: ")
recommend_anime(user_genre)

print("\n✨ Enjoy your anime marathon! ✨")
