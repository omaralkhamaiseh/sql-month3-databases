def transform_users(data):
    cleaned_users=[]
    for d in data:
        name=d['name']
        name=name.strip()
        email=d['email']
        email=email.strip()
        email=email.lower()
        user_id=d['id']
        if (isinstance(user_id,int) and
        user_id > 0 and
        not isinstance(user_id,bool) and 
        bool(name) and bool(email)):
            cleaned_user={
            "id":user_id,
            "name":name,
            "email":email 
            }
            cleaned_users.append(cleaned_user)
    return cleaned_users