__author__ = 'igonef'

from django.template import Library
from djangosphinx.utils import config
from django.template.base import Node, NodeList, Template, Context, Variable

register = Library()

class RelativePathNode(Node):
    def __init__(self, pathparts):
        self.pathparts = pathparts

    def render(self, context):
        result = config.relative_path(*self.pathparts)
        return result

@register.tag
def relative_path(parser, token):
    args = token.split_contents()
    #print args
    if len(args) < 2:
        raise TemplateSyntaxError("'relative_path' tag requires at least two arguments")
    else:
        values = [arg for arg in args[1:]]
        node = RelativePathNode(values)
        return node