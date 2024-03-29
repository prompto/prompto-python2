from io import StringIO

from prompto.value.BaseValue import BaseValue
from prompto.value.IntegerValue import IntegerValue
from prompto.value.TextValue import TextValue
from prompto.error.SyntaxError import SyntaxError


class VersionValue (BaseValue):

    @staticmethod
    def Parse(literal):
        if literal == 'latest':
            return VersionValue.LATEST
        elif literal == 'development':
            return VersionValue.DEVELOPMENT
        else:
            return VersionValue.ParsePrefixedSemanticVersion(literal)

    @staticmethod
    def ParsePrefixedSemanticVersion(literal):
        if literal[0]=='v':
            literal = literal[1:]
        return VersionValue.ParseSemanticVersion(literal)

    @staticmethod
    def ParseSemanticVersion(literal):
        parts = literal.split("-")
        version = VersionValue.ParseVersionNumber(parts[0])
        if len(parts) > 1:
            version.qualifier = VersionValue.ParseVersionQualifier(parts[1])
        return version

    @staticmethod
    def ParseVersionQualifier(literal):
        if "" == literal:
            return 0
        elif "alpha" == literal:
            return -3
        elif "beta" == literal:
            return -2
        elif "candidate" == literal:
            return -1
        else:
            raise Exception("Version qualifier must be 'alpha', 'beta' or 'candidate'!")

    @staticmethod
    def ParseVersionNumber(literal):
        parts = literal.split(".")
        major = int(parts[0])
        minor = int(parts[1])
        fix = 0 if len(parts) == 2 else int(parts[2])
        return VersionValue(major=major, minor=minor, fix=fix)

    @staticmethod
    def ParseInt(value):
        major = value >> 24 & 0xFF
        minor = value >> 16 & 0xFF
        fix = value >> 8 & 0xFF
        qualifier = value & 0xFF
        return VersionValue(major, minor, fix, qualifier)

    def __init__(self, major=-1, minor=-1, fix=-1, qualifier=0):
        from prompto.type.VersionType import VersionType
        super(VersionValue, self).__init__(VersionType.instance)
        self.major = major
        self.minor = minor
        self.fix = fix
        self.qualifier = qualifier

    def CompareTo(self, context, value):
        if isinstance(value, VersionValue):
            if self.asInt() < value.asInt():
                return -1
            elif self.asInt() == value.asInt():
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Version - " + type(value).__name__)

    def asInt(self):
        return (self.major << 24) | (self.minor << 16) | (self.fix << 8) | self.qualifier

    def __eq__(self, obj):
        if isinstance(obj, VersionValue):
            return self.asInt() == obj.asInt()
        else:
            return False

    def __lt__(self, other):
        return self.asInt() < other.asInt()

    def __str__(self):
        if self == VersionValue.LATEST:
            return "latest"
        elif self == VersionValue.DEVELOPMENT:
            return "development"
        else:
            with StringIO() as sb:
                sb.write(u"v")
                sb.write(unicode(self.major))
                sb.write(u'.')
                sb.write(unicode(self.minor))
                if self.fix != 0:
                    sb.write(u'.')
                    sb.write(unicode(self.fix))
                if self.qualifier != 0:
                    sb.write(u'-')
                    sb.write(self.qualifierString())
                return sb.getvalue()

    def qualifierString(self):
        if self.qualifier == 0:
            return u""
        elif self.qualifier == -3:
            return u"alpha"
        elif self.qualifier == -2:
            return u"beta"
        elif self.qualifier == -1:
            return u"candidate"
        else:
            raise Exception("Unsupported qualifier: " + self.qualifier)

    def __hash__(self):
        return hash(self.asInt())


    def getMemberValue(self, context, name, autoCreate=False):
        if "major" == name:
            return IntegerValue(self.major)
        elif "minor" == name:
            return IntegerValue(self.minor)
        elif "fix" == name:
            return IntegerValue(self.fix)
        elif "qualifier" == name:
            return TextValue(self.qualifierString())
        else:
            return super(VersionValue, self).getMemberValue(context, name, autoCreate)


VersionValue.LATEST = VersionValue.ParseInt(0xFFFFFFFF)
VersionValue.DEVELOPMENT = VersionValue.ParseInt(0xFEFEFEFE)

