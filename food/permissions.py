def can_access_admin(user):
    return user.role == 'admin'

def can_access_caretaker(user):
    return user.role in ['admin', 'caretaker']

def can_access_chief(user):
    return user.role in ['admin', 'chief']
