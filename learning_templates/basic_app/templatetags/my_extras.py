from django import template
register=template.Library()

def cut(value,arg):
    """
    This cuts out all values of "args" from the string!
    
    """
    return value.replace(args,'')

register.filter('cut',cut)
