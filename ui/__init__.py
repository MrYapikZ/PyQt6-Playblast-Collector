from . import navigation, preference

def register():
    preference.register()
    navigation.register()

def unregister():
    preference.unregister()
    navigation.unregister()