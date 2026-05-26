// Source https://cogu.github.io/apx/specification/idl/apx_idl_12

Document
    ApxHeader '\n' Statements

ApxHeader
    'APX/1.2'

Statements
    Statement '\n'
    Statement '\n' Statement

Statement
   NodeDeclaration
   TypeDeclaration
   RequirePortDeclaration
   ProvidePortDeclaration

NodeDeclaration
    'N' Name

TypeDeclaration
    'T' Name TypeSignature
    'T' Name TypeSignature ':' TypeAttributes

RequirePortDeclaration
    'R' Name TypeSignature
    'R' Name TypeSignature ':' PortAttributes

ProvidePortDeclaration
    'P' Name TypeSignature
    'P' Name TypeSignature ':' PortAttributes

Name
    '"' NameChars '"'

Names
    Name
    Name ',' Names

NameChars
    NameChar
    NameChar NameChars

NameChar
    'a' . 'z'
    'A' . 'Z'
    '0' . '9'
    '_'
    '-'

TypeSignature
    PrimitiveType
    PrimitiveType '[' OneNine Digits ']'
    'T[' Digits ']'
    '{' RecordElements '}'

PrimitiveType
    c
    s
    l
    u
    C
    S
    L
    U

RecordElements
    Name TypeSignature
    Name TypeSignature ',' RecordElements

TypeAttributes
    TypeAttribute
    TypeAttribute ',' TypeAttributes

TypeAttribute
    VT(Names)

PortAttributes
    PortAttribute
    PortAttributes ',' PortAttributes

PortAttribute
    '=' Integer
    '=' StringLiteral

Integer
    Digit
    OneNine Digits
    '-' Digit
    '-' OneNine Digits
    '0x' HexDigits

Digits
    Digit
    Digit Digits

Digit
    '0'
    OneNine

OneNine
    '1' . '9'
HexDigits
    HexDigit
    HexDigit HexDigits

HexDigit
    Digit
    'a' . 'f'
    'A' . 'F'

StringLiteral
    '"' '"'
    '"' Characters '"'

Characters
    character
    character characters

character
    '0020' . '007F' - '"'