print ()
print ('Welcome to <The Way Home> adventure game.')
print ('First of all, please be ready for the following scenarios \nthat bring you into a strange place, but remember one true principal\n - Life will find its way out!')
print ()
print ('Please tell me some basic information.')
print ()
name = input ('What is your name? ')
print ()
age = input ('How old are you? ')
print ()
print ("That's right. " + str (name.capitalize()) + ', good luck!')
print ()
print ('You are walking through a dark forest alone, it is difficult to tell the time, luckily you find two items: a MATCH and a FLASHLIGHT.')
answer1 = input ('Which one do you pick up? [MATCH / FLASHLIGHT] ')
answer1 = str (answer1.lower())
print ()
if answer1 == 'match':
    print ('A match is better than none, but the light is limit, you barely see a path on your left, and you see an old car on your right.')
    answer1_1 = input ('Which way do you want to go? [LEFT / RIGHT] ')
    answer1_1 = str (answer1_1.lower())
    print ()
    if answer1_1 == 'left':
        print ('Your match burn out, you walk slowly on the path, moon light is the only help in the dark. Wind blow woo woo woo. You are scared.')
        print ('You remember your mom taught you pray.')
        answer1_1_1 = input ('Do you want to PRAY or CRY? ')
        answer1_1_1 = str (answer1_1_1.lower())
        print ()
        if answer1_1_1 == 'pray':
            print ('You stop walking, close your eyes and do a prayer sincerely. You hope God will save you. You make a promise in your heart that if you are saved, you must pay back to the God')
            print ('A light spot on you suddenly. An old women holding a flashlight and ask do you need help?')
            print ('You can not believe God answer your prayer immediately!!!')
            answer1_1_1_1 = input ('Do you NEED the woman help, or it is FINE? [NEED / FINE] ')
            answer1_1_1_1 = str(answer1_1_1_1.lower())
            print()
            if answer1_1_1_1 == 'need':
                print ('The old woman take her little old car and drive you back to a town.')
                print ('You are blessed. You are safe now. You dad find you right on the street.')
                print ('Congratulation! You find the way back home.')
            elif answer1_1_1_1 == 'fine':
                print ('You refuse the woman help. You think people always can not tell good or bad. You do not think she is the answer of your prayer.')
                print ('But you ask her for the location of here. She does not understand why you do not know where is here. She tell you a word but you can not understand.')
                answer1_1_1_1_2 = input ('Do you want to TALK to the woman a little bit more, or WALK away because she is talking none scense? [TALK / WALK] ')
                answer1_1_1_1_2 = str(answer1_1_1_1_2.lower())
                print ()
                if answer1_1_1_1_2 == 'talk':
                    print ('You finally understand what she is talking about, she has very heavy country accent.')
                    print ('She said she has a car that can drive you out of here.')
                    answer1_1_1_1_2_1 = input ('Do you TRUST her and get on her car? or you still want to WALK by youself? [TRUST / WALK] ')
                    answer1_1_1_1_2_1 = str(answer1_1_1_1_2_1.lower())
                    print ()
                    if answer1_1_1_1_2_1 == 'trust':
                        print ('The old woman take her little old car and drive you back to a town.')
                        print ('You are blessed. You are safe now. You dad find you right on the street.')
                        print ('Congratulation! You find the way back home.')
                    elif answer1_1_1_1_2_1 == 'walk':
                        print ('You keep moving with no light, no food and no direction.')
                        print ('It is getting more cold at night. You walk on the path and into the trees again')
                        print ('Unfortunately, your stubborn make you miss the last help .')
                        print ('GAME OVER')
                    else:
                        print('Please select a valid option. Try again.')
                elif answer1_1_1_1_2 == 'walk':
                    print ('You keep moving with no light, no food and no direction.')
                    print ('It is getting more cold at night. You walk on the path and into the trees again')
                    print ('Unfortunately, Wolves appear in front of your way. You have been eaten.')
                    print ('GAME OVER')
                else:
                    print('Please select a valid option. Try again.')
            else:
                print('Please select a valid option. Try again.')        
        elif answer1_1_1 == 'cry':
            print ('Your voice break the silence in the dark. A few wolves howl back, sound like they respond to your voice.')
            print ('Unfortunately, a real wolf appear and stare at you in front of your way.')
            answer_after_cry = input ('Quick action, do you want to stare back at the wolf or run? [STARE / RUN] ')
            answer_after_cry = str(answer_after_cry.lower())
            print()
            if answer_after_cry == 'stare':
                print('The wolf freeze its motion a few minutes.')
                input('[press enter]')
                print('Suddenly, it run away.')
                print('You are so luck.')
                answer_after_stare = input('You sweat so much, because you just escap from death. Do you want to fo back search the old car or find somewhere to hide? [SEARCH / HIDE] ')
                answer_after_stare = str(answer_after_stare.lower())
                print()
                if answer_after_stare == 'search':
                    print ('Thats a good idea. You search the old car and find a flashlight and a baseball bat.')
                    print ('Now you can see clearly the way and you have a weapon to protect yourself. You see a wood house is not far from here.')
                    answer_after_oldcar = input ('Do you want to get inside the HOUSE or walk around to SEARCH this area? [HOUSE / SEARCH] ')
                    answer_after_oldcar = str(answer_after_oldcar.lower())
                    print()
                    if answer_after_oldcar == 'house':
                        print ('You are lucky, you find a phone! Now you want to make a phone call immediately!!!')
                        answer_after_house = input ('Do you want to call your MOM, or your DAD? [MOM / DAD] ')
                        answer_after_house = str (answer_after_house.lower())
                        print ()
                        if answer_after_house == 'mom':
                            print ('Your mom is worried to death, but you do not know where you are.')
                            print ('Your mom teach you to pray sincerely and ask for help from Heavenly Father.')
                            input ('[press enter]')
                            print ('This is always a wise choice.')
                            print ('Congratulation! Angel appears and take you back home.')
                        elif answer_after_house == 'dad':
                            print ('You dad is so worried. He is finding you everywhere.')
                            print ('You just only know you are at countryside.')
                            print ('You dad teach you to go on the top of the house, and then flash your flashlight.')
                            print ('Congratulation! Police helicopter finds you and take you back home.')
                        else:
                            print('Life is made of choices, you have to choose one. Try again.')
                    elif answer_after_oldcar == 'search':
                        print ('Darkness is horrible.')
                        print ('You get lost in the wood and can not find any help.')
                        print ('Probably, maybe you should get inside the house to see if you can get some rest and stay warm.')
                        print ('Unfortunately, Wolves appear in front of your way. You have been eaten.')
                        print ('GAME OVER')
                    else:
                        print('Please select a valid option. Try again.')
                elif answer_after_stare == 'hide':
                    print ('It is getting cold. You can not find any places to hide.')
                    print ('Hide can not survive. You are cold to death. ')
                    print ('GAME OVER')
                else:
                    print('Please select a valid option. Try again.')
            elif answer_after_cry == 'run':
                print ('The wolf chase you, human run so slow.')
                print ('You have been eaten.')
                print ('GAME OVER')
            else:
                print('Please select a valid option. Try again.')
        else:
            print('Life is made of choices, you have to choose one. Try again.')    
    elif answer1_1 == 'right':
        print ('Thats a good idea. You search the old car and find a flashlight and a baseball bat.')
        print ('Now you can see clearly the way and you have a weapon to protect yourself. You see a wood house is not far from here.')
        answer1_1_2 = input ('Do you want to get inside the HOUSE or walk around to SEARCH this area? [HOUSE / SEARCH] ')
        answer1_1_2 = str(answer1_1_2.lower())
        print()
        if answer1_1_2 == 'house':
            print ('You are lucky, you find a phone! Now you want to make a phone call immediately!!!')
            answer1_1_2_1 = input ('Do you want to call your MOM, or your DAD? [MOM / DAD] ')
            answer1_1_2_1 = str (answer1_1_2_1.lower())
            print ()
            if answer1_1_2_1 == 'mom':
                print ('Unfortunately, no one pick up the phone. You remember your mom used to turn off the phone when she sleeps.')
                answer1_1_2_1_1 = input ('Do you want to call your DAD? or SEARCH the house? [DAD / SEARCH] ')
                answer1_1_2_1_1 = str (answer1_1_2_1_1.lower())
                print ()
                if answer1_1_2_1_1 == 'dad':
                    print ('Your dad is worried about you, but you can not tell where you are because you have no idea. Your dad remind you to calm down, make sure you are safe, and wait for the sunrise.')
                    print ('You listen to your dad, stay safe and wait for the sun rise.')
                    print ('This is a wise choice.')
                    print ('Congratulation! You find the way back home.')











                elif answer1_1_2_1_1 == 'search':
                    print ('The door close by itself. You open every wardrobe drawers and closets.')
                    print ('Nervous spend much your energy. You vaguely hear some voices come from the ground.')
                    input ('[press enter]')
                    print ('You find an oil lamp, some matches, a rusty key and a thick wood stick.')
                    answer_house_1 = input ('Do you want to uncover the carpet? [YES / NO] ')
                    answer_house_1 = str(answer_house_1.lower())
                    print()
                    if answer_house_1 == 'yes':
                        print ('An ancient wooden cellar appear on the floor. After you sweep out the dust, a key hole is at the center of the cellar.')
                        print ('The sound come from it more clear now.')
                        answer_house_1_1 = input ('Which tool do you want to use? [oil lamp / key / wood stick] ')
                        answer_house_1_1 = str(answer_house_1_1.lower())
                        print()
                        if answer_house_1_1 == 'key':
                            print ('It is so rusty. You are pretty sure that the key shape is right but it can not twit the lock.')
                            print ('What to do now?')
                            print ('[A] Try to crush the door with the wood stick.\n[B] Pour some lamp oil into the key hole.\n[C] Do not care about it and leave it. ')
                            answer_house_1_1_1 = input ('What is your choice? ')
                            answer_house_1_1_1 = str(answer_house_1_1_1.lower())
                            print()
                            if answer_house_1_1_1 == 'a':
                                print ('You spend all of your energy but the cellar is unbeatable.')
                                print ('A cellar guardian appear on the air to protect the ancient cellar, you are frightened.')
                                print ('You run out of the house and eaten by wolves.')
                                print ('GAME OVER')
                            elif answer_house_1_1_1 == 'b':
                                print ('You remeber what your dad taught. You pour some oil into the hole, then the key is work, you open the lock.')
                                print ('The cellar is so dusty, it looks like has not been opened for a long time.')
                                print ('There is a down stair.')
                                answer_house_1_1_1_stair = input ('Are you dare to see what is down stair? [YES / NO] ')
                                answer_house_1_1_1_stair = str(answer_house_1_1_1_stair.lower())
                                print()
                                if answer_house_1_1_1_stair == 'yes':
                                    print ('You are brave! Blessing come from Heaven, your flashlight and baseball bat are glowing.')
                                    print ('You walk carefully and your flashlight is very bright!')
                                    input ('[press enter]')
                                    print ('you see an endless tunnel, build by rock, look so old.')
                                    print ('[A]Strike match to light up the old torch on the wall.\n[B]Keep going with your flashlight.')
                                    answer_house_1_1_1_stair_down = str(input ('What is your choice? ')).lower()
                                    print()
                                    if answer_house_1_1_1_stair_down == 'a':
                                        print ('The tunnel is light up because you use match to light each wall torch.')
                                        print ('You keep moving forward until you arrive to a big room.')
                                        print ('A skeleton stand up from the ground, and come toward you.')
                                        input ('[press enter]')
                                        print ('You use the bat to hit it with two hand. It is crashed.')
                                        print ('You think you become a brave worrior now.')
                                        answer_deeper = str(input('Do you want to go deeper or go back? [DEEPER / BACK] ')).lower()
                                        print()
                                        if answer_deeper == 'deeper':
                                            print ('After another long tunnel path, you see a little light.')
                                            print ('Suddenly a stone wall fall down from the top.')
                                            input ('[press enter]')
                                            print ('')

                                            
                                        else:
                                            print ('You sit down on the floor and take some rest.')
                                            print ('Suddenly a huge red spider scroll down from the ceiling.')
                                            print ('You scared and run out of the house and eaten by wolves.')
                                            print ('GAME OVER')
                                    else:
                                        print ('You keep moving forward until you arrive to a big room.')
                                        print ('A skeleton stand up from the ground, and come toward you.')
                                        print ('You just have one hand to swing the bat, it is not enough power to hit the thing.')
                                        print ('You are dead.')
                                        print ('GAME OVER')
                                else:
                                    print ('You sit down on the floor and take some rest.')
                                    print ('Suddenly a huge red spider scroll down from the ceiling.')
                                    print ('You scared and run out of the house and eaten by wolves.')
                                    print ('GAME OVER')

                            elif answer_house_1_1_1 == 'c':
                                print ('You sit down on the floor and take some rest.')
                                print ('Suddenly a huge red spider scroll down from the ceiling.')
                                print ('You scared and run out of the house and eaten by wolves.')
                                print ('GAME OVER')
                            else:
                                print ('Life is made of choices, you have to choose one. Try again.')
                        else:
                            print ('It is not for this. Try again.')
                    elif answer_house_1 == 'no':
                        print ('You sit down on the floor and take some rest.')
                        print ('Suddenly a huge red spider scroll down from the ceiling.')
                        print ('You scared and run out of the house and eaten by wolves.')
                        print ('GAME OVER')
                    else:
                        print('Please select a valid option. Try again.')
                else:
                    print('Please select a valid option. Try again.')










            elif answer1_1_2_1 == 'dad':
                print ('Your dad is worried about you, but you can not tell where you are because you have no idea. Your dad remind you to calm down, make sure you are safe, and wait for the sunrise.')
                answer1_1_2_1_2 = input ('Do you want to KEEP moving or STAY? [KEEP / STAY] ')
                answer1_1_2_1_2 = str (answer1_1_2_1_2.lower())
                print ()
                if answer1_1_2_1_2 == 'keep':
                    print ('You get lost again and can not find any help.')
                    print ('You should listen to your dad advice.')
                    print ('Unfortunately, Wolves appear in front of your way. You have been eaten.')
                    print ('GAME OVER')
                elif answer1_1_2_1_2 == 'stay':
                    print ('You sit down by the wall and fall asleep.')
                    print ('The sun is rise when you open your eyes.')
                    print ('You are wise because you listen to your dad.')
                    print ('Congratulation! You find the way back home.')
                else:
                    print('Please select a valid option. Try again.')
            else:
                print('Please select a valid option. Try again.')
        elif answer1_1_2 == 'search':
            print ('You see a wood house on the side of the path, a large farm behind the house, and a sign near by the fence.')
            print ('The house has no light, some horses in the farm field, and the sign said "Be ware of wolves!"')
            answer1_1_2_2 = input ('You can choose one place to investigate, the HOUSE or the FIELD? [HOUSE / FIELD] ')
            answer1_1_2_2 = str (answer1_1_2_2.lower())
            print ()
            if answer1_1_2_2 == 'house':
                print ('You are lucky, you find a phone! Now you want to make a phone call immediately!!!')
                answer1_1_2_2_1 = input ('Do you want to call your MOM, or your DAD? [MOM / DAD] ')
                answer1_1_2_2_1 = str (answer1_1_2_2_1.lower())
                print ()
                if answer1_1_2_2_1 == 'mom':
                    print ('Unfortunately, no one pick up the phone. You remember your mom used to turn off the phone when she sleeps.')
                    answer1_1_2_2_1_1 = input ('Do you want to call your DAD? or SEARCH the house? [DAD / SEARCH] ')
                    answer1_1_2_2_1_1 = str (answer1_1_2_2_1_1.lower())
                    print ()
                    if answer1_1_2_2_1_1 == 'dad':
                        print ('Your dad is worried about you, but you can not tell where you are because you have no idea. Your dad remind you to calm down, make sure you are safe, and wait for the sunrise.')
                        print ('You listen to your dad, stay safe and wait for the sun rise.')
                        print ('This is a wise choice.')
                        print ('Congratulation! You find the way back home.')










                    elif answer1_1_2_2_1_1 == 'search':
                        print ('The door close by itself. You open every drawers and closets.')
                        print ('Nervous spend much your energy. Darkness make you tired and sleepy.')
                        print ('Unfortunately, you find nothing and you run out of energy.')
                        print ('GAME OVER')










                    else:
                        print('Life is made of choices, you have to choose one. Try again.')
                elif answer1_1_2_2_1 == 'dad':
                    print ('Your dad is worried about you, but you can not tell where you are because you have no idea. Your dad remind you to calm down, make sure you are safe, and wait for the sunrise.')
                    answer1_1_2_2_1_2 = input ('Do you want to KEEP moving or STAY and rest? [STAY / REST] ')
                    answer1_1_2_2_1_2 = str (answer1_1_2_2_1_2.lower())
                    print ()
                    if answer1_1_2_2_1_2 == 'keep':
                        print ('You get lost again and can not find any help.')
                        print ('You should listen to your dad advice.')
                        print ('Unfortunately, Wolves appear in front of your way. You have been eaten.')
                        print ('GAME OVER')
                    elif answer1_1_2_2_1_2 == 'rest':
                        print ('You sit down by the wall and fall asleep.')
                        print ('The sun is rise when you open your eyes.')
                        print ('You are wise because you listen to your dad.')
                        print ('Congratulation! You find the way back home.')
                    else:
                        print('Please select a valid option. Try again.')
                else:
                    print('Please select a valid option. Try again.')
            elif answer1_1_2_2 == 'field':
                print ('You want to ride a horse to get out of here. But horses are not easy to accept stranger especially in the dark.')
                print ('You go find something eat to feed the horse or keep trying to ride on it?')
                answer1_1_2_2_2 = input ('What do you think? [FEED / TRY] ')
                answer1_1_2_2_2 = str (answer1_1_2_2_2.lower())
                print ()
                if answer1_1_2_2_2 == 'feed':
                    print ('You find a carrot and the horse is happy now. You can ride on it. It makes you feel warm and calm.')
                    print ('It helps you go through the trees quickly. Now you see a vehicle road and a big barn.')
                    print ('Congratulation! You find the way back home.')
                elif answer1_1_2_2_2 == 'try':
                    print ('The horse does not let you to ride on it. You fall down, it is painful. You get up and walk slowly back to the house. It is your only choice now.')
                    print ('The door is locked. You can not go inside.')
                    print ('You continue on the path. You get lost in the trees unfortunately.')
                    print ('GAME OVER')
                else:
                    print('Wolves appear in front of your way. You have been eaten.')
            else:
                print('Wolves appear in front of your way. You have been eaten.')
        else:
            print('Wolves appear in front of your way. You have been eaten.')
    else:
        print ('Life is made of choices, you have to choose one. Try again.')

