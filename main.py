from urllib import parse as p
from http.cookies import SimpleCookie


def parse(query: str) -> dict:
    p.urlsplit(query)
    p.parse_qs(p.urlsplit(query).query)
    result = dict(p.parse_qsl(p.urlsplit(query).query))
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/pagename=11&color=222') == {}
    assert parse('https://example.com/path/to/page?1=2&1=2&1=2&1=2&1=2&1=2&') == {'1': '2'}
    assert parse('https://example.com/path/to/page?car=smart&color=green&fuel_type=diesel&') == \
           {'car': 'smart', 'color': 'green', 'fuel_type': 'diesel'}
    assert parse('https://example.com/path/to/page?=&') == {}
    assert parse('https://example.com/path/to/page?name=1&name=2&name=3') == {'name': '3'}
    assert parse('https://example.com/path/to/page?name=ferret=1&color=blue') == {'name': 'ferret=1', 'color': 'blue'}
    assert parse('https://example.com/path/to/page?!=!&!!=!!') == {'!': '!', '!!': '!!'}
    assert parse('https://example.com/path/to/page?q=w&e=r&t=y') == {'q': 'w', 'e': 'r', 't': 'y'}
    assert parse('https://example.com/path/to/page?якийсь=1&текст=2') == {'якийсь': '1', 'текст': '2'}
    assert parse('https://example.com/path/to/page?!@$%^*()=1&{}[]:;",<.>/?=1') == \
           {'!@$%^*()': '1', '{}[]:;",<.>/?': '1'}


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    res = {k: v.value for k, v in cookie.items()}
    return res


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('1=1;1=1;') == {'1': '1'}
    assert parse_cookie('name;age=28;') == {}
    assert parse_cookie('name=Dima;age=28;gender=male') == {'name': 'Dima', 'age': '28', 'gender': 'male'}
    assert parse_cookie('!=!;') == {'!': '!'}
    assert parse_cookie('=Dima') == {}
    assert parse_cookie('.=.') == {'.': '.'}
    assert parse_cookie('1=1;1=2;1=3;1=4') == {'1': '4'}
    assert parse_cookie('name=Dima;;;;;;;;;;;;') == {'name': 'Dima'}
    assert parse_cookie('name_1=Dima?;') == {'name_1': 'Dima?'}
    assert parse_cookie('FSDFSDFSDF=SDFSDFSDF') == {'FSDFSDFSDF': 'SDFSDFSDF'}
