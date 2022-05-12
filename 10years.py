print("This program makes it less tedious to make ch139 references.")
print("How it works is it gives you part of Eren's 139 breakdown, and you can type anything, and it will replace the dash in the prompt with that.")
print('''For example if you write \"Annie pegging Armin\" into the first prompt,
and \"him to receive my seed and no one elses\" into the second,
and \"to keep rewarding him with my seed\" into the third, the program will print out

\"NO, I DON'T WANT THAT!
ANNIE PEGGING ARMIN...?!
I WANT HIM TO RECEIVE MY SEED AND NO ONE ELSES FOR THE REST OF MY LIFE!
EVEN AFTER I DIE... I WANT TO KEEP REWARDING HIM WITH MY SEED FOR A WHILE! TEN YEARS, AT LEAST!!\"
''')
print("Note that the program will automatically change your input into uppercase since Eren is yelling in the scene.")
mikasa = input("NO! I DON'T WANT THAT! --- ...?! ")
restofmylife = input("I WANT --- FOR THE REST OF MY LIFE! ")
tenyearsatleast = input("EVEN AFTER I DIE... I WANT --- FOR A WHILE! TEN YEARS, AT LEAST!! ")
mikasa = mikasa.upper()
restofmylife = restofmylife.upper()
tenyearsatleast = tenyearsatleast.upper()
print()
print("NO! I DON'T WANT THAT! ", sep = '')
print(mikasa, "...?! ", sep = '')
print("I WANT ", restofmylife, " FOR THE REST OF MY LIFE! ", sep = '')
print("EVEN AFTER I DIE... I WANT ", tenyearsatleast, " FOR A WHILE! TEN YEARS, AT LEAST!!", sep = '')
print()
input("Press Enter once you have copied the above to close. ")