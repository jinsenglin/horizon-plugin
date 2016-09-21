from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def mytag(context):
    request = context['request']
    user = request.user
    perms = user.get_all_permissions()

    output = ['<div>',
              'user.get_all_permissions()<br/>',
              '<br/>'.join(perms),
              '</div>']
    outstr = ''.join(output)
    return outstr
