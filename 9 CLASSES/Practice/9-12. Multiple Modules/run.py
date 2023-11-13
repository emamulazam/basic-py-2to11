from s_admin import Admin

me = Admin("emamul", 'azam')
me.privileges.privilege = ["can add post", "can delete post", "can ban user"]
me.privileges.show_privilege()
print(me.privileges.privilege)