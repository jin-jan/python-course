# -*- coding: utf-8 -*-
title = 'Whatever it takes'
#print("Title: '{}'\n".format(title))
genre = 'pop'
#print("Genre: '{}'\n".format(genre))
album = 'Evolve'
#print("Album: '{}'\n".format(album))
release_day = 23
release_month = 'June'
release_year = 2017
#print("Release date: '{}'\n".format(" ".join([release_month,
#                                              str(release_day),
#                                              str(release_year)])))
artist = 'Imagine Dragons'
#print("Artist: '{}'\n".format(artist))
members = ['Benjamin Arthur McKee',
           'Daniel Coulter Reynolds',
           'Daniel James Platzman',
           'Daniel Wayne Sermon']
#print("Members: \n{}\n".format("\n".join(members)))
hometown = {'Benjamin Arthur McKee':'Forestville, CA',
            'Daniel Coulter Reynolds': 'Las Vegas, NV',
            'Daniel James Platzman': 'Atlanta, GA',
            'Daniel Wayne Sermon': 'American Fork, UT'}
#print("Hometown per member: \n{}\n".format(hometown))
instrument = {'Benjamin Arthur McKee':'Bass',
              'Daniel Coulter Reynolds': 'Singer',
              'Daniel James Platzman': 'Percussion',
              'Daniel Wayne Sermon': 'Guitar'}
#print("Instruments per member: \n{}\n".format(instrument))
awards = ['MTV Video Music Award for Best Rock Video',
          'Teen Choice Award for Choice Rock Song']
#print("Awards: \n{}\n ".format("\n".join(awards)))
songwritters = ['Benjamin Arthur McKee',
                'Daniel Coulter Reynolds',
                'Daniel James Platzman',
                'Daniel Wayne Sermon', 
                'Joel Little']
#print("Songwritters: \n{}\n".format("\n".join(songwritters)))
copyright = 'Whatever It Takes lyrics © Universal Music Publishing Group, Sony/ATV Music Publishing LLC'
#print("Copyright: '{}'\n".format(copyright))
availability = ['Spotify',
                'Deezer',
                'Play Music',
                'Youtube',
                'iTunes']
#print("Availability: \n{}\n".format("\n".join(availability)))
duration_sec = 3.39
#print("Duration in seconds: '{}'\n".format(duration_sec))
lyrics = """Falling too fast to prepare for this
Tripping in the world could be dangerous
Everybody circling, it's vulturous
Negative, nepotist
Everybody waiting for the fall of man
Everybody praying for the end of times
Everybody hoping they could be the one
I was born to run, I was born for this
Whip, whip
Run me like a racehorse
Pull me like a ripcord
Break me down and build me up
I wanna be the slip, slip
Word upon your lip, lip
Letter that you rip, rip
Break me down and build me up
Whatever it takes
'Cause I love the adrenaline in my veins
I do whatever it takes
'Cause I love how it feels when I break the chains
Whatever it takes
You take me to the top I'm ready for
Whatever it takes
'Cause I love the adrenaline in my veins
I do what it takes
Always had a fear of being typical
Looking at my body feeling miserable
Always hanging on to the visual
I wanna be invisible
Looking at my years like a martyrdom
Everybody needs to be a part of 'em
Never be enough, I'm the prodigal son
I was born to run, I was born for this
Whip, whip
Run me like a racehorse
Pull me like a ripcord
Break me down and build me up
I wanna be the slip, slip
Word upon your lip, lip
Letter that you rip, rip
Break me down and build me up
Whatever it takes
'Cause I love the adrenaline in my veins
I do whatever it takes
'Cause I love how it feels when I break the chains
Whatever it takes
You take me to the top, I'm ready for
Whatever it takes
'Cause I love the adrenaline in my veins
I do what it takes
Hypocritical, egotistical
Don't wanna be the parenthetical, hypothetical
Working onto something that I'm proud of, out of the box
An epoxy to the world and the vision we've lost
I'm an apostrophe
I'm just a symbol to remind you that there's more to see
I'm just a product of the system, a catastrophe
And yet a masterpiece, and yet I'm half-diseased
And when I am deceased
At least I go down to the grave and die happily
Leave the body and my soul to be a part of thee
I do what it takes
Whatever it takes
'Cause I love the adrenaline in my veins
I do whatever it takes
'Cause I love how it feels when I break the chains
Whatever it takes
You take me to the top, I'm ready for
Whatever it takes
'Cause I love the adrenaline in my veins
I do what it takes"""
#print("Lyrics: \n\"{}\"\n".format(lyrics))
lines = lyrics.split('\n')
#print("Lines: \n{}\n".format("\n".join(lines)))
num_lines = len(lines)
#print("Number of lines: '{}'\n".format(num_lines)) 
num_words = len(lyrics.split())
#print("Number of words: '{}'\n".format(num_words))
list_love = [i for i in lines if 'love' in i]
#print("List of sentences using the word 'love': \n{}\n".format("\n".join(list_love)))
