from http.cookies import SimpleCookie


def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


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
