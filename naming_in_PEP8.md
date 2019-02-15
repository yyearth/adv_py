
# Naming Convention in PEP 8 

### Naming Style
* b (single lowercase letter)
* B (single uppercase letter)
* lowercase
* lowercase_with_underscore
* UPERCASE
* UPERCASE_WITH_UNDERSCORE
* CapitalizedWords or CapWords or CamelCase 驼峰法
* mixedCase (prefered in Java)

#### In addition, some have special meaning.

* \_single_leading_underscore: weak internal use. E.g. from M import * does not import \_them
* single_trailing_underscore_: avoid conflicts with keywords. E.g. class_
* \_\_double_leading_underscore: when naming a class attribute, invokes naming mangling. E.g. class FooBar.\_\_boo becomes \_FooBar\_\_boo
* \_\_double_leading_and_trailing_underscore__: magic objects or attributes

### Names to Avoid 
Never use 'l el', 'O oh' or 'I eye' as single character names.

* Package name: lowercase
* Module name: lowercase, lowercase_with_underscore (if improves readability) 
* Class name: CapWords
* Function name: lowercase, lowercase_with_underscore
* Variable name: lowercase, lowercase_with_underscore
* Constants name: UPERCASE, UPERCASE_WITH_UNDERSCORE
