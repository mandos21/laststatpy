import curses
import scrobblefeed
import time
from datetime import datetime, timedelta
from curses import wrapper

global last_call 
last_call = datetime.now() - timedelta(minutes=3)

global tscrob 
tscrob = ""

global wscrob 
wscrob = ""

global slist 
slist = []



def time_sensitive(current_time):
	global last_call
	if(current_time >= (last_call + timedelta(minutes=2))):
		data_fetch()
		last_call = datetime.now()
		

def data_fetch():
	global tscrob
	global wscrob
	global slist
	temp = scrobblefeed.poll_friends()
	if(slist != temp):
		slist = temp

	temp2 = scrobblefeed.scrobbles_today()
	if(tscrob != temp2):
		tscrob = temp2

	temp3 = scrobblefeed.scrobbles_7d()
	if(wscrob != temp3):
		wscrob = temp3

	text_window.clear()
	text_window.refresh()
	
	text_window.addstr("Scrobble User Data" + "\n\n",curses.A_REVERSE)
	text_window.chgat(-1,curses.A_REVERSE)
	text_window.addstr("Scobbles Today: " + tscrob + "\n")
	#text_window.addstr("\n")
	text_window.addstr("Scobbles Last 7 Days: " + wscrob + "\n")
	text_window.addstr("\n\n")

	if(len(slist) >= 1):
		text_window.addstr("Friends Now Scrobbling" + "\n\n",curses.A_REVERSE)
		#text_window.chgat(-1,curses.A_REVERSE)

	for np in slist:
		text_window.addstr(np + "\n\n")


stdscr = curses.initscr()

# Properly initialize the screen

curses.noecho()
curses.cbreak()
curses.curs_set(0)

#curses.assume_default_colors()

# BEGIN PROGRAM

stdscr.addstr("ScrobbleFeed - Matthew DeGenaro V1.0", curses.A_REVERSE)
stdscr.chgat(-1, curses.A_REVERSE)

bottom_text = "Press 'Q' to quit	" + "Last Refreshed: " + last_call.strftime("%I:%M:%S")

stdscr.addstr(curses.LINES-1, 0, bottom_text)


# Window that holds text display
window = curses.newwin(curses.LINES-2,curses.COLS, 1,0)

# Create a sub-window to cleanly display the quote without
# overwriting border
text_window = window.subwin(curses.LINES-6,curses.COLS-4, 3,2)

text_window.addstr("Gathering Last.fm Data...")

# Apply a box to the window object
window.box()

# Update the internal window data structures
stdscr.noutrefresh()
window.noutrefresh()
text_window.noutrefresh()

# Redraw the screen

curses.doupdate()




while True:
	
	time_sensitive(datetime.now())
	
	# Refresh windows from the bottom up

	stdscr.noutrefresh()
	window.noutrefresh()
	text_window.noutrefresh()
	curses.doupdate()



	if(text_window.getch() == ord('q')):
		break
	
		
# Restore the terminal settings
stdscr.clear()
stdscr.refresh()
curses.nocbreak()
curses.curs_set(1)
curses.echo()
curses.endwin()
