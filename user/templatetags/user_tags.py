from urllib.parse import urlencode
from django import template

register = template.Library()

@register.simple_tag
def get_login_qq_url():
	params = {
		'response_type':'code',
		'client_id':'101893332',
		'redirect_url':'https://leyilee.top/user/login_by_qq',
		'state':'leyilee',

	}
	return 'https://graph.qq.com/oauth2.0/authorize?' + urlencode(params)
