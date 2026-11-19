def transform_users(data):
    """Clean and validate API user data, then return a list of valid users."""
    cleaned_users=[]
    for user in data:
        name=user['name']
        name= name.strip()
        email=user['email']
        email=email.strip()
        email=email.lower()
        user_id=user['id']
        if( isinstance(user_id,int) 
           and not isinstance(user_id,bool) and 
           user_id > 0 and 
           bool(name) and 
           bool(email)):
            clean_user={
            "user_id":user_id,
            "name":name,
            "email":email
             }
            cleaned_users.append(clean_user)
    return cleaned_users       