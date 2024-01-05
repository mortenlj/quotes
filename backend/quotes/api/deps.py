from quotes.api.schemas import Quote

QUOTES = (
    Quote(id=1, quote="/earth is 98% full...  Please delete anyone you can."),
    Quote(id=2, quote="10.0 times 0.1 is hardly ever 1.0."),
    Quote(id=3, quote="A bad random number generator:  1, 1, 1, 1, 1, 4.33e+67, 1, 1, 1"),
    Quote(id=4, quote="A bug in the hand is better than one as yet undetected."),
    Quote(id=5, quote="A computer program does what you tell it to do, not what you want it to do."),
    Quote(id=6, quote="A Computer Scientist is someone who fixes things that aren't broken."),
    Quote(id=7, quote="After a number of decimal places, nobody gives a damn."),
    Quote(id=8, quote="An elephant is a mouse with an operating system."),
    Quote(id=9, quote="And on the seventh day, he exited from append mode."),
    Quote(id=10, quote="Any sufficiently advanced bug is indistinguishable from a feature.", dedication="Kulawiec"),
    Quote(id=11, quote="As far as we know, our computer has never had an undetected error.", dedication="Weisert"),
    Quote(id=12, quote="Asking whether machines can think is like asking whether submarines can swim."),
    Quote(id=13, quote="Avoid temporary variables and strange women."),
    Quote(id=14, quote="Base 8 is just like base 10, if you are missing two fingers.", dedication="Tom Lehrer"),
    Quote(id=15, quote="Beware of programmers who carry screwdrivers.", dedication="Leonard Brandwein"),
    Quote(id=16, quote="Breakthrough:  It finally booted on the first try."),
    Quote(id=17, quote="Compatible: Gracefully accepts erroneous data from any source."),
    Quote(id=18, quote="Computers are a more fun way to do the same work you'd have to do without them."),
    Quote(id=19, quote="Disc Space -- The Final Frontier!"),
    Quote(id=20, quote="Disclaimer: Any errors in spelling, tact, or fact are transmission errors."),
    Quote(id=21, quote="Don't hit the keys so hard, it hurts."),
    Quote(id=22, quote="Every program in development at MIT expands until it can read mail."),
    Quote(id=23, quote="Every program is a part of some other program, and rarely fits."),
    Quote(id=24, quote="Foolproof Operation:  All parameters are hard coded."),
    Quote(id=25, quote="Fortune:  No such file or directory"),
    Quote(id=26, quote="Futuristic: It will only run on a next generation supercomputer."),
    Quote(id=27, quote="Hardware: The parts of a computer system that can be kicked."),
    Quote(id=28, quote="Host system not responding, probably down.  Do you want to wait?  (Y/N)"),
    Quote(id=29, quote="I am a computer -- Dumber than any human and smarter than an administrator."),
    Quote(id=30, quote="I am still waiting for the advent of the computer science groupie."),
    Quote(id=31, quote="I am the computer your mother warned you about."),
    Quote(id=32, quote="I came, I saw, I deleted all your files."),
    Quote(id=33, quote="I haven't lost my mind; It's backed up on tape somewhere."),
    Quote(id=34, quote='If a "Train station" is where the train stops, what is a "Work station"?'),
    Quote(id=35, quote="If God had intended man to program, we would be born with serial I/O ports."),
    Quote(id=36, quote="If it was easy, the hardware people would take care of it."),
    Quote(id=37, quote="It is now pitch dark. If you proceed, you will likely fall into a pit."),
    Quote(id=38, quote="It is ten o'clock; Do you know where your processes are?"),
    Quote(id=39, quote="Kiss your keyboard goodbye!"),
    Quote(id=40, quote="Last one out, turn off the computer!"),
    Quote(id=41, quote="Life would be so much easier if we could just look at the source code."),
    Quote(id=42, quote="Lisp users: Due to the holiday, there will be no garbage collection on monday."),
    Quote(id=43, quote="Long computations that yield zero are probably all for naught."),
    Quote(id=44, quote="Machine-independent:  Does not run on any existing machine."),
    Quote(id=45, quote="Manual writer's creed:  Garbage in, gospel out."),
    Quote(id=46, quote="Maybe computer science should be in the college of theology.", dedication="R. S. Barton"),
    Quote(id=47, quote="Meets Quality Standards:  Compiles without errors."),
    Quote(id=48, quote="MIPS:  Meaningless Indicator Of Processor Speed."),
    Quote(id=49, quote='Netnews is like yelling, "Anyone want to buy a used car?" in a crowded theater.'),
    Quote(id=50, quote="Never trust a computer you can't lift.", dedication="Stan Masor"),
    Quote(id=51, quote="Nice computers don't go down."),
    Quote(id=52, quote="No program done by a hacker will work unless he is on the system."),
    Quote(id=53, quote="No program done by an undergrad will work after she graduates."),
    Quote(id=54, quote="People who deal with bits should expect to get bitten.", dedication="Jon Bentley"),
    Quote(id=55, quote="Portable: Survives system reboot."),
    Quote(id=56, quote="Programming Department:  Mistakes made while you wait."),
    Quote(id=57, quote="Programming is an unnatural act."),
    Quote(id=58, quote="Programming just with goto's is like swatting flies with a sledgehammer."),
    Quote(id=59, quote="Protect your software at all costs -- All else is meat."),
    Quote(id=60, quote="Random access is the optimum of the mass storages."),
    Quote(id=61, quote="Real programs don't eat cache."),
    Quote(id=62, quote="Remember the good old days, when CPU was singular?"),
    Quote(id=63, quote="Revolutionary:  Disk drives go round and round."),
    Quote(id=64, quote="Some programming languages manage to absorb change but withstand progress."),
    Quote(id=65, quote="System going down at 1:45 for disk crashing."),
    Quote(id=66, quote="System going down at 5 pm to install scheduler bug."),
    Quote(id=67, quote="Systems programmers are the high priests of a low cult.", dedication="R. S. Barton"),
    Quote(id=68, quote="The attention span of a computer is only as long as its power cord."),
    Quote(id=69, quote="The computer is mightier than the pen, the sword, and usually, the programmer."),
    Quote(id=70, quote="The determined programmer can write a fortran program in any language."),
    Quote(id=71, quote="The generation of random numbers is too important to be left to chance."),
    Quote(id=72, quote='The next generation of computers will have a "Warranty expired" interrupt.'),
    Quote(id=73, quote="The program is absolutely right; Therefore, the computer must be wrong."),
    Quote(id=74, quote="The world is coming to an end... Save your buffers!!"),
    Quote(id=75, quote="The world will end in 5 minutes. Please log out."),
    Quote(id=76, quote="There are two ways to write error-free programs; Only the third one works."),
    Quote(id=77, quote="There must be more to life than compile-and-go."),
    Quote(id=78, quote="This fortune soaks up 47 times its own weight in excess memory."),
    Quote(id=79, quote="This login session:  $13.76, but for you:  $11.88."),
    Quote(id=80, quote="This screen intentionally left blank."),
    Quote(id=81, quote="This system will self-destruct in five minutes."),
    Quote(id=82, quote="Those who can't write, write help files."),
    Quote(id=83, quote="To err is human; To forgive, beyond the scope of the operating system."),
    Quote(id=84, quote="To err is human; To really foul things up requires a computer."),
    Quote(id=85, quote="To iterate is human; To recurse, divine.", dedication="Robert Heller"),
    Quote(id=86, quote="Unprecedented performance:  Nothing ever ran this slow before."),
    Quote(id=87, quote='Where the system is concerned, you are not allowed to ask "Why?".'),
    Quote(id=88, quote="Why do we want intelligent terminals when there are so many stupid users?"),
    Quote(id=89, quote="You can't go home again, unless you set $HOME."),
    Quote(id=90, quote="You can't make a program without broken egos."),
    Quote(id=91, quote="You depend too much on computers for information."),
    Quote(id=92, quote="You forgot to do your backup 16 days ago.  Tomorrow you will need that version."),
    Quote(id=93, quote="You had mail, but the super-user read it, and deleted it!"),
    Quote(id=94, quote="You have a tendency to feel you are superior to most computers."),
    Quote(id=95, quote="You have junk mail."),
    Quote(id=96, quote="You know it is going to be a bad day when you forget your new password."),
    Quote(id=97, quote="You might have mail."),
    Quote(id=98, quote="You never finish a program, you just stop working on it."),
    Quote(id=99, quote="Your password is pitifully obvious."),
    Quote(id=100, quote="If anything can go wrong, it will.", dedication="Murphys Law §1"),
    Quote(
        id=101,
        quote="If there is a possibility of several things going wrong, the one that will cause the most damage will be the first one to go wrong.",
        dedication="Murphys Law §2",
    ),
    Quote(id=102, quote="If anything just cannot go wrong, it will anyway.  --  Murphys Law §3"),
    Quote(
        id=103,
        quote="If you perceive that there are four possible ways in which something can go wrong, and circumvent these, then a fifth way, unprepared for, will promptly develop.",
        dedication="Murphys Law §4",
    ),
    Quote(id=104, quote="Left to themselves, things tend to go from bad to worse.", dedication="Murphys Law §5"),
    Quote(
        id=105,
        quote="If everything seems to be going well, you have obviously overlooked something.",
        dedication="Murphys Law §6",
    ),
    Quote(id=106, quote="Nature always sides with the hidden flaw.", dedication="Murphys Law §7"),
    Quote(id=107, quote="Mother nature is a bitch.", dedication="Murphys Law §8"),
    Quote(
        id=108,
        quote="Just when you see the light at the end of the tunnel, the roof caves in.",
        dedication="Forsyth's Second Corollary To Murphy's Laws",
    ),
    Quote(
        id=109, quote="Nothing is impossible for the man who doesn't have to do it himself.", dedication="Weiler's Law"
    ),
    Quote(id=110, quote="Any given program, when running, is obsolete."),
    Quote(id=111, quote="Any given program costs more and takes longer each time it is run."),
    Quote(id=112, quote="If a program is useful, it will have to be changed."),
    Quote(id=113, quote="If a program is useless, it will have to be documented."),
    Quote(id=114, quote="Any given program will expand to fill all the available memory."),
    Quote(id=115, quote="The value of a program is inversely proportional to the weight of its output."),
    Quote(
        id=116, quote="Program complexity grows until it exceeds the capability of the programmer who must maintain it."
    ),
    Quote(
        id=117,
        quote="When a compiler accepts a program without error on the first run, the program will not yield the desired output.",
    ),
    Quote(
        id=118,
        quote="In nature, nothing is ever right. Therefore, if everything is going right... Something is wrong.",
        dedication="Addition To Murphy's Laws",
    ),
    Quote(
        id=119,
        quote="If builders built buildings the way programmers wrote programs, then the first woodpecker that came along would destroy civilization.",
        dedication="Weinberg's Second Law",
    ),
    Quote(id=120, quote="It Won't Work.", dedication="Jenkinson's Law"),
    Quote(id=121, quote="Anything that begins well ends badly.", dedication="Pudders Law §1"),
    Quote(id=122, quote="Anything that begins badly ends worse.", dedication="Pudders Law §2"),
    Quote(
        id=123,
        quote="No books are lost by lending except those you particularly wanted to keep.",
        dedication="Atwoods Corollary",
    ),
    Quote(
        id=124,
        quote="Any inanimate object, regardless of its position, configuration or purpose, may be expected to perform at any time in a totally unexpected manner for reasons that are either entirely obscure or else completely mysterious.",
        dedication="Flap's Law",
    ),
    Quote(id=125, quote="ATTENTION, all abducting aliens!  you DON'T need to RETURN them!"),
    Quote(
        id=126,
        quote="The difference between fiction and reality is that fiction has to make sense.",
        dedication="Tom Clancy",
    ),
    Quote(
        id=127,
        quote="Early to rise, early to bed, makes a man healthy, wealthy and dead.",
        dedication='Pratchett, "The Light Fantastic"',
    ),
    Quote(
        id=128,
        quote="To assert that the earth revolves around the sun is as erroneous as to claim that Jesus was not born of a virgin.",
        dedication="Cardinal Bellarmino 1615, during the trial of Galileo",
    ),
    Quote(
        id=129,
        quote="There's a fine line between genius and insanity.  I have erased this line.",
        dedication="Oscar Levant",
    ),
    Quote(id=130, quote="You can count on Intel, Just don't divide..."),
    Quote(
        id=131,
        quote="Cynicism: The idea that man acts selfishly. Buzhism: The idea that idiocy is just as big a factor.",
    ),
    Quote(id=132, quote="A penny for your thoughts. Mine are more expensive."),
    Quote(
        id=133,
        quote="Computers in the future may weigh no more than 1.5 tons.",
        dedication="Popular Mechanics, forecasting the relentless march of science, 1949",
    ),
    Quote(
        id=134,
        quote="I think there is a world market for maybe five computers.",
        dedication="Thomas Watson, chairman of IBM, 1943",
    ),
    Quote(
        id=135,
        quote="But what ... is it good for?",
        dedication="Engineer at the Advanced Computing Systems Division of IBM, 1968, commenting on the microchip.",
    ),
    Quote(
        id=136,
        quote="There is no reason anyone would want a computer in their home.",
        dedication="Ken Olson, president, chairman and founder of Digital Equipment Corp., 1977",
    ),
    Quote(
        id=137,
        quote="This 'telephone' has too many shortcomings to be seriously considered as a means of communication. The device is inherently of no value to us.",
        dedication="Western Union internal memo, 1876.",
    ),
    Quote(id=138, quote="Who the hell wants to hear actors talk?", dedication="H.M. Warner, Warner Brothers, 1927."),
    Quote(
        id=139,
        quote="We don't like their sound, and guitar music is on the way out.",
        dedication="Decca Recording Co. rejecting the Beatles, 1962.",
    ),
    Quote(
        id=140,
        quote="Heavier-than-air flying machines are impossible.",
        dedication="Lord Kelvin, president, Royal Society, 1895.",
    ),
    Quote(
        id=141,
        quote="Drill for oil? You mean drill into the ground to try and find oil? You're crazy.",
        dedication="Drillers who Edwin L. Drake tried to enlist to his project to drill for oil in 1859.",
    ),
    Quote(
        id=142,
        quote="Stocks have reached what looks like a permanently high plateau.",
        dedication="Irving Fisher, Professor of Economics, Yale University, 1929.",
    ),
    Quote(
        id=143,
        quote="Airplanes are interesting toys but of no military value.",
        dedication="Marechal Ferdinand Foch, Professor of Strategy, Ecole Superieure de Guerre.",
    ),
    Quote(
        id=144,
        quote="Everything that can be invented has been invented.",
        dedication="Charles H. Duell, Commissioner, U.S. Office of Patents, 1899.",
    ),
    Quote(
        id=145,
        quote="Louis Pasteur's theory of germs is ridiculous fiction.",
        dedication="Pierre Pachet, Professor of Physiology at Toulouse, 1872",
    ),
    Quote(id=146, quote="Black holes are where God divided by zero."),
    Quote(id=147, quote="This mind intentionally left blank."),
    Quote(id=148, quote="Time flies when you don't know what you're doing."),
    Quote(id=149, quote="Time is an illusion, lunchtime doubly so."),
    Quote(id=150, quote="To all virgins.  Thanks for nothing."),
    Quote(id=151, quote="To err is human, to forgive is against company policy."),
    Quote(id=152, quote="To err is human. To blame someone else is politics."),
    Quote(id=153, quote="To every rule there is an exception, and vice versa."),
    Quote(id=154, quote="Today is the tomorrow you worried about yesterday."),
    Quote(id=155, quote="Too much month at the end of the money."),
    Quote(id=156, quote="Trees hit cars only in self-defence."),
    Quote(id=157, quote="Tried to play my shoehorn... all I got was footnotes!"),
    Quote(id=158, quote="Two's company, three's the result."),
    Quote(id=159, quote="Unable to locate Coffee -- Operator Halted!"),
    Quote(id=160, quote="Virginity can be cured."),
    Quote(id=161, quote="Vuja De - The feeling you've never been here"),
    Quote(id=162, quote="WARNING ... drinking tap water can kill your thirst!"),
    Quote(id=163, quote="WARNING: my messages are offensive to morons!"),
    Quote(id=164, quote="Want a stupid answer? Ask me anything!"),
    Quote(id=165, quote="Was that your wife I saw in that GIF."),
    Quote(id=166, quote="Was today really Necessary?"),
    Quote(id=167, quote="We all live in a yellow subroutine."),
    Quote(id=168, quote="When in doubt, think."),
    Quote(id=169, quote="Where does weight go when you lose it?"),
    Quote(id=170, quote="Your feet have balls but not vice versa?"),
    Quote(id=171, quote="Your friendly neighborhood Atheist."),
    Quote(id=172, quote="Youth is a gift of nature. Age is a work of art."),
    Quote(id=173, quote="[DISCLAIMER:  my fingers are epileptic]"),
    Quote(id=174, quote="[If you can't hear me, it's because I'm in parentheses]"),
    Quote(id=175, quote="Every morning is the dawn of a new error..."),
    Quote(id=176, quote="Cannot find REALITY.SYS. Universe halted."),
    Quote(id=177, quote="COFFEE.EXE Missing - Insert Cup and Press Any Key to continue."),
    Quote(id=178, quote="Buy a Pentium III so you can reboot faster."),
    Quote(id=179, quote="Computers make very fast, very accurate mistakes."),
    Quote(id=180, quote="Computers are not intelligent. They only think they are."),
    Quote(id=181, quote="My software never has bugs. It just develops random features."),
    Quote(id=182, quote='Best file compression around: "DEL *.*" = 100% compression.'),
    Quote(id=183, quote="The Definition of an Upgrade: Take old bugs out, put new ones in."),
    Quote(id=184, quote="BREAKFAST.COM Halted. Cereal port not responding."),
    Quote(id=185, quote="The name is Baud, James Baud."),
    Quote(id=186, quote="Access denied. Thought you could get in?"),
    Quote(id=187, quote="Bad command or file name! Go stand in the corner."),
    Quote(id=188, quote="Bad command. Bad, bad, command! Sit! Bark! Stay!"),
    Quote(id=189, quote='Why doesn\'t DOS ever say "EXCELLENT command or filename?"'),
    Quote(id=190, quote="As a computer, I find your faith in technology amusing."),
    Quote(id=191, quote="File not found. Should I fake it? (y/n)"),
    Quote(id=192, quote="Ethernet: Something used to catch the EtherBunny."),
    Quote(id=193, quote="An error? Impossible! My modem is error correcting."),
    Quote(id=194, quote="CONGRESS.SYS Corrupted: Reboot Washington D.C? (y/n)"),
    Quote(id=195, quote="Does fuzzy logic tickle?"),
    Quote(id=197, quote="The magic of Windows: Turns a Pentium into an XT, instantly."),
    Quote(id=198, quote="SENILE.COM found. Out of memory."),
    Quote(id=199, quote="Who's General Failure and why is he reading my disk?"),
    Quote(id=200, quote="Ultimate office automation: networked coffee."),
    Quote(id=201, quote="Shell to DOS... Come in DOS, this is Shell calling, do you copy?"),
    Quote(id=202, quote="All computers wait at the same speed."),
    Quote(id=203, quote="Defination of a computer: A device designed to speed up and automate errors."),
    Quote(id=204, quote="Press <CTRL>-<ALT>-<DEL> to continue."),
    Quote(id=205, quote="AscII a stupid question, get a stupid ANSI!"),
    Quote(id=206, quote="E-mail returned to sender. Insufficient voltage."),
    Quote(id=207, quote="Hex dump: Where witches leave their used curses."),
    Quote(id=208, quote="Do witches run spell checkers?"),
    Quote(id=209, quote="Smash forehead on keyboard to continue."),
    Quote(id=210, quote="Enter any 11-digit prime number to continue."),
    Quote(id=211, quote="Press any key to continue or any other key to quit."),
    Quote(id=212, quote="Backup not found: (A)bort (R)etry (P)anic?"),
    Quote(
        id=213, quote="I used dip switches and connector wires to speed up my computer. It works just finE*Åä^'=ö:.¨\~"
    ),
    Quote(id=214, quote="Error! No keyboard detected. Press F1 to continue."),
    Quote(id=215, quote="Error! No mouse detected. Click here to continue."),
    Quote(id=216, quote="Error! Virus requires a different operating system."),
    Quote(id=217, quote="Ever noticed how fast Windows runs? Neither did I."),
    Quote(id=218, quote="Double your HD space, delete your operating system!"),
    Quote(id=219, quote="Is reading in the bathroom considered as multi-tasking?"),
    Quote(
        id=220, quote='My computer said that "Insert disk #3" but I couldn\'t get more than one disk fit in at a time!'
    ),
    Quote(id=221, quote="Bug? That's not a bug, that's a random feature!"),
    Quote(id=222, quote='The computer programmer\'s national anthem is "AAAAAARRRRGGGGHHH!"'),
    Quote(id=223, quote="If at first you don't succeed, call it a version 1.0."),
    Quote(id=224, quote="Asking if computers can think, is like asking if submarines can swim."),
    Quote(id=225, quote='Todays UNIX command: "EXSOP" = Execute System Operator.'),
    Quote(id=226, quote="Computer programming is an artform that fights back."),
    Quote(id=227, quote='Dad, what does "FORMATTING DRIVE C: 90% DONE" mean?'),
    Quote(id=228, quote="Windows loaded. System in danger."),
    Quote(id=229, quote="No errors detected. Yet."),
    Quote(id=230, quote="File Linking Error. Your mistake is now in every file."),
    Quote(id=231, quote="Erroneous Error. Nothing is wrong."),
    Quote(id=232, quote="Multitasking Attempted. System confused."),
    Quote(id=233, quote="System Price Error. Inadequate money spent on hardware."),
    Quote(id=234, quote="Broken Window. Watch out for glass fragments."),
    Quote(id=235, quote="Horrible Bug Encountered. No idea what has happened."),
    Quote(id=236, quote="Running low on diskspace. Free at least 2GB."),
    Quote(id=237, quote="Windows Closed. You can't look outside now."),
    Quote(id=238, quote="Unexplained Error. Please tell the programmer how is this possible."),
    Quote(id=239, quote="Keyboard Locked. Try anything you can think of."),
    Quote(id=240, quote="Illegal Error. You are not allowed to get this error, next time you will be punished."),
    Quote(id=241, quote="Timing Error. Please wait, and wait, and wait, and wait..."),
    Quote(id=242, quote="Process running. If not ready in 10 minutes, wait longer."),
    Quote(id=243, quote="This will end your Windows session, do you wish to play another game?"),
    Quote(id=244, quote="Timeout Error. Operator fell asleep waiting for the system to boot."),
    Quote(id=245, quote="Error! Computer hungry. Insert hamburger in drive A: and press Y to continue."),
    Quote(id=246, quote="Error! Programmer running out of cash. Insert Wallet in drive A: and remove when empty."),
    Quote(
        id=247,
        quote="Even if you're on the right track, you'll get run over if you just sit there.",
        dedication="Will Rogers",
    ),
    Quote(
        id=248,
        quote="The scientific theory I like best is that the rings of Saturn are composed entirely of lost airline luggage.",
        dedication="Mark Russell",
    ),
    Quote(id=249, quote="Me? A robot? That's ridiculous! For one thing, that doesn't compute at all!"),
    Quote(
        id=250,
        quote='The most exciting phrase to hear in science, the one that heralds the most discoveries, is not "Eureka!"  (I found it!)  but "That\'s funny..."',
        dedication="Isaac Asimov",
    ),
    Quote(id=251, quote="To err is human, but engineers write detailed documents on how they managed it"),
    Quote(
        id=252,
        quote="The brain is a wonderful organ. It starts working the moment you get up in the morning, and does not stop until you get into the office.",
        dedication="Robert Frost",
    ),
    Quote(id=253, quote="Logic is the art of going wrong with confidence.", dedication="Joseph Wood Krutch"),
    Quote(
        id=254,
        quote="The first man to fence in a piece of land saying 'This is mine' and who found people simple enough to believe him, was the real founder of civil society.",
        dedication="Jean-Jacques Rousseau",
    ),
    Quote(
        id=255,
        quote="The trouble with this country is that there are too many politicians who believe, with a conviction based on experience, that you can fool all of the people all of the time.",
        dedication="Franklin P. Adams",
    ),
    Quote(
        id=256,
        quote="The most essential mental quality for a free people, whose liberty is to be progressive, permanent and on a large scale, is much stupidity.",
        dedication="Walter Bagehot",
    ),
    Quote(
        id=257,
        quote="A lawyer is a learned gentleman who rescues your estate from your enemies and keeps it for himself.",
        dedication="Lord Brougham",
    ),
    Quote(
        id=258,
        quote="The only thing that stops God sending a second Flood is that the first one was useless.",
        dedication="Nicolas Chamfort",
    ),
    Quote(id=259, quote="I love the woooshing sounds deadlines make as they pass"),
    Quote(id=260, quote="Dejamoo : The feeling you've heard this bull before"),
    Quote(id=261, quote="The only Mac I trust is MacGyver."),
    Quote(id=262, quote="Programming from a spec is like walking on water.... Its easier to do when it's frozen."),
    Quote(id=263, quote="It's a 'timing' problem. It is just not time for the software to work, yet."),
    Quote(
        id=264, quote="We agree that the software performs to specification, but the specification does not make sense."
    ),
    Quote(id=265, quote="I do object-oriented programming - if the customer objects, I do more programming."),
    Quote(id=266, quote="It is easier to port a shell than a shell script."),
    Quote(id=267, quote="The only intuitive interface is the nipple. After that, it's all learned."),
    Quote(id=268, quote="The only thing worse than a computer you can't control is a computer you can."),
    Quote(
        id=269,
        quote="It is difficult to get a man to understand something when his salary depends upon his not understanding it.",
    ),
)


def get_db():
    return {q.id: q for q in QUOTES}
