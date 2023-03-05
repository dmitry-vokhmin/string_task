from string import StringType, String, HashString, BaseString


class StringFactory:
    string_classes = {
        StringType.string: String,
        StringType.hash_string: HashString,
    }

    @classmethod
    def create(cls, string_type: StringType, chars: str = '') -> BaseString:
        return cls.string_classes[string_type](chars)
