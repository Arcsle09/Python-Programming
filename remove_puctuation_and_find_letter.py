import string 

def remove_punctuation(phrase):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    new_phrase = phrase_sans_punct.split()
    count = 0 
    for i in new_phrase:
        if "e" in i:
            count = count + 1
    print("Your text contains {0} words, of which {1}({2:.1f}%) contain an ".format(len(new_phrase),count,(count/len(new_phrase))*100)+'"e"'+".")

lp_phrase = """Put 'em up like this
Let me see 'em now, yeah
I like that
Yeah
This is not the end
This is not the beginning
Just a voice like a riot
Rocking every revision
But you listen to the tone
And the violent rhythm
And though the words sound steady
Something empty's within 'em
We say, "yeah"
Fists flying up in the air
Like we're holding onto something
That's invisible there
'Cause we're living at the mercy of
The pain and the fear
Until we tell it, forget it
Let it all disappear
Waiting for the end to come
Wishing I had strength to stand
This is not what I had planned
It's out of my control
Flying at the speed of light
Thoughts were spinning in my head
So many things were left unsaid
It's hard to let you go
I know what it takes to move on
(Oh) I know how it feels to lie
(Oh) all I wanna do is trade this life for something new
Holding on to what I haven't got
Sitting in an empty room
Trying to forget the past
This was never meant to last
I wish it wasn't so
I know what it takes to move on
(Oh) I know how it feels to lie
(Oh) all I wanna do is trade this life for something new
Holding on to what I haven't got
Yeah, yeah
What was left when that fire was gone?
I thought it felt right but that right was wrong
All caught up in the eye of the storm
And trying to figure out what it's like moving on
And I don't even know what kind of things I've said
My mouth kept moving and my mind went dead
So, picking up the pieces, now where to begin?
The hardest part of ending is starting again
All I wanna do is trade this life for something new
Holding on to what I haven't got
This is not the end
This is not the beginning
Just a voice like a riot
Rocking every revision
But you listen to the tone (holding on to what I haven't got)
And the violent rhythm
Though the words sound steady
Something empty's within 'em
We say, "yeah"
With fists flying up in the air
Like we're holding onto something
That's invisible there
'Cause we're living at the mercy of (holding on to what I haven't got)
The pain and the fear
Until we get it, forget it
Let it all disappear"""