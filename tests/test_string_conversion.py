from dynagrpc import snake2pascal, pascal2snake
from pytest import mark

@mark.parametrize(
    'pascal, snake',
    [
        ('CreateEnumDict', 'create_enum_dict'),
        ('RegisterEnumType', 'register_enum_type'),
        ('ValuesByName', 'values_by_name'),
        ('RegisterGoogleTypes', 'register_google_types'),
    ]
)
def test_conversion_cases(pascal, snake):
    assert pascal2snake(pascal) == snake 
    assert snake2pascal(snake) == pascal 
    assert snake2pascal('_'+snake) == pascal 
