#by deviousname

emoji_dictionary = {
"😀 ":"Grinning Face",
"😁 ":"Grinning Face with Smiling Eyes",
"😂 ":"Face with Tears of Joy",
"😃 ":"Smiling Face with Open Mouth",
"😄 ":"Smiling Face with Open Mouth and Smiling Eyes",
"😅 ":"Smiling Face with Open Mouth and Cold Sweat",
"😆 ":"Smiling Face with Open Mouth and Tightly-Closed Eyes",
"😇 ":"Smiling Face with Halo",
"😈 ":"Smiling Face with Horns",
"😉 ":"Winking Face"
}

for key, value in emoji_dictionary.items():
    print(f'{key} {value}')

while (x := input("Which emoji? ")).lower() not in ["quit","exit","stop","end","escape"]:
    if x in list(emoji_dictionary.keys()):    
        print(f'Ahhh {x}, the "{emoji_dictionary[x]}" emoji.')        
    else:    
        emoji_list = []        
        for key, value in emoji_dictionary.items():
            if x in value.lower():
                emoji_list.append(key)                
        if emoji_list != []:
            print(f'Found the following emojis: {emoji_list}')
        else:
            print('No emoji found fitting that description.')
print(f"Okay, let's {x}.")
