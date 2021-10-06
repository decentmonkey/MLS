init python:
    licenses_text = "\nFollowing music compositions used in project 'MILFs of Sunville' are licensed by Jamendo S.A. (licensing.jamendo.com)\n\n\
3 A.M. (ABOVE ENVY)\n\
A Little More (Acoustic) (NEMO WILSON)\n\
A New Perspective On Life (BDKSONIC)\n\
Adventures of the Deaf Dreamer (JOSH WOODWARD)\n\
Baby Baby (LEO DYNAMIC)\n\
I'll Be Right Behing You (JOSH WOODWARD)\n\
Border Blaster (JOSH WOODWARD)\n\
Boy Loves Girl (FADING AUTUMN)\n\
Carefree Ukulele (SEASTOCK)\n\
Corporate_BPM120 (ARACHANG)\n\
Crazy Glue (MELANIE UNGAR)\n\
Deeper For You (MELANIE UNGAR)\n\
Don't Close Your Eyes (JOSH WOODWARD)\n\
Elle avait pas les yeux noirs (LÖHSTANA DAVID)\n\
Et c'est triste (LÖHSTANA DAVID)\n\
Fly With Me (STEEP)\n\
Fun Happy Energetic Rock (SOUNDATELIER)\n\
Future Bass (ALEXGROHL)\n\
Happy Acoustic (AKASHIC RECORDS)\n\
Happy Whistling Ukulele (SEASTOCK)\n\
Have A Good Day (MICHAEL HAHN)\n\
He Wants (LAU)\n\
Acoustic Inspiration (JOYSTOCK)\n\
Let Me Let You Let Go (ABOVE ENVY)\n\
Light it Up (SAMUEL HANSON)\n\
Little Tomcat (JOSH WOODWARD)\n\
Montana (DANIEL ROBINSON)\n\
Motivating Inspiring (ALEXGROHL)\n\
Never Been Gone (ABOVE ENVY)\n\
Postcard From Hell (JOSH WOODWARD)\n\
Remember Me (SEASTOCK)\n\
Right Now (LAU)\n\
Sandy Shoes (FADING AUTUMN)\n\
Secretions (HELLO CITIZEN)\n\
She Lost Her Wings (JOSH WOODWARD)\n\
Shining Through (ALUMO)\n\
Step By Step (STEFANO VITA)\n\
Story of One Success (AKASHIC RECORDS)\n\
Stylish Fashion Electronic Rock (ALEXGROHL)\n\
Stylish Hip Hop Rock (ALEXGROHL)\n\
Summernight (SLEEPING SKY)\n\
The Brave Worms of the Future (HELLO CITIZEN)\n\
The Heat (INFRACTION)\n\
Upbeat Summer Electro-Pop (JOYSTOCK)\n\
Visions Of Plenty (KEN VERHEECKE)\n\
Write Your Story (JOYSTOCK)\n\
"

screen licenses():
    tag menu

    use game_menu(t_("Licenses"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "Licenses"
            text t__(licenses_text)
