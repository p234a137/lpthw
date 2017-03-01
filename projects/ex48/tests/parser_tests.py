from nose.tools import *
from ex48 import parser


# word_list = [('stop', 'of'), ('verb', 'go'), ('noun', 'princess'), ('verb', 'am'), ('direction', 'left'), ('verb', 'do'), ('noun', 'dog'), ('stop', 'the'),  ]

def test_peek():
    word_list = [('stop', 'of'), ('verb', 'go')]
    assert_equal(parser.peek(word_list), 'stop')


def test_match():
    word_list = [('stop', 'of'), ('verb', 'go')]
    assert_equal(parser.match(word_list, 'stop'), ('stop', 'of'))
    assert_equal(parser.match(word_list, 'verb'), ('verb', 'go'))


def test_skip():
    word_list = [('stop', 'of'), ('verb', 'go'), ('noun', 'princess')]
    parser.skip(word_list,'stop')
    assert_equal(word_list, [('verb', 'go'), ('noun', 'princess')])
    parser.skip(word_list,'verb')
    assert_equal(word_list, [('noun', 'princess')])


def test_parse_verb():
    word_list = [('stop', 'of'), ('verb', 'go')]
    assert_equal(parser.parse_verb(word_list), ('verb', 'go'))


def test_parse_object():
    word_list = [('stop', 'of'), ('noun', 'princess'), ('direction', 'left')]
    assert_equal(parser.parse_object(word_list), ('noun', 'princess'))
    assert_equal(parser.parse_object(word_list), ('direction', 'left'))


def test_parse_subject():
    word_list = [('stop', 'it'), ('verb', 'went'), ('direction', 'left')]
    s1 = parser.Sentence(('noun', 'dog'), ('verb', 'went'), ('direction', 'left'))
    s2 = parser.parse_subject(word_list,('noun', 'dog'))
    assert_equal((s1.subject, s1.verb, s1.object), (s2.subject, s2.verb, s2.object))


def test_parse_sentence():
    word_list = [('stop', 'the'), ('noun', 'dog'), ('verb', 'went'), ('direction', 'left')]
    s1 = parser.Sentence(('noun', 'dog'), ('verb', 'went'), ('direction', 'left'))
    s2 = parser.parse_sentence(word_list)
    assert_equal((s1.subject, s1.verb, s1.object), (s2.subject, s2.verb, s2.object))


def test_parse_sentence2():
    word_list = [('stop', 'it'), ('verb', 'went'), ('direction', 'left')]
    s1 = parser.Sentence(('noun', 'player'), ('verb', 'went'), ('direction', 'left'))
    s2 = parser.parse_sentence(word_list)
    assert_equal((s1.subject, s1.verb, s1.object), (s2.subject, s2.verb, s2.object))

