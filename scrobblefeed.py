import pylast
import timestuff

API_KEY = "ada4529ad4a007695ea71ab23da78dac"
API_SECRET = "a8d9caa037bc7b31c23c54339ad39a2d"

lastfm_network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET)

user = lastfm_network.get_user("m_degenaro")

friends_list = user.get_friends()



# Loops through friends_list, and adds a string to 'now_playing_list' 
# containing the currently playing song and who's playing it
def poll_friends():
	now_playing_list = []
	for friend in friends_list:
		now_playing = str(friend.get_now_playing())
		friend_name = str(friend.get_name())
		if(now_playing != "None"):
			now_playing_list.append(friend_name + ": " + now_playing)
	return now_playing_list

# returns the total amount of scrobbles today for given user
def scrobbles_today():
	return str((len(user.get_recent_tracks(limit=400, time_from=timestuff.yesterday_midnight()))))


# returns the total amount of scrobbles in the last seven days for the given user
def scrobbles_7d():
	return str((len(user.get_recent_tracks(limit=1000,time_from=timestuff.week_ago()))))