elif answer1 == 'flashlight':
    print ("You are smart. The light show you clearly there is a wood house not far away on your left hand side, and there are some horses in the large farm field on your right.")
    answer1_2 = input ('You can choose. Do you want to go into the HOUSE or go to the FIELD? [HOUSE / FIELD] ')
    answer1_2 = str (answer1_2.lower())
    print ()
    if answer1_2 == 'house':
        print ('You are lucky, you find a phone! Now you want to make a phone call immediately!!!')
        answer1_2_1 = input ('Do you want to call your MOM, or your DAD? [MOM / DAD] ')
        answer1_2_1 = str (answer1_2_1.lower())
        print ()
        if answer1_2_1 == 'mom':
            print ('Unfortunately, no one pick up the phone. You remember your mom used to turn off the phone when she sleeps.')
            answer1_2_1_1 = input ('Do you want to call your DAD? or SEARCH the house? [DAD / SEARCH] ')
            answer1_2_1_1 = str (answer1_2_1_1.lower())
            print ()
            if answer1_2_1_1 == 'dad':
                print ('Your dad is worried about you, but you can not tell where you are because you have no idea. Your dad remind you to calm down, make sure you are safe, and wait for the sunrise.')
                print ('You listen to your dad, stay safe and wait for the sun rise.')
                print ('This is a wise choice.')
                print ('Congratulation! You find the way back home.')










            elif answer1_2_1_1 == 'search':
                print ('The door close by itself. You open every drawers and closets.')
                print ('Nervous spend much your energy. Darkness make you tired and sleepy.')
                print ('Unfortunately, you find nothing and you run out of energy.')
                print ('GAME OVER')




                





            else:
                print ('Oops...You need to choose one. Please try again.')
        elif answer1_2_1 == 'dad':
            print ('Your dad is worried about you, but you can not tell where you are because you have no idea. Your dad remind you to calm down, make sure you are safe, and wait for the sunrise.')
            answer1_2_1_2 = input ('Do you want to KEEP moving or STAY and rest? [KEEP / STAY] ')
            answer1_2_1_2 = str (answer1_2_1_2.lower())
            print ()
            if answer1_2_1_2 == 'keep':
                print ('You get lost again and can not find any help.')
                print ('You should listen to your dad advice.')
                print ('Unfortunately, you can not make it.')
                print ('GAME OVER')
            elif answer1_2_1_2 == 'rest':
                print ('You sit down by the wall and fall asleep.')
                print ('The sun is rise when you open your eyes.')
                print ('You are wise because you listen to your dad.')
                print ('Congratulation! You find the way back home.')
            else:
                print ('Oops...You need to choose one. Please try again.')
        else:
            print ('Oops...You need to choose one. Please try again.')
    elif answer1_2 == 'field':
        print ('You want to ride a horse to get out of here. But horses are not easy to accept stranger especially in the dark.')
        print ('You go find something eat to feed the horse or keep trying to ride on it?')
        answer1_2_2 = input ('What do you think? [FEED / TRY] ')
        answer1_2_2 = str (answer1_2_2.lower())
        print ()
        if answer1_2_2 == 'feed':
            print ('You find a carrot and the horse is happy now. You can ride on it. It makes you feel warm and calm.')
            print ('It helps you go through the trees quickly. Now you see a vehicle road and a big barn.')
            print ('Congratulation! You find the way back home.')
        elif answer1_2_2 == 'try':
            print ('The horse does not let you to ride on it. You fall down, it is painful. You get up and walk slowly back to the house. It is your only choice now.')
            print ('The door is locked. You can not go inside.')
            print ('You continue on the path. You get lost in the trees unfortunately.')
            print ('GAME OVER')
        else:
            print ('Oops...You need to choose one. Please try again.')
    else:
        print ('Oops...You need to choose one. Please try again.')
else:
    print ('Life is made of choices, you have to choose one. Try again.')


