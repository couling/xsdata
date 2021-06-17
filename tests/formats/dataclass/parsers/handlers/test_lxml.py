from unittest import mock
from unittest.case import TestCase

from lxml import etree

from tests import fixtures_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from tests.fixtures.books.fixtures import books
from tests.fixtures.books.fixtures import events
from tests.fixtures.books.fixtures import events_default_ns
from xsdata.exceptions import XmlHandlerError
from xsdata.formats.dataclass.parsers.bases import RecordParser
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.parsers.handlers import LxmlSaxHandler


class LxmlEventHandlerTests(TestCase):
    def setUp(self) -> None:
        self.parser = RecordParser(handler=LxmlEventHandler)

    def test_parse(self):
        path = fixtures_dir.joinpath("books/books.xml")
        self.assertEqual(books, self.parser.from_path(path, Books))
        self.assertEqual({"brk": "urn:books"}, self.parser.ns_map)
        self.assertEqual(events, self.parser.events)

    def test_parse_with_default_ns(self):
        path = fixtures_dir.joinpath("books/books_default_ns.xml")
        self.assertEqual(books, self.parser.from_path(path, Books))
        self.assertEqual({None: "urn:books"}, self.parser.ns_map)
        self.assertEqual(events_default_ns, self.parser.events)

    def test_parse_with_element_or_tree(self):
        path = fixtures_dir.joinpath("books/books.xml")
        tree = etree.parse(str(path))

        result = self.parser.parse(tree, Books)
        self.assertEqual(books, result)

        tree = etree.parse(str(path))
        result = self.parser.parse(tree.find(".//book"), BookForm)
        self.assertEqual(books.book[0], result)

    def test_parse_with_xinclude(self):
        path = fixtures_dir.joinpath("books/books-xinclude.xml")
        ns_map = {"brk": "urn:books", "xi": "http://www.w3.org/2001/XInclude"}

        self.parser.config.process_xinclude = True
        self.assertEqual(books, self.parser.from_path(path, Books))
        self.assertEqual(ns_map, self.parser.ns_map)

    def test_parse_with_xinclude_from_memory(self):
        path = fixtures_dir.joinpath("books/books-xinclude.xml")
        ns_map = {"brk": "urn:books", "xi": "http://www.w3.org/2001/XInclude"}

        self.parser.config.process_xinclude = True
        self.parser.config.base_url = path.as_uri()
        self.assertEqual(books, self.parser.from_bytes(path.read_bytes(), Books))
        self.assertEqual(ns_map, self.parser.ns_map)

    def test_parse_context_with_unhandled_event(self):
        handler = LxmlEventHandler(clazz=Books, parser=self.parser)

        with self.assertRaises(XmlHandlerError) as cm:
            handler.process_context([("reverse", "")])

        self.assertEqual("Unhandled event: `reverse`.", str(cm.exception))


class LxmlSaxHandlerTests(TestCase):
    def setUp(self):
        self.parser = RecordParser(handler=LxmlSaxHandler)

    def test_parse(self):
        path = fixtures_dir.joinpath("books/books.xml")
        self.assertEqual(books, self.parser.from_path(path, Books))
        self.assertEqual({"brk": "urn:books"}, self.parser.ns_map)
        self.assertEqual(events, self.parser.events)

    def test_parse_with_default_ns(self):
        path = fixtures_dir.joinpath("books/books_default_ns.xml")
        self.assertEqual(books, self.parser.from_path(path, Books))
        self.assertEqual({None: "urn:books"}, self.parser.ns_map)
        self.assertEqual(events_default_ns, self.parser.events)

    def test_parse_from_memory(self):
        path = fixtures_dir.joinpath("books/books.xml")
        self.assertEqual(books, self.parser.from_bytes(path.read_bytes(), Books))
        self.assertEqual({"brk": "urn:books"}, self.parser.ns_map)
        self.assertEqual(events, self.parser.events)

    def test_close_with_no_objects_returns_none(self):
        handler = LxmlSaxHandler(clazz=Books, parser=self.parser)
        self.assertIsNone(handler.close())

    @mock.patch.object(RecordParser, "end")
    def test_flush_normalizes_data_frames(self, mock_end):
        handler = LxmlSaxHandler(parser=self.parser, clazz=Books)
        handler.data_frames.append(([], []))
        handler.flush_next = "value"
        handler.flush()

        handler.data_frames.append((["a", "b"], [""]))
        handler.flush_next = "value"
        handler.flush()

        mock_end.assert_has_calls(
            [
                mock.call(handler.queue, handler.objects, "value", None, None),
                mock.call(handler.queue, handler.objects, "value", "ab", ""),
            ]
        )
        self.assertEqual(2, mock_end.call_count)

    def test_parse_with_xinclude_raises_exception(self):
        self.parser.config.process_xinclude = True

        with self.assertRaises(XmlHandlerError) as cm:
            self.parser.from_string("", Books)

        self.assertEqual(
            "LxmlSaxHandler doesn't support xinclude elements.", str(cm.exception)
        )
