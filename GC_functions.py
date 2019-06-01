def get_match1(this_user):
	
	#this_user = {"topics": ["1","2","3"]}
	all_users = {
	  "user1": {"topics": ["4","6","7"]},
	  "user2": {"topics": ["1","6","7"]},
	  "user3": {"topics": ["2","3","7"]},
	  "user4": {"topics": ["1","5"]}
	}
	
	match=[]
	similar=[]
		
	return_list = []
	for username, user_data in all_users.items():
		all_users[username]["common"] = list(set(this_user["topics"]) & set(user_data["topics"]))
		if len(user_data["common"]):
				return_list.append(username)
		
	return return_list
