# script to convert text to emoji

def convert_text_to_emoji(text):
    words = text.split(" ")
    dict_emojis = { "happy": "😀", "sad":"😔", "angry":"😡", ":)":"😊"}

    converted_text = ""

    for word in words:
        converted_text += dict_emojis.get(word, word) + " "
    print(converted_text)


def main():
    text = input("Enter your text: ")
    convert_text_to_emoji(text)

if __name__ == "__main__":
    main()
    
